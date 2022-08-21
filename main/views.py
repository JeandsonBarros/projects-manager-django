from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, reverse
from django.http import HttpResponse

# Create your views here.

def mainTeste(request):
    #return HttpResponse("<h1> Teste do main </h1>")
    return render(request, 'main/index.html')