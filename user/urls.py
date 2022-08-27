from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name='loginView'),
    path('cadastro/', views.register, name='register'),
    path('logout/', views.logoutView, name='logoutView'),
]