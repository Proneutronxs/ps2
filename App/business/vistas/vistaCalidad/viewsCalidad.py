from contextlib import redirect_stderr
from email.mime import audio
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
from ps.conexion import *
from ps.permissions import *
from xhtml2pdf import pisa
from django.template.loader import get_template

##LOGIN
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import logout


###ZONA CALIDAD

@login_required
def calidad(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['calidad'] == 1:
        permissions = 1
        area_permisos = p_calidad(usr_permisos['id'])
        variable = "calidad"
        return render(request,'business/calidad/calidad.html', {'business': variable, 'calidad': variable, 'permiso': permissions, 'permisos': area_permisos})
    else:
        permissions = 0
        variable = "calidad"
        return render(request,'business/calidad/calidad.html', {'business': variable, 'calidad': variable, 'permiso': permissions})