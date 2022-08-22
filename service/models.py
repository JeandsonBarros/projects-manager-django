from django.db import models
from project.models import Project

# Create your models here.
class Service(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
