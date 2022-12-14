from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from project.models import Project
from .forms import ServiceForm
from .models import Service
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def list(request, pkProject, page=1):

    data = {}
    data['project'] = get_object_or_404(Project, pk=pkProject, user=request.user)
   
    services = Service.objects.filter(project=data['project'].pk)
    
    if request.GET.get('search'):
        services = Service.objects.filter(name__contains=request.GET.get('search'), project=data['project'].pk)

    paginator = Paginator(services, 10)
    data['services'] = paginator.get_page(page)

    return render(request, 'service/services.html', data)


def save(request, pkProject):

    form = ServiceForm(request.POST or None) 
   
    if form.is_valid():
        project = Project.objects.get(pk=pkProject, user=request.user)

        if project.budget is None:
            messages.error(request, "É necessário definir um orçamento para o projeto para salvar um serviço.")
            return redirect(reverse('viewProject', args=[pkProject]))
  
        service = form.save(commit=False)
        service.project = project
   
        services = Service.objects.filter(project=pkProject)
        spentBudget = service.price or 0

        for servicBudget in services:
            spentBudget += servicBudget.price
        
        if spentBudget>project.budget:
            messages.error(request, "O preço do serviço '"+service.name+"' excede o orçamento do projeto.")
            return redirect(reverse('viewProject', args=[pkProject]))
  
        try:
             service.save()
             messages.success(request, "Serviço '"+service.name+"' salvo!")
        except:
             messages.error(request, "Erro ao salvar o serviço '"+service.name+"'!")
        
        return redirect(reverse('viewProject', args=[pkProject]))

    else:
        print('error saving')
        return redirect('projects')

def edit(request, pkProject, pk):

    project = get_object_or_404(Project, pk=pkProject, user=request.user)
    service = Service.objects.get(pk=pk, project=project)
    form = ServiceForm(request.POST or None, instance=service)

    if form.is_valid():
        try:
           serviceUpdate = form.save(commit=False)
           serviceUpdate.project = project

           services = Service.objects.filter(project=project)
           spentBudget = serviceUpdate.price or 0

           for serviceBudget in services:
                spentBudget += serviceBudget.price

           if spentBudget > serviceUpdate.project.budget:
                messages.error(request, "O preço do serviço '"+service.name+"' excede o orçamento do projeto.")
                return redirect(reverse('viewProject', args=[pkProject]))

           serviceUpdate.save()
           messages.success(request, "Serviço '"+service.name+"' editado!")

        except NameError:
            print("================")
            print(NameError)
            print("================")
            messages.error(request, "Erro ao editar serviço!")
        

    return redirect(reverse('viewProject', args=[pkProject]))

def delete(request, pkProject, pk):
    project = get_object_or_404(Project, pk=pkProject, user=request.user)
    service = Service.objects.get(pk=pk, project=project)

    try:
        service.delete()
        messages.success(request, "Serviço '"+service.name+"' deletado!")
    except:
        messages.error(request, "Erro ao deletar serviço!")

    return redirect(reverse('viewProject', args=[pkProject]))


