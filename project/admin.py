from django.contrib import admin
from .models import Project

# Register your models here.

@admin.action(description="Complete projects")
def completeProjects(modeladmin, request, queryset):
    queryset.update(status="Concluído")

@admin.action(description="Cancel projects")
def cancelProjects(modeladmin, request, queryset):
    queryset.update(status="Cancelado")

class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'manager',
        'deadline', 
        'budget',
        'status' ]

    list_filter = [
        'deadline',
         'status']

    search_fields = ['name']

    actions = [
        completeProjects, 
        cancelProjects ]

admin.site.register(Project, ProjectAdmin)