from django.db import models

# Create your models here.
class about(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()


class projects(models.Model):
    nombre = models.CharField(max_length=255)
    descripción = models.TextField()
    imagen = models.TextField()

class send(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField()
    mensaje = models.CharField(max_length=255)