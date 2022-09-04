from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login/', views.loginView, name='loginView'),
    path('cadastro/', views.register, name='register'),
    path('logout/', views.logoutView, name='logoutView'),
    path('usuario/', login_required(views.userData, login_url='loginView'), name='userData'),
    path('deletar-user/', login_required(views.removeUser, login_url='loginView'), name='removeUser'),
    path('upload-image-user/', login_required(views.imageUserSave, login_url='loginView'), name='imageUserSave'),
    path('update-image-user/<int:pk>', login_required(views.updateImageUser, login_url='loginView'), name='updateImageUser'),
    path('delete-image-user/<int:pk>', login_required(views.deleteImageUser, login_url='loginView'), name='deleteImageUser'),
   
]

