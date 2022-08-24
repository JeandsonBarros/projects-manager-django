from django.urls import path
from .views import save, delete, edit, list
""" search """
urlpatterns = [
    path('salvar/<int:pkProject>/', save, name='saveService'),
    path('delete/<int:pkProject>/<int:pk>/', delete, name='deleteService'),
    path('editar/<int:pkProject>/<int:pk>/', edit, name='editService'),
    #path('search/<int:pkProject>/', search, name='searchService'),
    path('list/<int:pkProject>/<int:page>', list, name='listServices'),
]