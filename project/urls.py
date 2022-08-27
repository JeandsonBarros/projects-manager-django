from django.urls import path
from project.views import index, saveProject, viewProject, editProject, delete
from django.contrib.auth.decorators import login_required

urlpatterns = [
    
    path('', login_required(index, login_url='loginView') , name='projects'),
    path('<int:page>/', login_required(index, login_url='loginView'), name='projects'),
    path('criar/', login_required(saveProject, login_url='loginView'), name='createProject'),
    path('projeto/<int:pk>/', login_required(viewProject, login_url='loginView'), name='viewProject'),
    path('editar/<int:pk>/', login_required(editProject, login_url='loginView'), name='editProject'),
    path('delete/<int:pk>/', login_required(delete, login_url='loginView'), name='deleteProject'),

]