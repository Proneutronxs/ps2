from email.mime import audio
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
from ps.conexion import *
from xhtml2pdf import pisa
from django.template.loader import get_template

# Create your views here.

####### PARTES DE LA WEB

def business(request):
    variable = "business"
    return render(request,'business/business.html', {'business': variable})

#### ZONA APP ZETONE 

def login(request):
    variable = "business"
    return render(request,'business/login.html', {'business': variable})

### ZONA RONDÍN

def rondin(request):
    variable = "rondin"
    return render(request,'business/rondin.html', {'business': variable, 'rondin': variable})

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
                        "ORDER BY  Plantas.Planta, Registros.Fecha, Legajos.Nombre, Puntos.Ubicacion, Puntos.ID")
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
                variable = "rondin"
                constante = "activo"
                return render(request,'business/verRegistros.html', {'business': variable, 'rondin': variable, 'constante': constante, 'datosResult': datosResult, 'busquedahtml': lista})
            else:
                Rondin.close()
                lista = ["No existen datos para esa Fecha"]
                return render(request,'business/errorRondin.html', {'error': lista})
        except Exception as e:
            lista = [e]
            print (e)
            print(lista)
            return render(request,'business/errorRondin.html', {'error': lista})
    else:
        variable = "rondin"
        return render(request,'business/verRegistros.html', {'business': variable, 'rondin': variable})

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
                        "ORDER BY  Plantas.Planta, Registros.Fecha, Legajos.Nombre, Puntos.Ubicacion, Puntos.ID")
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
                    template_path = 'business/pdfrondin.html'
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
                    return render(request,'business/errorRondin.html', {'error': lista})
            else:
                Rondin.close()
                lista = ["No existen datos para esa Fecha"]
                return render(request,'business/errorRondin.html', {'error': lista})
        except Exception as e:
            lista = [e]
            print (e)
            print(lista)
            return render(request,'business/errorRondin.html', {'error': lista})
    else:
        variable = "rondin"
        return render(request,'business/exportRondin.html', {'business': variable, 'rondin': variable})

def newSereno(request):
    if request.GET.get("legajo_sereno"):
        legajo = request.GET.get("legajo_sereno",0)
        nombre = request.GET.get("nombre_sereno",1)
        autorizado = request.GET.get("autorizado",2)
        variables = [legajo,nombre]
        if autorizado!= '4992':
            variable = "El Token no es válido!"
            return render(request,'business/errorRondin.html', {'error': variable})
        elif len(legajo) > 4:            
            variable = "El Legajo no puede superar los cuatro(4) dígitos."
            return render(request,'business/errorRondin.html', {'error': variable})
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
                    return render(request,'business/errorRondin.html', {'error': variable})
                else:
                    try:
                        insertPunto = ("INSERT INTO `Legajos` (`ID`, `Nombre`) VALUES (%s, %s);")
                        cursorRondin.execute(insertPunto, variables)
                        Rondin.commit()
                        cursorRondin.close()
                        Rondin.close()
                        variable = "El Legajo se guardó correctamente."
                        return render(request,'business/exitoRondin.html', {'error': variable})
                    except Exception as e:
                        print(e)
                        variable = "----ERROR DE CONEXIÓN----"
                        return render(request,'business/errorRondin.html', {'error': variable})
            except Exception as e:
                print(e)
                variable = "----ERROR DE CONEXIÓN----"
                return render(request,'business/errorRondin.html', {'error': variable})
    else:
        variable = "rondin"
        return render(request,'business/newsereno.html', {'business': variable, 'rondin': variable})

#def insertSereno(request):
 



##### FUNCIONES DE COMPROBACIÓN #####



###CONSULTA PRUEBA

def consulta(self):
    fecha = '2022-09-19'
    planta = 'Planta Uno'
    variables = [fecha, planta]
    Rondin = ps_Rondin()
    try:
        cursor = Rondin.cursor()
        consulta = ("SELECT Plantas.planta As Planta, Legajos.Nombre AS Sereno, DATE_FORMAT(Registros.Fecha, '%d/%m/%Y') AS Fecha, DATE_FORMAT(Registros.Hora, ' %T') AS Hora, Puntos.Ubicacion AS Ubicación\n" +
                    "FROM   Registros INNER JOIN\n" +
                            "Legajos ON Registros.Sereno = Legajos.ID INNER JOIN\n" + 
                            "Plantas ON Registros.Planta = Plantas.ID INNER JOIN\n" +
                            "Puntos ON Registros.Punto = Puntos.ID\n" +
                    "WHERE Registros.fecha > '" + fecha + "' AND Plantas.planta = '" + planta + "' \n" +
                    "ORDER BY  Plantas.planta, Registros.Fecha, Legajos.Nombre, Puntos.Ubicacion, Puntos.ID")
        cursor.execute(consulta)
        if_consulta = cursor.fetchall()
        if if_consulta:
            lista_consulta = []
            id = 0
            i = cursor.fetchall()
            for i in if_consulta:            
                pb = {'ID':id,'Planta':i[0], 'Sereno':i[1], 'Fecha':i[2], 'Hora':i[3], 'Ubicación':i[4]}
                lista_consulta.append(pb)
                id = id + 1
            return HttpResponse([lista_consulta])

    except Exception as e:
        print("hola")
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)


######### PARTES DE LA API
### INSERT DE PUNTO DE PUNTO DE CONTROL

#URL: save/point/sereno=<str:sereno>&planta=<str:planta>&punto=<str:punto>&fecha=<str:fecha>&hora=<str:hora>
## save/point/sereno=4992&planta=1&punto=ZT-238-PZ&fecha=2022-09-21&hora=13:06:55
def insert_Punto(self, sereno, planta, punto, fecha, hora):
    estado = 0
    variables = [sereno, planta, punto, fecha, hora, estado]
    Rondin = ps_Rondin()
    try:
        cursor_insertPunto = Rondin.cursor()
        insertPunto = ("INSERT INTO `Registros` (`Sereno`, `Planta`, `Punto`, `Fecha`, `Hora`, `Estado`) VALUES (%s, %s, %s, %s, %s, %s);")
        cursor_insertPunto.execute(insertPunto, variables)
        Rondin.commit()
        cursor_insertPunto.close()
        Rondin.close()
        respuesta = 'Success'
        lista_estado= [{'Info':respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)
    except Exception as e:
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)

# Create your views here.
