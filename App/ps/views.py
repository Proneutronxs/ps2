from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import *
from urllib import request
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    variable = "Inicio"
    return render(request,'ps/index.html', {'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def project(request):
    proyectos = projects.objects.all()
    variable = "Proyecto"
    return render(request,'ps/project.html', {'proyectoshtml':proyectos,'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def detail(request, id):
    id = projects.objects.filter(id=id)
    variable = "Proyecto"
    return render(request,'ps/detail.html', {'id': id, 'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def consumoApi(request):
    variable = "consumoApi"
    return render(request,'ps/consumoApi.html', {'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def about1(request):
    about1 = about.objects.all()
    variable = "about"
    return render(request,'ps/about.html', {'abouthtml':about1,'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def contact(request):
    variable = "contacto"
    return render(request,'ps/contact.html', {'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})
