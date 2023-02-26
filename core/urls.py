from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register/', views.AdvocateSignUpView.as_view(), name='register'),
    path('signup/', views.NormalSignUpView.as_view(), name='sign_up'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]