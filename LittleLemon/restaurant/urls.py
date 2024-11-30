#define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # This handles the base path of /restaurant/menu
    path('menu/', views.MenuItemsView.as_view(), name='menu_list'),  # List menu items
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu_item_detail'),  # View/edit a single menu item
    path('menu/items/', views.MenuItemsView.as_view(), name='menu_items'),  # This path will handle /restaurant/menu/items
]