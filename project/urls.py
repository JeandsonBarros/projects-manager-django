from django.urls import path
from project.views import index, saveProject, viewProject, editProject, delete

urlpatterns = [
    path('', index, name='projects'),
    path('<int:page>/', index, name='projects'),
    path('criar/', saveProject, name='createProject'),
    path('projeto/<int:pk>/', viewProject, name='viewProject'),
    path('editar/<int:pk>/', editProject, name='editProject'),
    path('delete/<int:pk>/', delete, name='deleteProject'),

]