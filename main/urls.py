from django.urls import path
from .views import mainTeste

urlpatterns = [
    path('', mainTeste, name='home'),
    path('criar', mainTeste, name='create'),
]