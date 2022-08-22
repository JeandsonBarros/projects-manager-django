from django.urls import path
from .views import save, delete

urlpatterns = [
    path('save/<int:pkProject>/', save, name='saveService'),
    path('delete/<int:pkProject>/<int:pk>/', delete, name='deleteService'),
]