from contextlib import redirect_stderr
from email.mime import audio
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
from ps.conexion import *
from ps.permissions import *

##LOGIN
from django.contrib.auth.decorators import login_required

### ZONA ADMINISTRACIÓN
@login_required
def administracion(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['admin'] == 1:
        permissions = 1
        area_permisos = p_admin(usr_permisos['id'])
        variable = "administracion"
        return render(request,'business/administracion/administracion.html', {'business': variable, 'administracion': variable, 'permiso': permissions, 'permisos': area_permisos})
    else:
        permissions = 0
        variable = "administracion"
        return render(request,'business/administracion/administracion.html', {'business': variable, 'administracion': variable, 'permiso': permissions})
