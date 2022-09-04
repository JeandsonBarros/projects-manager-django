
from .models import Service
from django import forms


class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ['name', 'price', 'description' ]
        widgets = {
            
            'name': forms.TextInput(attrs={
                'spellcheck': 'true',
                'class': 'form-control',
                'placeholder': 'Nome do serviço',
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '2000,30',
            }),
            'description': forms.Textarea(attrs={
                'spellcheck': 'true',
                'class': 'form-control',
                'placeholder': 'Descrição do serviço',
            })
        }
        

