from django.shortcuts import render, redirect, reverse
from project.forms import ProjectForm
from project.models import Project
from django.http import HttpResponse
from django.contrib import messages
from service.forms import ServiceForm
from service.models import Service

def index(request):
    data = {}
    data['projects'] = Project.objects.all()

    if request.GET.get('search'):
        data['projects'] = Project.objects.filter(name__contains=request.GET.get('search'))

    return render(request, 'project/index.html', data)


def saveProject(request):
    if request.method == 'GET':
        data = {}
        data['form'] = ProjectForm()
        return render(request, 'project/form_project.html', data)

    elif request.method == 'POST':
        form = ProjectForm(request.POST or None)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Projeto salvo!")
                return redirect('projects')

            except NameError: 
                print(NameError)
                messages.error(request, "Erro ao salvar o projeto!")
                return redirect('projects')
            
            
def viewProject(request, pk):
    data = {}
    data['project'] = Project.objects.get(pk=pk)
    data['services'] = Service.objects.filter(project=pk)

    spentBudget = 0

    for servicBudget in data['services']:
        spentBudget += servicBudget.price
   
    data['serviceForm'] = ServiceForm()
    data['spentBudget'] = spentBudget

    return render(request, 'project/view_project.html', data)


def editProject(request, pk):  
    data = {}
    data['project'] = Project.objects.get(pk=pk)

    if request.method == 'GET':
        data['form'] = ProjectForm(instance=data['project'])
        return render(request, 'project/form_project.html', data)

    elif request.method == 'POST':
        form = ProjectForm(request.POST or None, instance=data['project'])

        if form.is_valid():
            try:
                form.save()
            except NameError:
                print(NameError)

            data['project'] = Project.objects.get(pk=pk)            
            data['form'] = ProjectForm(instance=data['project'])

            return render(request, 'project/form_project.html', data)


def delete(request, pk):
    project = Project.objects.get(pk=pk)
    project.delete()
    messages.success(request, f"Projeto {project.name} deletado!")
    return redirect('projects')

