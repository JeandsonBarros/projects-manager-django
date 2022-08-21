from django.db import models

# Create your models here.
class Project(models.Model):
    
    name = models.CharField(max_length=200)
    manager = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    deadline = models.DateField()
    status = models.CharField(max_length=200)
    budget = models.IntegerField(null=True, blank=True)
