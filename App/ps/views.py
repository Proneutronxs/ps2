from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from .models import *
from urllib import request
from django.views.generic.detail import DetailView
from datetime import datetime
from xhtml2pdf import pisa
from django.template.loader import get_template
from ps.conexion import *
import os
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

# Create your views here.
def index(request):
    variable = "Inicio"
    return render(request,'ps/index.html', {'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def project(request):
    proyectos = projects.objects.all()
    variable = "Proyecto"
    return render(request,'ps/project.html', {'proyectoshtml':proyectos,'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def detail(request, id):
    id = projects.objects.filter(id=id)
    variable = "Proyecto"
    return render(request,'ps/detail.html', {'id': id, 'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def consumoApi(request):
    variable = "consumoApi"
    return render(request,'ps/consumoApi.html', {'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def about1(request):
    about1 = about.objects.all()
    variable = "about"
    return render(request,'ps/about.html', {'abouthtml':about1,'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})

def contact(request):
    if request.GET.get("contact_name"):
        name = request.GET.get("contact_name",0)
        email = request.GET.get("contact_email",1)
        message = request.GET.get("contact_message",2)
        sendContact = send(nombre = name, email = email, mensaje = message)
        sendContact.save()
        variable = "contacto"
        return render(request,'ps/send.html', {'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})
    else:
        variable = "contacto"
        return render(request,'ps/contact.html', {'inicio': variable, 'proyecto': variable, 'consumoApi': variable, 'about': variable, 'contacto': variable})


##Prueba de Rondin
def sqlQuery(request):
    pdf = "pdf"
    if request.GET.get("start"):
        start = request.GET.get("start", 0)
        end = request.GET.get("end", 1)
        planta = request.GET.get("planta", 2)
        formatStart = datetime.strptime(start, "%Y-%m-%d").strftime("%d/%m/%Y")
        formatEnd = datetime.strptime(end, "%Y-%m-%d").strftime("%d/%m/%Y")
        logo = 'static/ps/img/zt.jpg'
        now = datetime.now()
        dia = now.day
        mes = now.month
        año = now.year
        hora = now.time().strftime("%H:%M:%S")
        fechaActual = str(dia) + str(mes) + str(año)
        fechaActual2 = str(dia) + "-" + str(mes) + "-" + str(año)
        try:
            Rondin = SQLRondin()        
            cursor = Rondin.cursor()
            sqlQuery = ("SELECT      Plantas.plantas As Planta, Serenos.sereno AS Sereno, CONVERT(varchar(10), Registros.fechayhora, 103) AS Fecha,CONVERT(varchar(5), Registros.fechayhora, 108) AS Hora, Puntos.punto AS Punto\n" +
                        "FROM            Registros INNER JOIN\n" +
                                "Serenos ON Registros.sereno = Serenos.id INNER JOIN\n" +
                                "Plantas ON Registros.planta = Plantas.ID INNER JOIN\n" +
                                "Puntos ON Registros.punto = Puntos.ID\n" +
                        "WHERE Registros.fechayhora > ? AND CONVERT(varchar(10), Registros.fechayhora, 103) <= ? AND Plantas.plantas = ?\n" +
                        "ORDER BY  Plantas.plantas, Registros.fechayhora, Serenos.sereno, Puntos.punto, Puntos.ID")
            cursor.execute(sqlQuery, formatStart, formatEnd, planta)
            datos = cursor.fetchall()
            if datos:
                lista = []
                ron = cursor.fetchall()
                for ron in datos:
                    resultado = {'Planta': ron[0], 'Sereno': ron[1], 'Fecha': ron[2], 'Hora': ron[3], 'Punto': ron[4]}
                    lista.append(resultado)
                Rondin.close()
                datosResult = [{'planta':planta, 'formatStart':formatStart, 'formatEnd':formatEnd, 'logo': logo, 'hora': hora, 'fechaActual2': fechaActual2}]
                try:
                    template_path = 'ps/pdfrondin.html'
                    context = {'resutadohtml': lista, 'datosResult2': datosResult}
                    response = HttpResponse(content_type='application/pdf')
                    response['Content-Disposition'] = 'attachment; filename= "Rondin - '+ planta +' - '+ fechaActual + "-" + str(hora) +'.pdf"'
                    template = get_template(template_path)
                    html = template.render(context)
                    pisa_status = pisa.CreatePDF(
                        html, dest=response)
                    return response
                except Exception as e:
                    print("Exception")
                    print (e)
            else:
                Rondin.close()
                lista = ["No existen datos para esa Fecha"]
                return render(request,'ps/error.html', {'error': lista})
        except Exception as e:
            lista = [e]
            print (e)
            print(lista)
            return render(request,'ps/error.html', {'error': lista})
    else:
        return render(request,'ps/rondin.html')


""" SELECT      Plantas.plantas As Planta, Legajos.Nombre AS Sereno, Registros.Fecha Fecha, Registros.Hora AS Hora, Puntos.Ubicacion AS Ubicación
                        FROM            Registros INNER JOIN
                                Legajos ON Registros.Sereno = Legajos.ID INNER JOIN
                                Plantas ON Registros.Planta = Plantas.ID INNER JOIN
                                Puntos ON Registros.Punto = Puntos.ID
WHERE Registros.fecha = "2022-09-20" AND Plantas.Plantas = "Planta Uno"
ORDER BY  Plantas.Plantas, Registros.Fecha, Legajos.Nombre, Puntos.Ubicacion, Puntos.ID """