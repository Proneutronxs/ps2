from django.shortcuts import render
from django.http import HttpResponse
from ps.conexion import *
import datetime

# Create your views here.
##save/client/nombre=<str:nombre>&ciudad=<str:ciudad>&provincia=<str:provincia>&direccion=<str:direccion>&cuit=<str:cuit>&telefono=<str:telefono>
def insert_Cliente(self, nombre, ciudad, provincia, direccion, cuit, telefono):
    if telefono == "":
        telefono == "0"
    variables = [nombre, ciudad, provincia, direccion, cuit, telefono]
    Viko = ps_VikoSur()
    try:
        cursor_insertCliente = Viko.cursor()
        insertCliente = ("INSERT INTO `Clientes` (`nombreCliente`, `ciudadCliente`, `provinciaCliente`, `direccionCliente`, `cuitCliente`, `telefonoCliente`) VALUES (%s, %s, %s, %s, %s, %s);")
        cursor_insertCliente.execute(insertCliente, variables)
        Viko.commit()
        cursor_insertCliente.close()
        Viko.close()
        respuesta = 'Success'
        lista_estado= [{'Info':respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)
    except Exception as e:
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':e, 'Info2': respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)

def insert_Remito(self, idCliente, fecha):
    fechaMySql = datetime.datetime.strptime(str(fecha), "%d-%m-%Y").strftime("%Y-%m-%d")
    variables = [idCliente, fechaMySql]
    Viko = ps_VikoSur()
    try:
        cursor_insertRemito = Viko.cursor()
        insertRemito = ("INSERT INTO `NumeroRemito` (`idCliente`, `fechaRemito`) VALUES (%s, %s);")
        cursor_insertRemito.execute(insertRemito, variables)
        Viko.commit()
        cursor_insertRemito.close()
        Viko.close()
        respuesta = 'Success'
        lista_estado= [{'Info':respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)
    except Exception as e:
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':e, 'Info2': respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)

def listado_Clientes(self):
    Viko = ps_VikoSur()
    try:
        cursor_mostrarCliente = Viko.cursor()
        mostrarCliente = ("SELECT ID AS ID, nombreCliente AS Cliente FROM `Clientes` ORDER BY Cliente;")
        cursor_mostrarCliente.execute(mostrarCliente)
        if_consulta = cursor_mostrarCliente.fetchall()
        if if_consulta:
            lista_consulta = []
            i = cursor_mostrarCliente.fetchall()
            for i in if_consulta:            
                pb = {'ID':i[0],'Cliente':i[1]}
                lista_consulta.append(pb)
            return HttpResponse([lista_consulta])
    except Exception as e:
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':e, 'Info2': respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)

def max_ID(self):
    Viko = ps_VikoSur()
    try:
        cursor_maxID = Viko.cursor()
        mostrarCliente = ("SELECT MAX(ID) AS ID FROM `NumeroRemito`;")
        cursor_maxID.execute(mostrarCliente)
        if_consulta = cursor_maxID.fetchone()
        if if_consulta:
            lista_consulta = []
            pb = {'ID':if_consulta[0]}
            lista_consulta.append(pb)
            return HttpResponse([lista_consulta])
    except Exception as e:
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':e, 'Info2': respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)

def insert_Data_Remito(self, idRemito, cantidad, descripcion, precio):
    variables = [idRemito, cantidad, descripcion, precio]
    Viko = ps_VikoSur()
    try:
        cursor_insert_Data_Remito = Viko.cursor()
        insertDataRemito = ("INSERT INTO `DatosRemito` (`idRemito`, `cantidadRemito`, `descripcionRemito`, `importeRemito`) VALUES (%s, %s, %s, %s);")
        cursor_insert_Data_Remito.execute(insertDataRemito, variables)
        Viko.commit()
        cursor_insert_Data_Remito.close()
        Viko.close()
        respuesta = 'Success'
        lista_estado= [{'Info':respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)
    except Exception as e:
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':e, 'Info2': respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)