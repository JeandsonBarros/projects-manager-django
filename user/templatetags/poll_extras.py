from django import template
from user.models import Image
from django.shortcuts import render, redirect, get_object_or_404

register = template.Library()

#https://www.pluralsight.com/guides/create-custom-template-tags-and-filters-in-django
@register.filter(name='image_user_url')
def getImageUserUrl(user):

   if Image.objects.filter(user=user).exists():
      imageUser = Image.objects.filter(user=user)
      return imageUser[0].image.url
   else: 
     return False
    