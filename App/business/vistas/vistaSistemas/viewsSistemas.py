
from django.shortcuts import render
from datetime import datetime
from ps.conexion import *
from ps.permissions import *
from django.template.loader import get_template

##LOGIN
from django.contrib.auth.decorators import login_required


### ZONA SISTEMAS

@login_required
def sistemas(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['sistemas'] == 1:
        permissions = 1
        area_permisos = p_sistemas(usr_permisos['id'])
        variable = "sistemas"
        return render(request,'business/sistemas/sistemas.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'permisos': area_permisos})
    else:
        permissions = 0
        variable = "sistemas"
        return render(request,'business/sistemas/sistemas.html', {'business': variable, 'sistemas': variable, 'permiso': permissions})