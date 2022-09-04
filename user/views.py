from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm, ImageForm
from .models import Image
import os
from django.conf import settings

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
        data['form'] = NewUserForm()
        return render(request, 'user/form_user.html', data)

def logoutView(request):
    logout(request)
    return redirect('home')

def userData(request):
    data = {}
    data['form'] = NewUserForm(instance=request.user)
    data['imageForm'] = ImageForm()

    if Image.objects.filter(user=request.user).exists():
        data['imageUser'] = Image.objects.filter(user=request.user)[0]
    
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


""" ------ Start views image user --------- """

#https://djangocentral.com/uploading-images-with-django/
def imageUserSave(request):
    form = ImageForm(request.POST or None, request.FILES)

    if form.is_valid():
        image = form.save(commit=False)
        image.user = request.user
        image.save()
        messages.success(request, "Imagem salva.")
    else:
        messages.error(request, "Erro ao salvar imagem.")

    return redirect("userData")

def updateImageUser(request, pk):
    
    imageGet = get_object_or_404(Image, pk=pk, user=request.user)
    form = ImageForm(request.POST, request.FILES, instance=imageGet)

    if form.is_valid():
        image = form.save(commit=False)
        image.user = request.user
        image.save()
        messages.success(request, "Imagem editada.")
        return redirect("userData")
    else:
        messages.error(request, "Erro ao editar imagem.")
        return redirect("userData")

def deleteImageUser(request, pk):
    imageGet = get_object_or_404(Image, pk=pk, user=request.user)

    try:
        os.remove(f'{settings.BASE_DIR}/{imageGet.image.url}')
        imageGet.delete()
        messages.success(request, "Imagem removida.")
    except:
        messages.error(request, "Erro ao remover imagem.")
    
    return redirect("userData")

""" ------ End views image user --------- """