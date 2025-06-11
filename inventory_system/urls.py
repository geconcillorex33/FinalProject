from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='home'),

    path('history/export/', views.export_history_csv, name='export_history_csv'),
    path('grocery/export/', views.export_grocery_excel, name='export_grocery_excel'),
    path('kitchen/export/', views.export_kitchen_excel, name='export_kitchen_excel'),
    path('snack/export/', views.export_snack_excel, name='export_snack_excel'),

    path('groceries/', views.grocery_list, name='grocery_list'),
    path('groceries/add/', views.grocery_add, name='grocery_add'),
    path('groceries/delete/<int:id>/', views.grocery_delete, name='grocery_delete'),
    path('stock_in/<int:id>/', views.stock_in, name='stock_in'),
    path('stock_out/<int:id>/', views.stock_out, name='stock_out'),
    path('grocery/monthly-summary/', views.grocery_monthly_summary, name='grocery_monthly_summary'),



    path('kitchen/', views.kitchen_list, name='kitchen_list'),
    path('kitchen/add/', views.kitchen_add, name='kitchen_add'),
    path('kitchen/delete/<int:id>/', views.kitchen_delete, name='kitchen_delete'),
    path('kitchen/stock_in/<int:id>/', views.kitchen_stock_in, name='kitchen_stock_in'),
    path('kitchen/stock_out/<int:id>/', views.kitchen_stock_out, name='kitchen_stock_out'),
    path('kitchen/monthly-summary/', views.kitchen_monthly_summary, name='kitchen_monthly_summary'),

    path('snacks/', views.snack_list, name='snack_list'),
    path('snacks/add/', views.snack_add, name='snack_add'),
    path('snacks/delete/<int:id>/', views.snack_delete, name='snack_delete'),
    path('snacks/stock_in/<int:id>/', views.snack_stock_in, name='snack_stock_in'),  # <-- fixed here
    path('snacks/stock_out/<int:id>/', views.snack_stock_out, name='snack_stock_out'),
    path('snack/monthly-summary/', views.snack_monthly_summary, name='snack_monthly_summary'),


    path('history/', views.history_list, name='history_list'),
    path('history/delete_all/', views.delete_all_history, name='delete_all_history'),
]
