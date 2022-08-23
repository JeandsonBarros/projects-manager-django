from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from project.models import Project
from .forms import ServiceForm
from .models import Service
from django.contrib import messages

# Create your views here.

def save(request, pkProject):
    form = ServiceForm(request.POST or None) 
   
    if form.is_valid():
        service = form.save(commit=False)
        project = Project.objects.get(pk=pkProject)
        service.project = project
   
        services = Service.objects.filter(project=pkProject)
        spentBudget = service.price or 0

        for servicBudget in services:
            spentBudget += servicBudget.price
        
        if(spentBudget>project.budget):
            messages.error(request, "O preço do serviço '"+service.name+"' excede o orçamento do projeto.")
            return redirect(reverse('viewProject', args=[pkProject]))
  
        try:
             service.save()
             messages.success(request, "Serviço salvo!")
        except:
             messages.error(request, "Erro ao salvar serviço!")
        
        return redirect(reverse('viewProject', args=[pkProject]))
    else:
        print('error saving')
        return redirect('projects')


def edit(request, pkProject, pk):

    service = Service.objects.get(pk=pk)

    form = ServiceForm(request.POST or None, instance=service)
    if form.is_valid():
        try:
            form.save()
        except:
            print("================")
            print("|---- Erro ----|")
            print("================")
        

    return redirect(reverse('viewProject', args=[pkProject]))

def delete(request, pkProject, pk):
    service = get_object_or_404(Service, pk=pk)

    try:
        service.delete()
        messages.success(request, "Serviço deletado!")
    except:
        messages.error(request, "Erro ao deletar serviço!")

    return redirect(reverse('viewProject', args=[pkProject]))


