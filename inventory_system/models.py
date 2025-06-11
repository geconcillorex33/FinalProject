from django.db import models
from django.contrib.auth.models import User
from datetime import date

class History(models.Model):
    action = models.CharField(max_length=10)  # Add, Update, Delete
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # Grocery, Kitchen, Snack
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'history'

class Grocery(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField()
    stock_in = models.IntegerField()
    stock_out = models.IntegerField()
    remarks = models.TextField()
    total_balance = models.IntegerField()
    date_added = models.DateField(default=date.today)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = 'grocery'

class Kitchen(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField()
    stock_in = models.IntegerField()
    stock_out = models.IntegerField()
    remarks = models.TextField()
    total_balance = models.IntegerField()
    date_added = models.DateField(default=date.today)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = 'kitchen_stock'

class Snack(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField()
    stock_in = models.IntegerField()
    stock_out = models.IntegerField()
    total_balance = models.IntegerField()
    date_added = models.DateField(default=date.today)
    remarks = models.TextField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    class Meta:
        db_table = 'snack_station'
