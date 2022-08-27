from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','price']
    list_filter = ['name',]
    search_fields = ['name']

admin.site.register(Service, ServiceAdmin)