from django.urls import path

from ordersapp import views

app_name = 'ordersapp'


urlpatterns = [
    path('', views.OrderList.as_view(), name='orders_list'),
    path('read/<pk>/', views.OrderItemsRead.as_view(), name='order_read'),
    path('update/<pk>/', views.OrderItemUpdate.as_view(), name='order_update'),
    path('delete/<pk>/', views.OrderItemsDelete.as_view(), name='order_delete'),
    path('create/', views.OrderItemCreate.as_view(), name='order_create'),
]
