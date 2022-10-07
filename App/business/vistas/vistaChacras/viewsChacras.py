
from django.shortcuts import render
from ps.conexion import *
from ps.permissions import *

##LOGIN
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import logout

### ZONA CHACRAS

@login_required
def chacras(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['chacras'] == 1:
        permissions = 1
        area_permisos = p_chacras(usr_permisos['id'])
        variable = "chacras"
        return render(request,'business/chacras/chacras.html', {'business': variable, 'chacras': variable, 'permiso': permissions, 'permisos': area_permisos})
    else:
        permissions = 0
        variable = "chacras"
        return render(request,'business/chacras/chacras.html', {'business': variable, 'chacras': variable, 'permiso': permissions})
 