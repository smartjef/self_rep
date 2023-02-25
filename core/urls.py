from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/register/', views.register_advocate, name='register'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]