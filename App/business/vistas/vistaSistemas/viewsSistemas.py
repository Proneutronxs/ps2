
from django.shortcuts import render
from App.business.consultassql.administracion.contabilidad.sql_contable import sql_periodo
from ps.conexion import *
from ps.permissions import *
from App.business.consultassql.administracion.contabilidad import *
from App.business.forms import *
from datetime import datetime
import calendar

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

###PERIODOS

@login_required
def periodos(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['sistemas'] == 1:
        permissions = 1
        variable = "sistemas"
        return render(request,'business/sistemas/periodos/periodos.html', {'business': variable, 'sistemas': variable, 'permiso': permissions})
    else:
        permissions = 0
        variable = "sistemas"
        return render(request,'business/sistemas/periodos/periodos.html', {'business': variable, 'sistemas': variable, 'permiso': permissions})



#ULTIMO DÍA O INICIO DE MES
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

def empresa_activa(empresa):
    if empresa == "Zetone":
        empresa = "ZETONE"
        return empresa
    elif empresa == "Montever":
        empresa = "ZETONE1"
        return empresa
    elif empresa == "Nyassa":
        empresa = "ZETONE2"
        return empresa
    elif empresa == "Fruit World":
        empresa = "FRUIT"
        return empresa
    elif empresa == "Blue-ZT":
        empresa = "ZETONE3"
        return empresa
    elif empresa == "Blue-FW":
        empresa = "FRUIT4"
        return empresa

## HABILITAR PERIODO

@login_required
def habilitar_periodos(request):
    usr_permisos = user_General(request.user)
    if usr_permisos['sistemas'] == 1:
        permissions = 1
        if request.method == 'POST':
            form = accion_periodo(request.POST)
            if form.is_valid():
                desdeFormat = form.cleaned_data['desde']
                month = datetime.strptime(str(desdeFormat), "%Y-%m-%d").strftime("%m")
                year = datetime.strptime(str(desdeFormat), "%Y-%m-%d").strftime("%Y")
                business = empresa_activa(form.cleaned_data['empresa'])
                if form.cleaned_data['accion'] == "Acción":
                    message = "Selecione la acción a ejecutar."
                    variable = "sistemas"
                    return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form, 'message': message})
                elif form.cleaned_data['empresa'] == "Empresa":
                    message = "Selecione la Empresa."
                    variable = "sistemas"
                    return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form, 'message': message})
                else:
                    if form.cleaned_data['accion'] == "Habilitar":
                        if month == "01":
                            year_aplicable = int(year) - 1
                            month_aplicable = 12
                            day_aplicable = calendar.monthrange(year_aplicable,month_aplicable)
                            formato_sql = str(year_aplicable) + str(month_aplicable) + str(day_aplicable[1])
                            sql = sql_periodo(formato_sql, business, day_aplicable[1])
                            message =  sql 
                            variable = "sistemas"
                            return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form, 'message': message})
                        else:
                            year_aplicable = int(year)
                            month_aplicable = int(month) - 1
                            day_aplicable = calendar.monthrange(year_aplicable,month_aplicable)
                            if month_aplicable < 10:
                                month_aplicable = "0" + str(month_aplicable)
                            formato_sql = str(year_aplicable) + str(month_aplicable) + str(day_aplicable[1]) 
                            sql = sql_periodo(formato_sql, business, day_aplicable[1])
                            message =  sql
                            variable = "sistemas"
                            return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form, 'message': message})                     
                    elif form.cleaned_data['accion'] == "Cerrar":
                        day_aplicable = "01"
                        if month == "12":
                            year_aplicable = int(year) + 1
                            month_aplicable = "01"
                            formato_sql = str(year_aplicable) + str(month_aplicable) + str(day_aplicable) 
                            sql = sql_periodo(formato_sql, business, day_aplicable[1])
                            message =  sql
                            variable = "sistemas"
                            return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form, 'message': message})
                        else:
                            year_aplicable = year
                            month_aplicable = int(month) + 1
                            if month_aplicable < 10:
                                month_aplicable = "0" + str(month_aplicable)
                            formato_sql = str(year_aplicable) + str(month_aplicable) + str(day_aplicable) 
                            sql = sql_periodo(formato_sql, business, day_aplicable[1])
                            message =  sql
                            variable = "sistemas"
                            return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form, 'message': message})
            else:
                form = accion_periodo()
                message = "Selecione las fechas correctamente."
                variable = "sistemas"
                return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form, 'message': message})
        else:
            form = accion_periodo()
            permissions = 0
            variable = "sistemas"
            return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form})
    else:
        form = accion_periodo()
        permissions = 0
        variable = "sistemas"
        return render(request,'business/sistemas/periodos/habilitarperiodo.html', {'business': variable, 'sistemas': variable, 'permiso': permissions, 'form': form})