from django.db import models

# Create your models here.


class Personal (models.Model):
    
    cedula = models.IntegerField()