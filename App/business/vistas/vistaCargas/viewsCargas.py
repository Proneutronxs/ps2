udio
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from ps.conexion import *
from ps.permissions import *

##LOGIN
from django.contrib.auth.decorators import login_required

### ZONA CARGAS

@login_required
def cargas(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['cargas'] == 1:
        permissions = 1
        area_permisos = p_cargas(usr_permisos['id'])
        variable = "cargas"
        return render(request,'business/cargas/cargas.html', {'business': variable, 'cargas': variable, 'permiso': permissions, 'permisos': area_permisos})
    else:
        permissions = 0
        variable = "cargas"
        return render(request,'business/cargas/cargas.html', {'business': variable, 'cargas': variable, 'permiso': permissions})
