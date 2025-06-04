from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.dashboard, name='home'),
   

    path('history/export/', views.export_history_csv, name='export_history_csv'),
    path('grocery/export/', views.export_grocery_csv, name='export_grocery_csv'),
    path('kitchen/export/', views.export_kitchen_csv, name='export_kitchen_csv'),
    path('snack/export/', views.export_snack_csv, name='export_snack_csv'),

    path('groceries/', views.grocery_list, name='grocery_list'),
    path('groceries/add/', views.grocery_add, name='grocery_add'),
    path('groceries/edit/<int:id>/', views.grocery_edit, name='grocery_edit'),
    path('groceries/delete/<int:id>/', views.grocery_delete, name='grocery_delete'),

    path('kitchen/', views.kitchen_list, name='kitchen_list'),
    path('kitchen/add/', views.kitchen_add, name='kitchen_add'),
    path('kitchen/edit/<int:id>/', views.kitchen_edit, name='kitchen_edit'),
    path('kitchen/delete/<int:id>/', views.kitchen_delete, name='kitchen_delete'),

    path('snacks/', views.snack_list, name='snack_list'),
    path('snacks/add/', views.snack_add, name='snack_add'),
    path('snacks/edit/<int:id>/', views.snack_edit, name='snack_edit'),
    path('snacks/delete/<int:id>/', views.snack_delete, name='snack_delete'),

    path('history/', views.history_list, name='history_list'),
    path('history/delete_all/', views.delete_all_history, name='delete_all_history'),

    # Add routes for kitchen and snack station CRUD
]