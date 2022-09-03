from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.loginView, name='loginView'),
    path('cadastro/', views.register, name='register'),
    path('logout/', views.logoutView, name='logoutView'),
    path('usuario/', login_required(views.userData, login_url='loginView'), name='userData'),
    path('deletar-user/', login_required(views.removeUser, login_url='loginView'), name='removeUser'),
    path('upload-image-user/', login_required(views.imageUser, login_url='loginView'), name='imageUser'),
]

