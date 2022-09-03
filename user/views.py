from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm, ImageForm
from .models import Image

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
        data = {}
        data['from'] = NewUserForm()
        return render(request, 'user/form_user.html', data)

def logoutView(request):
    logout(request)
    return redirect('home')

#https://djangocentral.com/uploading-images-with-django/
def imageUser(request):
    form = ImageForm(request.POST or None, request.FILES)

    """  imageGet = Image.objects.get(pk=4)
    if imageGet:
        form = ImageForm(request.POST or None, request.FILES, instance=imageGet)
        image = form.save(commit=False)
        image.user = request.user
        image.save()
        print(form.instance.image.url)
        messages.success(request, "Imagem salva.")
        return redirect("userData") """

    if form.is_valid():
        image = form.save(commit=False)
        image.user = request.user
        image.save()
        print(form.instance.image.url)
        messages.success(request, "Imagem salva.")
    else:
        messages.error(request, "Erro ao salvar imagem.")

    return redirect("userData")

def userData(request):
    data = {}
    data['form'] = NewUserForm(instance=request.user)
    data['imageForm'] = ImageForm()
    data['imageUser'] = Image.objects.filter(user=request.user)

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

    return render(request, 'user/form_user.html', data)

def removeUser(request):

    try:
        request.user.delete()
    except NameError:
        messages.error(request, "Error:" + NameError)

    return redirect("loginView")