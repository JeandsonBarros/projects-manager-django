from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image


# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }))

    username = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))

    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }))
     
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class ImageForm(forms.ModelForm):
    """Form for the image model"""

    image = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={
            'class': 'form-control'
        }))

    class Meta:
        model = Image
        fields = ('image',)