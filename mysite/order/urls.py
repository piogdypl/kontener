from django.urls import path
from .views import (
                order_detail, create_order, update_order, OrderDelete, OrderListView, OrderDashBoard)

app_name = 'order'
urlpatterns = [
    path('dashboard', OrderListView.as_view(), name = 'order_list'),
    path('', OrderDashBoard.as_view(), name = 'dashboard'),
    path('create', create_order, name = 'create_order'),
    path('<str:get_booking>', order_detail, name = 'order_detail'),
    path('<str:get_booking>/update_order', update_order, name = 'update_order'),
    path('delete/<str:get_booking>/', OrderDelete.as_view(), name = 'order_delete'),




]