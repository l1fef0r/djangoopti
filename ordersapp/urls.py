from django.urls import path

import ordersapp.views
from ordersapp import views

app_name = 'ordersapp'


urlpatterns = [
    path('', views.OrderList.as_view(), name='orders_list'),
    path('read/<pk>/', views.OrderItemsRead.as_view(), name='order_read'),
    path('update/<pk>/', views.OrderItemUpdate.as_view(), name='order_update'),
    path('delete/<pk>/', views.OrderItemsDelete.as_view(), name='order_delete'),
    path('create/', views.OrderItemCreate.as_view(), name='order_create'),
    path('forming/complete/<pk>/', views.order_forming_complete, name='order_forming_complete'),
    path('product/<pk>/price/', ordersapp.views.product_price),
]
