from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from ps.conexion import *
import datetime
from App.vikosur.modeloPDF import *

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
    finally:
        cursor_insertCliente.close()
        Viko.close()

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
    finally:
        cursor_insertRemito.close()
        Viko.close()

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
                id = str(i[0])
                cliente = str(i[1])       
                pb = {'ID':id,'Cliente':cliente}
                lista_consulta.append(pb)
            return HttpResponse([lista_consulta])
    except Exception as e:
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':e, 'Info2': respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)
    finally:
        cursor_mostrarCliente.close()
        Viko.close()

def listado_Clientes_json(self):
    Viko = ps_VikoSur()
    try:
        cursor_mostrarCliente = Viko.cursor()
        mostrarCliente = ("SELECT ID AS ID, nombreCliente AS Cliente FROM `Clientes` ORDER BY Cliente;")
        cursor_mostrarCliente.execute(mostrarCliente)
        if_consulta = cursor_mostrarCliente.fetchall()
        if if_consulta:
            lista_consulta = []
            for i in if_consulta:     
                id = str(i[0])
                cliente = str(i[1])       
                result = {"ID":id,"Cliente":cliente}
                lista_consulta.append(result)
            jsonList = json.dumps({'message': 'OK','listado':lista_consulta}) 
            return HttpResponse(jsonList, content_type="application/json")
        else:
            jsonList = json.dumps({'message': 'Not Found'}) 
            return HttpResponse(jsonList, content_type="application/json")
    except Exception as e:
        print(e)
        error = str(e)
        jsonList = json.dumps({'error': error}) 
        return HttpResponse(jsonList, content_type="application/json")
    finally:
        cursor_mostrarCliente.close()
        Viko.close()


def data_Clientes_json(self, id):
    Viko = ps_VikoSur()
    try:
        cursor_mostrarCliente = Viko.cursor()
        mostrarCliente = ("SELECT nombreCliente, ciudadCliente, provinciaCliente, direccionCliente, cuitCliente, telefonoCliente FROM `Clientes` WHERE ID='" + str(id) + "';")
        cursor_mostrarCliente.execute(mostrarCliente)
        if_consulta = cursor_mostrarCliente.fetchone()
        if if_consulta: 
            nombre = str(if_consulta[0])
            ciudad = str(if_consulta[1])
            provincia = str(if_consulta[2]) 
            direccion = str(if_consulta[3])
            cuit = str(if_consulta[4])
            telefono = str(if_consulta[5])          
            result = {"Nombre":nombre,"Ciudad":ciudad,"Provincia":provincia,"Direccion":direccion,"Cuit":cuit,"telefono":telefono}
            jsonList = json.dumps({'message': 'Success','Data_Client':result}) 
            return HttpResponse(jsonList, content_type="application/json")
        else:
            jsonList = json.dumps({'message': 'Not Found'}) 
            return HttpResponse(jsonList, content_type="application/json")
    except Exception as e:
        error = str(e)
        jsonList = json.dumps({'error': error}) 
        return HttpResponse(jsonList, content_type="application/json")
    finally:
        cursor_mostrarCliente.close()
        Viko.close()

@csrf_exempt
def update_data_Clientes_json(request):
    if request.method == 'POST' and request.POST.get('id'):
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        ciudad = request.POST.get('ciudad')
        provincia = request.POST.get('provincia')
        direccion = request.POST.get('direccion')
        cuit = request.POST.get('cuit')
        telefono = request.POST.get('telefono')
        Viko = ps_VikoSur()
        try:
            cursor = Viko.cursor()
            actualizarCliente = ("UPDATE `Clientes` SET nombreCliente=%s, ciudadCliente=%s, provinciaCliente=%s, direccionCliente=%s, cuitCliente=%s, telefonoCliente=%s WHERE ID=%s")
            cursor.execute(actualizarCliente, (nombre, ciudad, provincia, direccion, cuit, telefono, id))
            Viko.commit()
            jsonList = json.dumps({'message': 'Success', 'Data_Client': {'ID': id, 'Nombre': nombre, 'Ciudad': ciudad, 'Provincia': provincia, 'Direccion': direccion, 'Cuit': cuit, 'Telefono': telefono}})
            return HttpResponse(jsonList, content_type="application/json")
        except Exception as e:
            error = str(e)
            jsonList = json.dumps({'error': error}) 
            return HttpResponse(jsonList, content_type="application/json")
        finally:
            cursor.close()
            Viko.close()
    else:
            jsonList = json.dumps({'message': 'No se resolvió la petición.'}) 
            return HttpResponse(jsonList, content_type="application/json")


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
    finally:
        cursor_maxID.close()
        Viko.close()

def insert_Data_Remito(self, idRemito, cantidad, descripcion, precio):
    variables = [idRemito, cantidad, descripcion, precio]
    Viko = ps_VikoSur()
    try:
        cursor_insert_Data_Remito = Viko.cursor()
        insertDataRemito = ("INSERT INTO `DatosRemito` (`idRemito`, `cantidadRemito`, `descripcionRemito`, `importeRemito`) VALUES (%s, %s, %s, %s);")
        cursor_insert_Data_Remito.execute(insertDataRemito, variables)
        Viko.commit()

        datosCliente = ("SELECT        NumeroRemito.ID AS numeroPresupuesto, DATE_FORMAT(NumeroRemito.fechaRemito, '%d/%m/%Y') AS Fecha, Clientes.nombreCliente AS Nombre, Clientes.ciudadCliente AS Ciudad, Clientes.provinciaCliente AS Provincia, Clientes.cuitCliente AS CUIT, Clientes.direccionCliente AS Direccion\n"+
                        "FROM            NumeroRemito INNER JOIN\n"+
                                                "Clientes ON NumeroRemito.idCliente = Clientes.ID\n"+
                        "WHERE        (NumeroRemito.ID = '" + idRemito + "')")

        cursor_insert_Data_Remito.execute(datosCliente)
        datos_Cliente = cursor_insert_Data_Remito.fetchone()
        if datos_Cliente:
            pdf = rondinPDF()
            pdf.alias_nb_pages()
            pdf.add_page()

            pdf.set_font('Arial', 'B', 10)#VARIABLE
            pdf.text(x=45, y=60, txt= str(datos_Cliente[2]))#VARIABLE NOMBRE
            pdf.set_font('Arial', '', 8)#VARIABLE
            pdf.text(x=45, y=64, txt= str(datos_Cliente[3]) + ', ' + str(datos_Cliente[4]))#VARIABLE
            pdf.text(x=45, y=68, txt= str(datos_Cliente[6]))#VARIABLE   
            pdf.text(x=45, y=72, txt= str(datos_Cliente[5]))#VARIABLE
            pdf.set_font('Arial', '', 17)#VARIABLE
            pdf.text(x=123, y=33, txt= 'N° 0005 - 00000' + str(datos_Cliente[0]))#VARIABLE
            pdf.set_font('Arial', '', 13)#VARIABLE
            pdf.text(x=123, y=40, txt= 'FECHA ' + str(datos_Cliente[1]))#VARIABLE

            listado_presupuesto = ("SELECT cantidadRemito AS Cantidad, descripcionRemito AS Descripcion, importeRemito AS Importe\n"+
                                    "FROM DatosRemito\n"+
                                    "WHERE idRemito='" + idRemito + "'")
            cursor_insert_Data_Remito.execute(listado_presupuesto)

            i = cursor_insert_Data_Remito.fetchall()
            if i:
                for j in i:
                    print("")
                    pdf.set_font('Arial', '', 10)
                    pdf.cell(w=15, h=7, txt= str(j[0]), border='', align='C', fill=0)
                    pdf.set_font('Arial', '', 8)
                    pdf.cell(w=125, h=7, txt= str(j[1]), border='', align='L', fill=0)
                    pdf.set_font('Arial', '', 10)
                    precioUnitario = round(float(j[2])/int(j[0]),2)
                    precioUnitarioSinComa = str(precioUnitario).replace(".", ",")
                    pdf.cell(w=20, h=7, txt= '$' + str(precioUnitarioSinComa), border='', align='C', fill=0)
                    pdf.multi_cell(w=30, h=7, txt= '$' + str(j[2]), border='', align='C', fill=0)

            suma_total = ("SELECT SUM(CAST(importeRemito AS UNSIGNED)) AS Total\n"+
                            "FROM DatosRemito\n"+
                            "WHERE idRemito='" + idRemito + "'")
            cursor_insert_Data_Remito.execute(suma_total)
            total = cursor_insert_Data_Remito.fetchone()
            if total:
                print("")
                pdf.set_font('Arial', '', 12)#VARIABLES
                pdf.text(x=178, y=285, txt= '$' + str(total[0]))#VARIABLES TOTAL
            

            pdf.output('App/vikosur/presupuestos/'+str(datos_Cliente[2])+"_"+str(datos_Cliente[0])+'.pdf', 'F')
        
        
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
    finally:
        cursor_insert_Data_Remito.close()
        Viko.close()

def download_remito(self, idRemito):

    try:
        f = open('App/vikosur/presupuestos/' + idRemito +'.pdf', 'rb')
        response = HttpResponse(content=f)
        response['Content-Type'] = 'application/pdf'
        return response
    except Exception as e:
        print(e)
        respuesta = 'Error'
        lista_estado= [{'Info':e, 'Info2': respuesta}]
        estado = [lista_estado]
        return HttpResponse(estado)

def maximo_ID():
    Viko = ps_VikoSur()
    try:
        cursor_maxID = Viko.cursor()
        mostrarCliente = ("SELECT MAX(ID) AS ID FROM `NumeroRemito`;")
        cursor_maxID.execute(mostrarCliente)
        if_consulta = cursor_maxID.fetchone()
        if if_consulta:
            return str(if_consulta[0])
    except Exception as e:
        print(e)
    finally:
        cursor_maxID.close()
        Viko.close()


def inserta_cliente(idCliente, fecha):
    Viko = ps_VikoSur()
    fechaMySql = datetime.datetime.strptime(str(fecha), "%d-%m-%Y").strftime("%Y-%m-%d")
    variables = [idCliente, fechaMySql]
    try:
        cursor_insertRemito = Viko.cursor()
        insertRemito = ("INSERT INTO `NumeroRemito` (`idCliente`, `fechaRemito`) VALUES (%s, %s);")
        cursor_insertRemito.execute(insertRemito, variables)
        Viko.commit()
    except Exception as e:
        respuesta = str(e)
    finally:
        cursor_insertRemito.close()
        Viko.close()

def inserta_datos_presupuesto(idRemito, cantidad, descripcion, precio):
    variables = [idRemito, cantidad, descripcion, precio]
    Viko = ps_VikoSur()
    try:
        cursor_insert_Data_Remito = Viko.cursor()
        insertDataRemito = ("INSERT INTO `DatosRemito` (`idRemito`, `cantidadRemito`, `descripcionRemito`, `importeRemito`) VALUES (%s, %s, %s, %s);")
        cursor_insert_Data_Remito.execute(insertDataRemito, variables)
        Viko.commit()
    except Exception as e:
        respuesta = str(e)
    finally:
        cursor_insert_Data_Remito.close()
        Viko.close()


@csrf_exempt   
def insert_Data_Remito_Post(request):
    if request.method == 'POST':
        body = request.body.decode('utf-8')
        fecha = str(json.loads(body)['Fecha'])
        idCliente = str(json.loads(body)['idCliente'])
        validez = str(json.loads(body)['Validez'])
        datos = json.loads(body)['Data']

        #### INSERTA EL CLIENTE
        inserta_cliente(idCliente,fecha)

        #### SELECCIONA EL MAXIMO ID
        idRemito = maximo_ID()
        
        for item in datos:
            cantidad = item['Cantidad']
            descripcion = item['Descripcion']
            precio = item['Precio']
            inserta_datos_presupuesto(idRemito, cantidad, descripcion, precio)
        
        Viko = ps_VikoSur()
        try:
            cursor_insert_Data_Remito = Viko.cursor()
            datosCliente = ("SELECT        NumeroRemito.ID AS numeroPresupuesto, DATE_FORMAT(NumeroRemito.fechaRemito, '%d/%m/%Y') AS Fecha, Clientes.nombreCliente AS Nombre, Clientes.ciudadCliente AS Ciudad, Clientes.provinciaCliente AS Provincia, Clientes.cuitCliente AS CUIT, Clientes.direccionCliente AS Direccion\n"+
                            "FROM            NumeroRemito INNER JOIN\n"+
                                                    "Clientes ON NumeroRemito.idCliente = Clientes.ID\n"+
                            "WHERE        (NumeroRemito.ID = '" + idRemito + "')")

            cursor_insert_Data_Remito.execute(datosCliente)
            datos_Cliente = cursor_insert_Data_Remito.fetchone()
            if datos_Cliente:
                pdf = rondinPDF()
                pdf.alias_nb_pages()
                pdf.add_page()
                pdf.text(x=130, y=80, txt= 'Presupuesto válido por ' + validez + ' días.')
                pdf.set_font('Arial', 'B', 10)#VARIABLE
                pdf.text(x=40, y=60, txt= str(datos_Cliente[2]))#VARIABLE NOMBRE
                pdf.set_font('Arial', '', 8)#VARIABLE
                pdf.text(x=40, y=64, txt= str(datos_Cliente[3]) + ', ' + str(datos_Cliente[4]))#VARIABLE
                pdf.text(x=40, y=68, txt= str(datos_Cliente[6]))#VARIABLE   
                pdf.text(x=40, y=72, txt= str(datos_Cliente[5]))#VARIABLE
                pdf.set_font('Arial', '', 17)#VARIABLE
                pdf.text(x=123, y=33, txt= 'N° 0005 - 00000' + str(datos_Cliente[0]))#VARIABLE
                pdf.set_font('Arial', '', 13)#VARIABLE
                pdf.text(x=123, y=40, txt= 'FECHA ' + str(datos_Cliente[1]))#VARIABLE

                listado_presupuesto = ("SELECT cantidadRemito AS Cantidad, descripcionRemito AS Descripcion, importeRemito AS Importe\n"+
                                        "FROM DatosRemito\n"+
                                        "WHERE idRemito='" + idRemito + "'")
                cursor_insert_Data_Remito.execute(listado_presupuesto)

                i = cursor_insert_Data_Remito.fetchall()
                if i:
                    for j in i:
                        print("")
                        pdf.set_font('Arial', '', 10)
                        pdf.cell(w=15, h=7, txt= str(j[0]), border='', align='C', fill=0)
                        pdf.set_font('Arial', '', 8)
                        pdf.cell(w=125, h=7, txt= str(j[1]), border='', align='L', fill=0)
                        pdf.set_font('Arial', '', 10)
                        precioUnitario = round(float(j[2])/int(j[0]),2)
                        precioUnitarioSinComa = str(precioUnitario).replace(".", ",")
                        pdf.cell(w=20, h=7, txt= '$' + str(precioUnitarioSinComa), border='', align='C', fill=0)
                        pdf.multi_cell(w=30, h=7, txt= '$' + str(j[2]), border='', align='C', fill=0)

                suma_total = ("SELECT SUM(CAST(importeRemito AS UNSIGNED)) AS Total\n"+
                                "FROM DatosRemito\n"+
                                "WHERE idRemito='" + idRemito + "'")
                cursor_insert_Data_Remito.execute(suma_total)
                total = cursor_insert_Data_Remito.fetchone()
                if total:
                    print("")
                    pdf.set_font('Arial', '', 12)#VARIABLES
                    pdf.text(x=178, y=285, txt= '$' + str(total[0]))#VARIABLES TOTAL
                
                cliente = str(datos_Cliente[2]).replace(' ', '_')
                nombre = cliente + "_" + str(datos_Cliente[0])
                pdf.output('App/vikosur/presupuestos/' + nombre + '.pdf', 'F')
                
            return JsonResponse({'Message': 'Success', 'PDF': nombre})
        except Exception as e:
            respuesta = str(e)
            return JsonResponse({'Message': 'Not Found', 'Nota': respuesta})
        finally:
            cursor_insert_Data_Remito.close()
            Viko.close()
    else:
        return JsonResponse({'Message': 'No se pudo resolver la petición.'})
