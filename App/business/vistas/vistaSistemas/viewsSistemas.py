
from django.shortcuts import render
from ps.conexion import *
from ps.permissions import *
from App.business.forms import *

from django.contrib.auth.forms import  UserCreationForm

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


### USUARIOS
@login_required
def usuarios(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['sistemas'] == 1:
        permissions = 1
        variable = "sistemas"
        return render(request,'business/sistemas/usuarios/usuarios.html', {'business': variable, 'sistemas': variable, 'permiso': permissions})
    else:
        permissions = 0
        variable = "sistemas"
        return render(request,'business/sistemas/usuarios/usuarios.html', {'business': variable, 'sistemas': variable, 'permiso': permissions})

@login_required
def newuser(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['sistemas'] == 1:
        permissions = 1

        if request.method == 'POST':

            form = UserRegisterForm(request.POST)

            if form.is_valid():

                id =form.cleaned_data['id']
                username =form.cleaned_data['username']
                defecto = 0
                
                variables_primarias = [id,username,defecto,defecto,defecto,defecto,defecto,defecto]
                variables_secundarias = [id]

                

                try:
                    permisos = ps_Permisos()
                    cursor_newuser = permisos.cursor()
                    insert_user = ("INSERT INTO `Usuarios` (`id`, `usr`, `usr_administracion`, `usr_calidad`, `usr_cargas`, `usr_empaque`, `usr_chacras`, `usr_sistemas`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);")
                    insert_admin = ("INSERT INTO `Administracion` (`id`) VALUES (%s)")
                    insert_calidad = ("INSERT INTO `Calidad` (`id`) VALUES (%s)")
                    insert_cargas = ("INSERT INTO `Cargas` (`id`) VALUES (%s)")
                    insert_empaque = ("INSERT INTO `Empaque` (`id`) VALUES (%s)")
                    insert_chacras = ("INSERT INTO `Chacras` (`id`) VALUES (%s)")
                    insert_sistemas = ("INSERT INTO `Sistemas` (`id`) VALUES (%s)")
                    cursor_newuser.execute(insert_user, variables_primarias)
                    cursor_newuser.execute(insert_admin, variables_secundarias)
                    cursor_newuser.execute(insert_calidad, variables_secundarias)
                    cursor_newuser.execute(insert_cargas, variables_secundarias)
                    cursor_newuser.execute(insert_empaque, variables_secundarias)
                    cursor_newuser.execute(insert_chacras, variables_secundarias)
                    cursor_newuser.execute(insert_sistemas, variables_secundarias)
                    permisos.commit()
                    cursor_newuser.close()
                except Exception as e:
                    print(e)
                
                form.save()
                variable = "sistemas"
                return render(request, 'business/sistemas/usuarios/newuser.html', {'business': variable, 'sistemas': variable, 'permiso': permissions})
    
        else:
            form = UserRegisterForm()
            variable = "sistemas"
            return render(request,'business/sistemas/usuarios/newuser.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form})

            
    else:
        form = UserRegisterForm()
        permissions = 0
        variable = "sistemas"
        return render(request,'business/sistemas/usuarios/newuser.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form})