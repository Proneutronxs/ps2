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

###RONDÍN

from django.db import models


class Plantas(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    plantas = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Plantas'


class Puntos(models.Model):
    id = models.CharField(db_column='ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    punto = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Puntos'


class Registros(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sereno = models.IntegerField(blank=True, null=True)
    planta = models.IntegerField(blank=True, null=True)
    punto = models.CharField(max_length=255, blank=True, null=True)
    fechayhora = models.DateTimeField(blank=True, null=True)
    fecha = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Registros'


class Serenos(models.Model):
    id = models.IntegerField(blank=True, null=True)
    sereno = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Serenos'