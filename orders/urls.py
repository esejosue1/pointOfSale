from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.orders, name='orders'),  #home page
    path('completeOrder/<str:cart_subtotal>/<str:cart_tax>/<str:cart_shipping>/<str:cart_total>/', views.completeOrder, name='completeOrder')   #orderForm
 ]