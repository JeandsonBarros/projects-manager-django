from django.shortcuts import render, redirect, reverse, get_object_or_404
from project.forms import ProjectForm
from project.models import Project
from django.http import HttpResponse
from django.contrib import messages
from service.forms import ServiceForm
from service.models import Service
from django.core.paginator import Paginator

def listProjects(request, page=1):
    data = {}
    projects = Project.objects.filter(user=request.user)

    if request.GET.get('search'):
        projects = Project.objects.filter(name__contains=request.GET.get('search'), user=request.user)
   
    paginator = Paginator(projects, 10) # Show 10 contacts per page.
   
    data['projects'] = paginator.get_page(page)

    return render(request, 'project/list_projects.html', data)


def saveProject(request):
    if request.method == 'GET':
        data = {}
        data['form'] = ProjectForm()
        return render(request, 'project/form_project.html', data)

    elif request.method == 'POST':
        form = ProjectForm(request.POST or None)

        if form.is_valid():
            try:
                project = form.save(commit=False)
                project.user = request.user
                project.save()
                messages.success(request, "Projeto salvo!")
                return redirect('projects')

            except NameError: 
                print(NameError)
                messages.error(request, "Erro ao salvar o projeto!")
                return redirect('projects')
        else:
            messages.error(request, "Erro ao salvar o projeto, dados invalidos!")
            return redirect('projects')

            
def viewProject(request, pk):
    data = {}
    #data['project'] = Project.objects.get(pk=pk, user=request.user)
    data['project'] = get_object_or_404(Project, pk=pk, user=request.user)
    services = Service.objects.filter(project=pk)
    
    paginator = Paginator(services, 10)
    data['services'] = paginator.get_page(1)

    spentBudget = 0

    for servicBudget in data['services']:
        spentBudget += servicBudget.price
   
    data['serviceForm'] = ServiceForm()
    data['spentBudget'] = spentBudget

    return render(request, 'project/view_project.html', data)


def editProject(request, pk):  
    data = {}
    data['project'] = get_object_or_404(Project, pk=pk, user=request.user)
    data['form'] = ProjectForm(instance=data['project'])
    
    if request.method == 'POST':
        form = ProjectForm(request.POST or None, instance=data['project'])

        if form.is_valid():
            try:
                data['project'] = form.save()
            except NameError:
                print(NameError)
         
            data['form'] = ProjectForm(instance=data['project'])

            return render(request, 'project/form_project.html', data)
        else:
            return render(request, 'project/form_project.html', data)

    return render(request, 'project/form_project.html', data)


def delete(request, pk):
    project = Project.objects.get(pk=pk, user=request.user)

    try:
        project.delete()
        messages.success(request, f"Projeto {project.name} deletado!")
    except NameError:
        messages.error(request, f"Erro ao deletar o projeto '{project.name}'!")

    return redirect('projects')

