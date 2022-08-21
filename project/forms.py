from tkinter import Widget
from django import forms
from project.models import Project


class DateInputDeadline(forms.DateInput):
    input_type = 'date'


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do projeto',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Descrição rápida do projeto',
                
            }),
            'manager': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Gerente do projeto'
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
             })
        }
