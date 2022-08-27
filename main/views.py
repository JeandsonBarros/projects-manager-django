from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='loginView')
def mainTeste(request):
    if request.user.is_authenticated:
        return redirect('projects')

    return render(request, 'main/index.html')