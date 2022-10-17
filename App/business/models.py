from django.db import models

# Create your models here.

class models_accion_periodo(models.Model):

    desde = models.DateField()
    empresa = models.CharField(max_length=25)
    accion = models.CharField(max_length=25)
