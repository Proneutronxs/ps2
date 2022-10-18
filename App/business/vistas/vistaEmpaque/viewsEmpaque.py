
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


### ZONA EMPAQUE ###

@login_required
def empaque(request):
    print(request.user)
    usr_permisos = user_General(request.user)
    if usr_permisos['empaque'] == 1:
        permissions = 1
        area_permisos = p_empaque(usr_permisos['id'])
        variable = "empaque"
        return render(request,'business/empaque/empaque.html', {'business': variable, 'empaque': variable, 'permiso': permissions, 'permisos': area_permisos})
    else:
        permissions = 0
        variable = "empaque"
        return render(request,'business/empaque/empaque.html', {'business': variable, 'empaque': variable, 'permiso': permissions})

############## ZONA RONDÍN

@login_required
def rondin(request):
    variable = "empaque"
    return render(request,'business/empaque/rondin/rondin.html', {'business': variable, 'empaque': variable})

@login_required
def verRegistros(request):
    if request.GET.get("start") and request.GET.get("end"):
        start = request.GET.get("start", 0)
        end = request.GET.get("end", 1)
        planta = request.GET.get("planta", 2)

        formatStart = datetime.strptime(start, "%Y-%m-%d").strftime("%d/%m/%Y")
        formatEnd = datetime.strptime(end, "%Y-%m-%d").strftime("%d/%m/%Y")
        try:
            Rondin = ps_Rondin()        
            cursor_export = Rondin.cursor()
            sqlQuery = ("SELECT      Plantas.planta As Planta, Legajos.Nombre AS Sereno, DATE_FORMAT(Fecha, '%d/%m/%Y') AS Fecha, Registros.Hora AS Hora, Puntos.Ubicacion AS Ubicación\n" +
                        "FROM            Registros INNER JOIN\n" +
                                "Legajos ON Registros.Sereno = Legajos.ID INNER JOIN\n" +
                                "Plantas ON Registros.Planta = Plantas.ID INNER JOIN\n" +
                                "Puntos ON Registros.Punto = Puntos.ID\n" +
                        "WHERE Registros.fecha BETWEEN '"+ start +"' AND '"+ end +"' AND Plantas.Planta = '"+ planta +"'\n" +
                        "ORDER BY  Plantas.Planta, Registros.Fecha, Registros.Hora") ###, Legajos.Nombre, Puntos.Ubicacion, Puntos.ID
            cursor_export.execute(sqlQuery)
            datos = cursor_export.fetchall()
            if datos:
                lista = []
                ron = cursor_export.fetchall()
                for ron in datos:
                    resultado = {'Planta': ron[0], 'Sereno': ron[1], 'Fecha': ron[2], 'Hora': ron[3], 'Punto': ron[4]}
                    lista.append(resultado)
                Rondin.close()
                datosResult = [{'planta':planta, 'formatStart':formatStart, 'formatEnd':formatEnd}]
                variable = "empaque"
                constante = "activo"
                return render(request,'business/empaque/rondin/verRegistros.html', {'business': variable, 'empaque': variable, 'constante': constante, 'datosResult': datosResult, 'busquedahtml': lista})
            else:
                Rondin.close()
                lista = ["No existen datos para esa Fecha"]
                return render(request,'business/empaque/rondin/errorRondin.html', {'error': lista})
        except Exception as e:
            lista = [e]
            return render(request,'business/empaque/rondin/errorRondin.html', {'error': lista})
    else:
        variable = "empaque"
        return render(request,'business/empaque/rondin/verRegistros.html', {'business': variable, 'empaque': variable})

@login_required
def exportRondin(request):
    if request.GET.get("start") and request.GET.get("end"):
        start = request.GET.get("start", 0)
        end = request.GET.get("end", 1)
        planta = request.GET.get("planta", 2)
        formatStart = datetime.strptime(start, "%Y-%m-%d").strftime("%d/%m/%Y")
        formatEnd = datetime.strptime(end, "%Y-%m-%d").strftime("%d/%m/%Y")
        logo = 'static/business/img/zt.jpg'
        now = datetime.now()
        dia = now.day
        mes = now.month
        año = now.year
        hora = now.time().strftime("%H:%M:%S")
        fechaActual = str(dia) + str(mes) + str(año)
        fechaActual2 = str(dia) + "-" + str(mes) + "-" + str(año)
        try:
            Rondin = ps_Rondin()        
            cursor_export = Rondin.cursor()
            sqlQuery = ("SELECT      Plantas.planta As Planta, Legajos.Nombre AS Sereno, DATE_FORMAT(Fecha, '%d/%m/%Y') AS Fecha, Registros.Hora AS Hora, Puntos.Ubicacion AS Ubicación\n" +
                        "FROM            Registros INNER JOIN\n" +
                                "Legajos ON Registros.Sereno = Legajos.ID INNER JOIN\n" +
                                "Plantas ON Registros.Planta = Plantas.ID INNER JOIN\n" +
                                "Puntos ON Registros.Punto = Puntos.ID\n" +
                        "WHERE Registros.fecha BETWEEN '"+ start +"' AND '"+ end +"' AND Plantas.Planta = '"+ planta +"'\n" +
                        "ORDER BY  Plantas.Planta, Registros.Fecha, Registros.Hora, Legajos.Nombre, Puntos.Ubicacion, Puntos.ID")
            cursor_export.execute(sqlQuery)
            datos = cursor_export.fetchall()
            if datos:
                lista = []
                ron = cursor_export.fetchall()
                for ron in datos:
                    resultado = {'Planta': ron[0], 'Sereno': ron[1], 'Fecha': ron[2], 'Hora': ron[3], 'Punto': ron[4]}
                    lista.append(resultado)
                Rondin.close()
                datosResult = [{'planta':planta, 'formatStart':formatStart, 'formatEnd':formatEnd, 'logo': logo, 'hora': hora, 'fechaActual2': fechaActual2}]
                try:
                    template_path = 'business/empaque/rondin/pdfrondin.html'
                    context = {'resutadohtml': lista, 'datosResult2': datosResult}
                    response = HttpResponse(content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename= "Rondin - '+ planta +' - '+ fechaActual + "-" + str(hora) +'.pdf"'
                    template = get_template(template_path)
                    html = template.render(context)
                    pisa_status = pisa.CreatePDF(
                        html, dest=response)
                    return response
                except Exception as e:
                    lista = [e]
                    print (e)
                    print(lista)
                    return render(request,'business/empaque/rondin/errorRondin.html', {'error': lista})
            else:
                Rondin.close()
                lista = ["No existen datos para esa Fecha"]
                return render(request,'business/empaque/rondin/errorRondin.html', {'error': lista})
        except Exception as e:
            lista = [e]
            print (e)
            print(lista)
            return render(request,'business/empaque/rondin/errorRondin.html', {'error': lista})
    else:
        variable = "empaque"
        return render(request,'business/empaque/rondin/exportRondin.html', {'business': variable, 'empaque': variable})

@login_required
def newSereno(request):
    if request.GET.get("legajo_sereno"):
        legajo = request.GET.get("legajo_sereno",0)
        nombre = request.GET.get("nombre_sereno",1)
        autorizado = request.GET.get("autorizado",2)
        variables = [legajo,nombre]
        if autorizado!= '4992':
            variable = "El Token no es válido!"
            return render(request,'business/empaque/rondin/errorRondin.html', {'error': variable})
        elif len(legajo) > 4:            
            variable = "El Legajo no puede superar los cuatro(4) dígitos."
            return render(request,'business/empaque/rondin/errorRondin.html', {'error': variable})
        else:
            Rondin = ps_Rondin()
            cursorRondin = Rondin.cursor()
            try:
                consulta = ("SELECT ID FROM `Legajos` WHERE ID = '"+ legajo +"'")
                cursorRondin .execute(consulta)
                if_consulta = cursorRondin .fetchall()
                if if_consulta:
                    cursorRondin.close()
                    variable = "El Legajo ya existe!"
                    return render(request,'business/empaque/rondin/errorRondin.html', {'error': variable})
                else:
                    try:
                        insertPunto = ("INSERT INTO `Legajos` (`ID`, `Nombre`) VALUES (%s, %s);")
                        cursorRondin.execute(insertPunto, variables)
                        Rondin.commit()
                        cursorRondin.close()
                        Rondin.close()
                        variable = "El Legajo se guardó correctamente."
                        return render(request,'business/empaque/rondin/exitoRondin.html', {'error': variable})
                    except Exception as e:
                        print(e)
                        variable = "----ERROR DE CONEXIÓN----"
                        return render(request,'business/empaque/rondin/errorRondin.html', {'error': variable})
            except Exception as e:
                print(e)
                variable = "----ERROR DE CONEXIÓN----"
                return render(request,'business/empaque/rondin/errorRondin.html', {'error': variable})
    else:
        variable = "empaque"
        return render(request,'business/empaque/rondin/newsereno.html', {'business': variable, 'empaque': variable})

