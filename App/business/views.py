from contextlib import redirect_stderr
from email.mime import audio
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from datetime import datetime
from ps.conexion import *
from ps.permissions import *
from django.template.loader import get_template

##LOGIN
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import logout



# Create your views here.

####### PARTES DE LA WEB

def index(request):
    return render(request,'business/index.html')

@login_required
def business(request):
    variable = "business"
    return render(request,'business/business.html', {'business': variable})

#### ZONA ZETONE 

def login_entrar(request):
    return render(request,'business/registration/login.html')


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
        lista_estado= [{'Info':e, 'Info2': Rondin}]
        estado = [lista_estado]
        return HttpResponse(estado)

# Create your views here.
