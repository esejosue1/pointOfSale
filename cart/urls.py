from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'cart'

urlpatterns = [
    path('cart/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('increment/<int:product_id>/', views.cart_increment, name='cart_increment'),
    path('decrement/<int:product_id>/', views.cart_decrement, name='cart_decrement'),
    path('add_decrement/<int:product_id>/', views.cart_add_decrement, name='cart_add_decrement'),
    path('add_increment/<int:product_id>/', views.cart_add_increment, name='cart_add_increment'),
    path('add_quantity/<int:product_id>/', views.cart_add_quantity, name='cart_add_quantity'),
    path('orders/', views.cart_to_orders, name='cart_to_orders'),
    path('', views.cart_detail, name='index'),
]