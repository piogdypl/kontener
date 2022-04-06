from django.urls import path
from . import views
from django.urls import path
from .views import (#order_list,
                order_detail, create_order, update_order, OrderListView, OrderDelete)

app_name = 'order'
urlpatterns = [
    path('', OrderListView.as_view(), name = 'order_list'),
    # path('', order_list, name='order_list'),
    path('create', create_order, name = 'create_order'),
    path('<str:get_booking>', order_detail, name = 'order_detail'),
    path('<str:get_booking>/update_order', update_order, name = 'update_order'),
    # path('<str:get_booking>/order_delete', order_delete, name = 'order_delete'),
    path('delete/<str:get_booking>/', OrderDelete.as_view(), name = 'order_delete')



]