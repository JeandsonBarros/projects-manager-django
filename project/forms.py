from tkinter import Widget
from django import forms
from project.models import Project

STATUS_CHOICES = [
    ('Em planejamento', 'Em planejamento'),
    ('Em desenvolvimento', 'Em desenvolvimento'),
    ('Concluído', 'Concluído'),
    ('Cancelado', 'Cancelado'),
]

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
                'spellcheck': 'true'        
            }),
            'manager': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Gerente do projeto'
            }),
            'status': forms.Select(choices=STATUS_CHOICES, attrs={
                'class': 'form-control',
                'placeholder': 'Status do projeto',          
            }),
            'budget': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Exemplo: 23000,95',  
                'step': 0.01    
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',            
             })
        }

