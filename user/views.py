from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.
def loginView(request):
    if request.user.is_authenticated:
        return redirect('projects')
    
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('projects')
            
        else:
            messages.error(request, 'Erro ao logar, verifique seu e-mail e senha!')
            return redirect('loginView')
    else:        
        return render(request, 'user/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('projects')  
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("projects")
        else:
            messages.error(request, "Registro sem sucesso. Informações inválidas.")
            return redirect("register")
    else:        
        return render(request, 'user/register.html', {'form': NewUserForm()})

def logoutView(request):
    logout(request)
    return redirect('home')

def userData(request):
    data = {}
    data['form'] = NewUserForm(instance=request.user)

    if request.method == "POST":
        form = NewUserForm(request.POST or None, instance=request.user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Alteração de dados feita com sucesso.")
            return redirect("userData")
        else:
            messages.error(request, "Alteração de dados sem sucesso. Informações inválidas.")
            return redirect("userData")

    return render(request, 'user/user_data.html', data)

def removeUser(request):

    try:
        request.user.delete()
    except NameError:
        messages.error(request, "Error:" + NameError)

    return redirect("loginView")