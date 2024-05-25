from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('pet/', views.pet, name='pet'),
    path('book/', views.book, name='book'),
    path('create-booking/', views.create_booking, name='create_booking'),
]
