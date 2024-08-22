from django.db import models

# Create your models here.


class Personal (models.Model):
    
    Cedula = models.IntegerField(max_length=8, primary_key=True)
    Apellidos= models.CharField(max_length=40)
    Nombres = models.CharField(max_length=40)
    EdoCiviles= [
        ('S', 'Soltero(a)'),
        ('C', 'Casado(a)'),
        ('D', 'Divorcidado(a)'),
        ('V', 'Viudo(a)' ),
        ('O', 'Otro')

    ]
    EdoCivil = models.CharField(max_length=1, choices=EdoCiviles, default= "S")


