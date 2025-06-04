from django.shortcuts import render, redirect, get_object_or_404
from .models import Grocery, Kitchen, Snack, History
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import csv
from django.http import HttpResponse
import json
from django.contrib import messages

# Authentication Views


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'base.html')

# Grocery CRUD

@login_required
def grocery_list(request):
    query = request.GET.get('q')
    if query:
        stocks = Grocery.objects.filter(
            Q(name__icontains=query) |
            Q(remarks__icontains=query)
        )
    else:
        stocks = Grocery.objects.all()
    return render(request, 'groceries/index.html', {'stocks': stocks, 'query': query})

@login_required
def grocery_add(request):
    if request.method == 'POST':
        balance = int(request.POST['balance'])
        stock_in = int(request.POST['stock_in'])
        stock_out = int(request.POST['stock_out'])
        unit_price = float(request.POST['unit_price'])
        total_balance = balance + stock_in - stock_out
        total_cost = total_balance * unit_price

        item = Grocery.objects.create(
            name=request.POST['name'],
            balance=balance,
            stock_in=stock_in,
            stock_out=stock_out,
            remarks=request.POST['remarks'],
            total_balance=total_balance,
            unit_price=unit_price,
            total_cost=total_cost
        )

        History.objects.create(
            action='Add',
            item_name=item.name,
            category='Grocery',
            user=request.user
        )
        return redirect('grocery_list')
    return render(request, 'groceries/add.html')

@login_required
def grocery_edit(request, id):
    stock = get_object_or_404(Grocery, id=id)
    if request.method == 'POST':
        stock.name = request.POST['name']
        stock.balance = int(request.POST['balance'])
        stock.stock_in = int(request.POST['stock_in'])
        stock.stock_out = int(request.POST['stock_out'])
        stock.remarks = request.POST['remarks']
        stock.unit_price = float(request.POST['unit_price'])
        stock.total_balance = stock.balance + stock.stock_in - stock.stock_out
        stock.total_cost = stock.total_balance * stock.unit_price
        stock.save()

        History.objects.create(
            action='Update',
            item_name=stock.name,
            category='Grocery',
            user=request.user
        )

        return redirect('grocery_list')
    return render(request, 'groceries/edit.html', {'stock': stock})

@login_required
def grocery_delete(request, id):
    stock = get_object_or_404(Grocery, id=id)
    if request.method == 'POST':
        History.objects.create(
            action='Delete',
            item_name=stock.name,
            category='Grocery',
            user=request.user
        )
        stock.delete()
        return redirect('grocery_list')
    # Optional: If you're no longer using the delete.html template
    return redirect('grocery_list')


@login_required
def kitchen_list(request):
    query = request.GET.get('q')
    if query:
        kitchens = Kitchen.objects.filter(
            Q(name__icontains=query) |
            Q(remarks__icontains=query)
        )
    else:
        kitchens = Kitchen.objects.all()
    return render(request, 'kitchen/index.html', {'items': kitchens, 'query': query})

@login_required
def kitchen_add(request):
    if request.method == 'POST':
        balance = int(request.POST['balance'])
        stock_in = int(request.POST['stock_in'])
        stock_out = int(request.POST['stock_out'])
        unit_price = float(request.POST['unit_price'])
        total_balance = balance + stock_in - stock_out
        total_cost = total_balance * unit_price

        item = Kitchen.objects.create(
            name=request.POST['name'],
            balance=balance,
            stock_in=stock_in,
            stock_out=stock_out,
            remarks=request.POST['remarks'],
            total_balance=total_balance,
            unit_price=unit_price,
            total_cost=total_cost
        )

        History.objects.create(
            action='Add',
            item_name=item.name,
            category='Kitchen',
            user=request.user
        )
        return redirect('kitchen_list')
    return render(request, 'kitchen/add.html')


@login_required
def kitchen_edit(request, id):
    stock = get_object_or_404(Kitchen, id=id)
    if request.method == 'POST':
        stock.name = request.POST['name']
        stock.balance = int(request.POST['balance'])
        stock.stock_in = int(request.POST['stock_in'])
        stock.stock_out = int(request.POST['stock_out'])
        stock.remarks = request.POST['remarks']
        stock.unit_price = float(request.POST['unit_price'])
        stock.total_balance = stock.balance + stock.stock_in - stock.stock_out
        stock.total_cost = stock.total_balance * stock.unit_price
        stock.save()

        History.objects.create(
            action='Update',
            item_name=stock.name,
            category='Kitchen',
            user=request.user
        )

        return redirect('kitchen_list')
    return render(request, 'kitchen/edit.html', {'stock': stock})

@login_required
def kitchen_delete(request, id):
    stock = get_object_or_404(Kitchen, id=id)
    if request.method == 'POST':
        History.objects.create(
            action='Delete',
            item_name=stock.name,
            category='Kitchen',
            user=request.user
        )
        stock.delete()
    return redirect('kitchen_list')

    
@login_required
def snack_list(request):
    query = request.GET.get('q')
    if query:
        snack_stocks = Snack.objects.filter(
            Q(name__icontains=query) | Q(remarks__icontains=query)
        )
    else:
        snack_stocks = Snack.objects.all()
    return render(request, 'snacks/index.html', {'snack_stocks': snack_stocks, 'query': query})

@login_required
def snack_add(request):
    if request.method == 'POST':
        balance = int(request.POST['balance'])
        stock_in = int(request.POST.get('stock_in', 0))
        stock_out = int(request.POST.get('stock_out', 0))
        unit_price = float(request.POST['unit_price'])
        total = balance + stock_in - stock_out
        total_cost = total * unit_price

        item = Snack.objects.create(
            name=request.POST['name'],
            balance=balance,
            stock_in=stock_in,
            stock_out=stock_out,
            remarks=request.POST.get('remarks', ''),
            total_balance=total,
            unit_price=unit_price,
            total_cost=total_cost
        )

        History.objects.create(
            action='Add',
            item_name=item.name,
            category='Snack',
            user=request.user
        )

        return redirect('snack_list')

    return render(request, 'snacks/add.html')

@login_required
def snack_edit(request, id):
    stock = get_object_or_404(Snack, id=id)
    if request.method == 'POST':
        stock.name = request.POST['name']
        stock.balance = int(request.POST['balance'])
        stock.stock_in = int(request.POST['stock_in'])
        stock.stock_out = int(request.POST['stock_out'])
        stock.remarks = request.POST.get('remarks', '')
        stock.unit_price = float(request.POST['unit_price'])
        stock.total_balance = stock.balance + stock.stock_in - stock.stock_out
        stock.total_cost = stock.total_balance * stock.unit_price
        stock.save()

        History.objects.create(
            action='Update',
            item_name=stock.name,
            category='Snack',
            user=request.user
        )

        return redirect('snack_list')
    return render(request, 'snacks/edit.html', {'stock': stock})

@login_required
def snack_delete(request, id):
    stock = get_object_or_404(Snack, id=id)
    if request.method == 'POST':
        History.objects.create(
            action='Delete',
            item_name=stock.name,
            category='Snack',
            user=request.user
        )
        stock.delete()
    return redirect('snack_list')

@login_required
def history_list(request):
    history = History.objects.all().order_by('-timestamp')
    return render(request, 'history/index.html', {'history_list': history})


@login_required
def delete_all_history(request):
    if request.method == 'POST':
        History.objects.all().delete()
        messages.success(request, "All history records deleted successfully.")
    return redirect('history_list')

@login_required
def dashboard(request):
    groceries = Grocery.objects.all()
    kitchens = Kitchen.objects.all()
    snacks = Snack.objects.all()

    context = {
        'groceries': groceries,
        'kitchens': kitchens,
        'snacks': snacks,
    }
    return render(request, 'dashboard.html', context)



def export_history_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="inventory_history.csv"'

    writer = csv.writer(response)
    writer.writerow(['Date','Time', 'Action', 'Item', 'Category', 'User'])

    history_entries = History.objects.all().order_by('-timestamp')

    for entry in history_entries:
        writer.writerow([
            entry.timestamp.strftime('%Y-%m-%d'),  # Date
            entry.timestamp.strftime('%H:%M'),  # Time
            entry.action,
            entry.item_name,
            entry.category,
            str(entry.user)
        ])

    return response


def export_grocery_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="grocery_inventory.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Balance', 'In', 'Out', 'Remarks', 'Unit Price', 'Total Balance', 'Total Cost'])

    groceries = Grocery.objects.all()

    query = request.GET.get('q')
    if query:
        groceries = groceries.filter(name__icontains=query)

    for item in groceries:
        writer.writerow([
            item.name,
            item.balance,
            item.stock_in,
            item.stock_out,
            item.remarks,
            f"{item.unit_price:.2f}",
            item.total_balance,
            f"{item.total_cost:.2f}",
        ])

    return response

def export_kitchen_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="kitchen_stocks.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Balance', 'In', 'Out', 'Total Balance', 'Unit Price', 'Total Cost', 'Remarks'])

    kitchen_items = Kitchen.objects.all()

    query = request.GET.get('q')
    if query:
        kitchen_items = kitchen_items.filter(name__icontains=query)

    for item in kitchen_items:
        writer.writerow([
            item.name,
            item.balance,
            item.stock_in,
            item.stock_out,
            item.total_balance,
            f"{item.unit_price:.2f}",
            f"{item.total_cost:.2f}",
            item.remarks,
        ])

    return response


def export_snack_csv(request):
    query = request.GET.get('q')
    snacks = Snack.objects.all()

    if query:
        snacks = snacks.filter(Q(name__icontains=query) | Q(remarks__icontains=query))

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="snack_inventory.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Balance', 'In', 'Out', 'Unit Price', 'Total Balance', 'Total Cost'])

    for item in snacks:
        writer.writerow([
            item.name,
            item.balance,
            item.stock_in,
            item.stock_out,
            f'{item.unit_price:.2f}',
            item.total_balance,
            f'{item.total_cost:.2f}'
        ])

    return response