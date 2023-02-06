from django.shortcuts import render
from django.http import JsonResponse
from App.zetone.conexion import *
import json
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'Zetone/inicio/index.html')

def pear(request):
    return render(request, 'Zetone/inicio/pear.html')

def apple(request):
    return render(request, 'Zetone/inicio/apple.html')

def fechaActual():
    hoy = datetime.now()
    dia = hoy.day
    mes = hoy.month
    if hoy.month < 10:
        mes = "0" + str(hoy.month)
    if hoy.day < 10:
        dia = "0" + str(hoy.day)
    return (str(dia) + "/" + str(mes) + "/" + str(hoy.year))
    #return "01/02/2023"

def mandarFecha(request):
    hoy = datetime.now()
    dia = hoy.day
    mes = hoy.month
    if hoy.month < 10:
        mes = "0" + str(hoy.month)
    if hoy.day < 10:
        dia = "0" + str(hoy.day)
    fecha = (str(dia) + "/" + str(mes) + "/" + str(hoy.year))
    data = [{'fecha': fecha}]
    jsonList = json.dumps({'message':'Success', 'fechas': data}) 
    return JsonResponse(jsonList, safe=False)

##JS PERA

##LOTES DE PERA
def consultaLotesPera(request):
    try:
        ZT = cox()
        cursorLotes = ZT.cursor()
        consultaLotes = ("SELECT  CONVERT(varchar(5), LoteEtiquetado.id_lote) + ' / ' + CONVERT(varchar, chacra.USR_CHAC_NOMBRE) AS loteProductor, (CONVERT(varchar(2), LoteEtiquetado.binsEmboq_loteEtiquetado)) AS Lotes, CONVERT(varchar(5), LoteEtiquetado.Fecha, 108) AS fecha\n"+
                        "FROM       [servidordb].Trazabilidad.dbo.LoteEtiquetado WITH (nolock) LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCLOTE AS lote WITH (nolock) ON LoteEtiquetado.id_lote = lote.USR_LOTE_NUMERO LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCMOVCAM AS movcam WITH (nolock) ON movcam.USR_MC_NUMERO = lote.USR_MC_NUMERO LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCCHACRA AS chacra WITH (nolock) ON movcam.USR_CHAC_ALIAS = chacra.USR_CHAC_ALIAS LEFT OUTER JOIN\n"+
                                    "[servidordb].Trazabilidad.dbo.Productor WITH (nolock) ON Productor.id_productor = movcam.USR_CHAC_ALIAS LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCVARIED AS varied WITH (nolock) ON lote.USR_VAR_ALIAS = varied.USR_VAR_ALIAS LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCCUADRO AS cuadro WITH (nolock) ON lote.USR_CUAD_ALIAS = cuadro.USR_CUAD_ALIAS\n"+
                        "WHERE (id_galpon='1' AND CONVERT(varchar(10), Fecha, 103)='" + fechaActual() + "')")
        cursorLotes.execute(consultaLotes)
        consulta = cursorLotes.fetchall()
        if consulta:
            listaLotes = []
            for i in consulta:
                result = {'lote': i[0], 'bins': i[1], 'hora': i[2]}
                listaLotes.append(result)
            jsonList = json.dumps({'message':'Success', 'lotes': listaLotes}) 
            #print(jsonList)
            cursorLotes.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorLotes.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'error'}) 
        return JsonResponse(jsonList, safe=False)

#BINS PROCESADOS
def cantBinsPera(request):
    try:
        ZT = cox()
        cursorLotes = ZT.cursor()
        consultaLotes = ("SELECT SUM(binsEmboq_loteEtiquetado) AS totalProceso\n"+
                        "FROM [servidordb].Trazabilidad.dbo.LoteEtiquetado\n"+
                        "WHERE (id_galpon='1' AND CONVERT(varchar(10), Fecha, 103)='" + fechaActual() + "')")
        cursorLotes.execute(consultaLotes)
        consulta = cursorLotes.fetchone()
        if consulta:
            cantidad = str(consulta[0])
            jsonList = json.dumps({'message':'Success', 'cantidad': cantidad}) 
            #print(jsonList)
            cursorLotes.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorLotes.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#VARIERDAD procesando o no procesando
def procesoPera(request):
    try:
        ZT = cox()
        cursorVaridad = ZT.cursor()
        consultaVariedad = ("SELECT DISTINCT USR_MCVARIED_1.USR_VAR_NOMBRE AS Variedad\n"+
                        "FROM            servidordb.Trazabilidad.dbo.LoteEtiquetado AS LoteEtiquetado_1 INNER JOIN\n"+
                                                "servidordb.Trazabilidad.dbo.Galpon AS Galpon_1 ON LoteEtiquetado_1.id_galpon = Galpon_1.Id_galpon INNER JOIN\n"+
                                                "servidordb.General.dbo.USR_MCLOTE AS lote ON LoteEtiquetado_1.id_lote = lote.USR_LOTE_NUMERO INNER JOIN\n"+
                                                "servidordb.General.dbo.USR_MCVARIED AS USR_MCVARIED_1 ON lote.USR_VAR_ALIAS = USR_MCVARIED_1.USR_VAR_ALIAS RIGHT OUTER JOIN\n"+
                                                "servidordb.General.dbo.USR_MCBINLOT AS bin ON Galpon_1.id_deposito = bin.USR_BINLOT_PCEMB AND lote.USR_LOTE_NUMERO = bin.USR_LOTE_NUMERO LEFT OUTER JOIN\n"+
                                                "servidordb.General.dbo.USR_MCCUADRO AS cuadro ON lote.USR_CUAD_ALIAS = cuadro.USR_CUAD_ALIAS\n"+
                        "WHERE        (CONVERT(varchar(10), bin.USR_BINLOT_FCEMB, 103)='" + fechaActual() + "') AND (Galpon_1.Id_galpon = 1)")
        cursorVaridad.execute(consultaVariedad)
        consulta = cursorVaridad.fetchone()
        if consulta:
            variedad = str(consulta[0])
            jsonList = json.dumps({'message':'Success', 'variedad': variedad}) 
            #print(jsonList)
            cursorVaridad.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorVaridad.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#CAJAS POR CALIDAD
def consultaCajasCalidad(request):
    try:
        ZT = cox()
        cursorCajasCalidad = ZT.cursor()
        consultaCajasCalidad = ("SELECT        Calidad.nombre_calidad AS Calidad, COUNT(1) AS Cajas\n" +
                                        "FROM            servidordb.Trazabilidad.dbo.Bulto INNER JOIN\n" +
                                                                "servidordb.Trazabilidad.dbo.Configuracion ON Bulto.id_configuracion = Configuracion.id_configuracion INNER JOIN\n" +
                                                                "servidordb.Trazabilidad.dbo.Calidad ON Configuracion.id_calidad = Calidad.Id_calidad\n" +
                                        "WHERE        (Bulto.Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (Bulto.id_galpon = '1')\n" +
                                        "GROUP BY Calidad.nombre_calidad\n" +
                                        "ORDER BY Calidad")
        cursorCajasCalidad.execute(consultaCajasCalidad)
        consulta = cursorCajasCalidad.fetchall()
        if consulta:
            listaCajasCalidad = []
            for i in consulta:
                result = {'calidad': i[0], 'cantidad': i[1]}
                listaCajasCalidad.append(result)
            jsonList = json.dumps({'message':'Success', 'cajas': listaCajasCalidad}) 
            #print(jsonList)
            cursorCajasCalidad.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorCajasCalidad.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)


def cantCajas(request):
    try:
        ZT = cox()
        cursorLotes = ZT.cursor()
        consultaLotes = ("SELECT        COUNT(1) AS Cajas\n"+
                        "FROM            servidordb.Trazabilidad.dbo.Bulto\n"+
                        "WHERE        (Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (id_galpon = '1')")
        cursorLotes.execute(consultaLotes)
        consulta = cursorLotes.fetchone()
        if consulta:
            cantidad = str(consulta[0])
            jsonList = json.dumps({'message':'Success', 'cantidad': cantidad}) 
            #print(jsonList)
            cursorLotes.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorLotes.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)


#CAJAS POR CALIBRE
def consultaCajasCalibre(request):
    try:
        ZT = cox()
        cursorCajasCalibre = ZT.cursor()
        consultaCajasCalibre = ("SELECT        Calibre.nombre_calibre AS Calibre, COUNT(1) AS Cajas\n" +
                                "FROM            servidordb.Trazabilidad.dbo.Bulto INNER JOIN\n" +
                                                        "servidordb.Trazabilidad.dbo.Configuracion ON Bulto.id_configuracion = Configuracion.id_configuracion INNER JOIN\n" +
                                                        "servidordb.Trazabilidad.dbo.Calibre ON Configuracion.id_calibre = Calibre.Id_calibre\n" +
                                "WHERE        (Bulto.Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (Bulto.id_galpon = '1')\n" +
                                "GROUP BY Calibre.nombre_calibre\n" +
                                "ORDER BY Calibre")
        cursorCajasCalibre.execute(consultaCajasCalibre )
        consulta = cursorCajasCalibre.fetchall()
        if consulta:
            listaCajasCalibre = []
            for i in consulta:
                result = {'calibre': i[0], 'cantidad': i[1]}
                listaCajasCalibre.append(result)
            jsonList = json.dumps({'message':'Success', 'cajas': listaCajasCalibre}) 
            #print(jsonList)
            cursorCajasCalibre.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorCajasCalibre.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#CAJAS POR MARCA
def consultaCajasMarca(request):
    try:
        ZT = cox()
        cursorCajasMarca = ZT.cursor()
        consultaCajasMarca = ("SELECT        Marca.Nombre_marca AS Marca, COUNT(1) AS Cajas\n"+
                                "FROM            servidordb.Trazabilidad.dbo.Bulto INNER JOIN \n"+
                                                        "servidordb.Trazabilidad.dbo.Configuracion ON Bulto.id_configuracion = Configuracion.id_configuracion INNER JOIN\n"+
                                                        "servidordb.Trazabilidad.dbo.Marca ON Configuracion.id_marca = Marca.id_marca\n"+
                                "WHERE        (Bulto.Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (Bulto.id_galpon = '1')\n"+
                                "GROUP BY Marca.Nombre_marca\n"+
                                "ORDER BY Marca")
        cursorCajasMarca.execute(consultaCajasMarca)
        consulta = cursorCajasMarca.fetchall()
        if consulta:
            listaCajasMarca = []
            for i in consulta:
                result = {'marca': i[0], 'cantidad': i[1]}
                listaCajasMarca.append(result)
            jsonList = json.dumps({'message':'Success', 'cajas': listaCajasMarca}) 
            #print(jsonList)
            cursorCajasMarca.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorCajasMarca.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#CAJAS POR ENVASE
def consultaCajasEnvase(request):
    try:
        ZT = cox()
        cursorCajasEnvase = ZT.cursor()
        consultaCajasEnvase = ("SELECT        Envase.nombre_envase AS Envase, COUNT(1) AS Cajas\n"+
                                "FROM            servidordb.Trazabilidad.dbo.Bulto INNER JOIN\n"+
                                                        "servidordb.Trazabilidad.dbo.Configuracion ON Bulto.id_configuracion = Configuracion.id_configuracion INNER JOIN\n"+
                                                        "servidordb.Trazabilidad.dbo.Envase ON Configuracion.id_envase = Envase.id_envase\n"+
                                "WHERE        (Bulto.Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (Bulto.id_galpon = '1')\n"+
                                "GROUP BY Envase.nombre_envase\n"+
                                "ORDER BY Envase.nombre_envase")
        cursorCajasEnvase.execute(consultaCajasEnvase)
        consulta = cursorCajasEnvase.fetchall()
        if consulta:
            listaCajasEnvase = []
            for i in consulta:
                result = {'envase': i[0], 'cantidad': i[1]}
                listaCajasEnvase.append(result)
            jsonList = json.dumps({'message':'Success', 'cajas': listaCajasEnvase}) 
            #print(jsonList)
            cursorCajasEnvase.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorCajasEnvase.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)


#EMPAQUE MANZANA

##LOTES DE MANZANA
def consultaLotesManzana(request):
    try:
        ZT = cox()
        cursorLotes = ZT.cursor()
        consultaLotes = ("SELECT  CONVERT(varchar(5), LoteEtiquetado.id_lote) + ' / ' + CONVERT(varchar, chacra.USR_CHAC_NOMBRE) AS loteProductor, (CONVERT(varchar(2), LoteEtiquetado.binsEmboq_loteEtiquetado)) AS Lotes, CONVERT(varchar(5), LoteEtiquetado.Fecha, 108) AS fecha\n"+
                        "FROM       [servidordb].Trazabilidad.dbo.LoteEtiquetado WITH (nolock) LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCLOTE AS lote WITH (nolock) ON LoteEtiquetado.id_lote = lote.USR_LOTE_NUMERO LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCMOVCAM AS movcam WITH (nolock) ON movcam.USR_MC_NUMERO = lote.USR_MC_NUMERO LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCCHACRA AS chacra WITH (nolock) ON movcam.USR_CHAC_ALIAS = chacra.USR_CHAC_ALIAS LEFT OUTER JOIN\n"+
                                    "[servidordb].Trazabilidad.dbo.Productor WITH (nolock) ON Productor.id_productor = movcam.USR_CHAC_ALIAS LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCVARIED AS varied WITH (nolock) ON lote.USR_VAR_ALIAS = varied.USR_VAR_ALIAS LEFT OUTER JOIN\n"+
                                    "[servidordb].General.dbo.USR_MCCUADRO AS cuadro WITH (nolock) ON lote.USR_CUAD_ALIAS = cuadro.USR_CUAD_ALIAS\n"+
                        "WHERE (id_galpon='8' AND CONVERT(varchar(10), Fecha, 103)='" + fechaActual() + "')")
        cursorLotes.execute(consultaLotes)
        consulta = cursorLotes.fetchall()
        if consulta:
            listaLotes = []
            for i in consulta:
                result = {'lote': i[0], 'bins': i[1], 'hora': i[2]}
                listaLotes.append(result)
            jsonList = json.dumps({'message':'Success', 'lotes': listaLotes}) 
            #print(jsonList)
            cursorLotes.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorLotes.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#BINS PROCESADOS
def cantBinsManzana(request):
    try:
        ZT = cox()
        cursorLotes = ZT.cursor()
        consultaLotes = ("SELECT SUM(binsEmboq_loteEtiquetado) AS totalProceso\n"+
                        "FROM [servidordb].Trazabilidad.dbo.LoteEtiquetado\n"+
                        "WHERE (id_galpon='8' AND CONVERT(varchar(10), Fecha, 103)='" + fechaActual() + "')")
        cursorLotes.execute(consultaLotes)
        consulta = cursorLotes.fetchone()
        if consulta:
            cantidad = str(consulta[0])
            jsonList = json.dumps({'message':'Success', 'cantidad': cantidad}) 
            #print(jsonList)
            cursorLotes.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorLotes.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#VARIERDAD procesando o no procesando
def procesoManzana(request):
    try:
        ZT = cox()
        cursorVaridad = ZT.cursor()
        consultaVariedad = ("SELECT DISTINCT USR_MCVARIED_1.USR_VAR_NOMBRE AS Variedad\n"+
                        "FROM            servidordb.Trazabilidad.dbo.LoteEtiquetado AS LoteEtiquetado_1 INNER JOIN\n"+
                                                "servidordb.Trazabilidad.dbo.Galpon AS Galpon_1 ON LoteEtiquetado_1.id_galpon = Galpon_1.Id_galpon INNER JOIN\n"+
                                                "servidordb.General.dbo.USR_MCLOTE AS lote ON LoteEtiquetado_1.id_lote = lote.USR_LOTE_NUMERO INNER JOIN\n"+
                                                "servidordb.General.dbo.USR_MCVARIED AS USR_MCVARIED_1 ON lote.USR_VAR_ALIAS = USR_MCVARIED_1.USR_VAR_ALIAS RIGHT OUTER JOIN\n"+
                                                "servidordb.General.dbo.USR_MCBINLOT AS bin ON Galpon_1.id_deposito = bin.USR_BINLOT_PCEMB AND lote.USR_LOTE_NUMERO = bin.USR_LOTE_NUMERO LEFT OUTER JOIN\n"+
                                                "servidordb.General.dbo.USR_MCCUADRO AS cuadro ON lote.USR_CUAD_ALIAS = cuadro.USR_CUAD_ALIAS\n"+
                        "WHERE        (CONVERT(varchar(10), bin.USR_BINLOT_FCEMB, 103)='" + fechaActual() + "') AND (Galpon_1.Id_galpon = 8)")
        cursorVaridad.execute(consultaVariedad)
        consulta = cursorVaridad.fetchone()
        if consulta:
            cantidad = str(consulta[0])
            jsonList = json.dumps({'message':'Success', 'cantidad': cantidad}) 
            #print(jsonList)
            cursorVaridad.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorVaridad.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#CAJAS POR CALIDAD
def consultaCajasCalidadManzana(request):
    try:
        ZT = cox()
        cursorCajasCalidad = ZT.cursor()
        consultaCajasCalidadManzana = ("SELECT        Calidad.nombre_calidad AS Calidad, COUNT(1) AS Cajas\n" +
                                        "FROM            servidordb.Trazabilidad.dbo.Bulto INNER JOIN\n" +
                                                                "servidordb.Trazabilidad.dbo.Configuracion ON Bulto.id_configuracion = Configuracion.id_configuracion INNER JOIN\n" +
                                                                "servidordb.Trazabilidad.dbo.Calidad ON Configuracion.id_calidad = Calidad.Id_calidad\n" +
                                        "WHERE        (Bulto.Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (Bulto.id_galpon = '8')\n" +
                                        "GROUP BY Calidad.nombre_calidad\n" +
                                        "ORDER BY Calidad")
        cursorCajasCalidad.execute(consultaCajasCalidadManzana)
        consulta = cursorCajasCalidad.fetchall()
        if consulta:
            listaCajasCalidad = []
            for i in consulta:
                result = {'calidad': i[0], 'cantidad': i[1]}
                listaCajasCalidad.append(result)
            jsonList = json.dumps({'message':'Success', 'cajas': listaCajasCalidad}) 
            #print(jsonList)
            cursorCajasCalidad.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorCajasCalidad.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)


def cantCajasManzana(request):
    try:
        ZT = cox()
        cursorLotes = ZT.cursor()
        consultaLotes = ("SELECT        COUNT(1) AS Cajas\n"+
                        "FROM            servidordb.Trazabilidad.dbo.Bulto\n"+
                        "WHERE        (Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (id_galpon = '8')")
        cursorLotes.execute(consultaLotes)
        consulta = cursorLotes.fetchone()
        if consulta:
            cantidad = str(consulta[0])
            jsonList = json.dumps({'message':'Success', 'cantidad': cantidad}) 
            #print(jsonList)
            cursorLotes.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorLotes.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#CAJAS POR CALIBRE
def consultaCajasCalibreManzana(request):
    try:
        ZT = cox()
        cursorCajasCalibre = ZT.cursor()
        consultaCajasCalibreManzana = ("SELECT        Calibre.nombre_calibre AS Calibre, COUNT(1) AS Cajas\n" +
                                "FROM            servidordb.Trazabilidad.dbo.Bulto INNER JOIN\n" +
                                                        "servidordb.Trazabilidad.dbo.Configuracion ON Bulto.id_configuracion = Configuracion.id_configuracion INNER JOIN\n" +
                                                        "servidordb.Trazabilidad.dbo.Calibre ON Configuracion.id_calibre = Calibre.Id_calibre\n" +
                                "WHERE        (Bulto.Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (Bulto.id_galpon = '8')\n" +
                                "GROUP BY Calibre.nombre_calibre\n" +
                                "ORDER BY Calibre")
        cursorCajasCalibre.execute(consultaCajasCalibreManzana )
        consulta = cursorCajasCalibre.fetchall()
        if consulta:
            listaCajasCalibre = []
            for i in consulta:
                result = {'calibre': i[0], 'cantidad': i[1]}
                listaCajasCalibre.append(result)
            jsonList = json.dumps({'message':'Success', 'cajas': listaCajasCalibre}) 
            #print(jsonList)
            cursorCajasCalibre.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorCajasCalibre.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#CAJAS POR MARCA
def consultaCajasMarcaManzana(request):
    try:
        ZT = cox()
        cursorCajasMarca = ZT.cursor()
        consultaCajasMarcaManzana = ("SELECT        Marca.Nombre_marca AS Marca, COUNT(1) AS Cajas\n"+
                                "FROM            servidordb.Trazabilidad.dbo.Bulto INNER JOIN \n"+
                                                        "servidordb.Trazabilidad.dbo.Configuracion ON Bulto.id_configuracion = Configuracion.id_configuracion INNER JOIN\n"+
                                                        "servidordb.Trazabilidad.dbo.Marca ON Configuracion.id_marca = Marca.id_marca\n"+
                                "WHERE        (Bulto.Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (Bulto.id_galpon = '8')\n"+
                                "GROUP BY Marca.Nombre_marca\n"+
                                "ORDER BY Marca")
        cursorCajasMarca.execute(consultaCajasMarcaManzana)
        consulta = cursorCajasMarca.fetchall()
        if consulta:
            listaCajasMarca = []
            for i in consulta:
                result = {'marca': i[0], 'cantidad': i[1]}
                listaCajasMarca.append(result)
            jsonList = json.dumps({'message':'Success', 'cajas': listaCajasMarca}) 
            #print(jsonList)
            cursorCajasMarca.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorCajasMarca.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)

#CAJAS POR ENVASE
def consultaCajasEnvaseManzana(request):
    try:
        ZT = cox()
        cursorCajasEnvase = ZT.cursor()
        consultaCajasEnvaseManzana = ("SELECT        Envase.nombre_envase AS Envase, COUNT(1) AS Cajas\n"+
                                "FROM            servidordb.Trazabilidad.dbo.Bulto INNER JOIN\n"+
                                                        "servidordb.Trazabilidad.dbo.Configuracion ON Bulto.id_configuracion = Configuracion.id_configuracion INNER JOIN\n"+
                                                        "servidordb.Trazabilidad.dbo.Envase ON Configuracion.id_envase = Envase.id_envase\n"+
                                "WHERE        (Bulto.Id_bulto > 17273700) AND CONVERT(varchar(10), Bulto.fecha_alta_bulto, 103)='" + fechaActual() + "' AND (Bulto.id_galpon = '8')\n"+
                                "GROUP BY Envase.nombre_envase\n"+
                                "ORDER BY Envase.nombre_envase")
        cursorCajasEnvase.execute(consultaCajasEnvaseManzana)
        consulta = cursorCajasEnvase.fetchall()
        if consulta:
            listaCajasEnvase = []
            for i in consulta:
                result = {'envase': i[0], 'cantidad': i[1]}
                listaCajasEnvase.append(result)
            jsonList = json.dumps({'message':'Success', 'cajas': listaCajasEnvase}) 
            #print(jsonList)
            cursorCajasEnvase.close()
            ZT.close()
            return JsonResponse(jsonList, safe=False)
        else:
            cursorCajasEnvase.close()
            ZT.close()
            jsonList = json.dumps({'message':'Not Found'}) 
            return JsonResponse(jsonList, safe=False)
    except Exception as e:
        print("Error")
        print(e)
        jsonList = json.dumps({'message':'Not Found'}) 
        return JsonResponse(jsonList, safe=False)
