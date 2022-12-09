from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),  #home page
    path('completeOrder/', views.completeOrder, name='completeOrder'),   #orderForm
    path('completeOrder/confirmation/', views.confirmation, name='confirmation')
 ]