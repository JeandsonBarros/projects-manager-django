from django.shortcuts import render

# Create your views here.
def login(request):
    print('aqui')
    return render(request, 'user/login.html')


