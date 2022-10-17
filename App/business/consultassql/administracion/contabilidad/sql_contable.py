import re
from ps.conexion import *
from App.business.consultassql.administracion.contabilidad import sql_contable

server_roca5 = SQLRoca5()

def sql_periodo(formato_sql, business, day_aplicable):
    try:
        print(formato_sql, business, day_aplicable)
        cursor_roca5 = server_roca5.cursor()
        consula_update1 = ("UPDATE [serverroca5\sqlexpress].ZETONE.dbo.CWPARAMETERS SET NORMALVALUE='" + formato_sql + "'\n" +
            "WHERE ISDEFAULT = 0 AND NAME = 'FC_PERDES'\n" +
            "and COMPANYNAME='" + business + "'")
        consula_update2 = ("UPDATE [serverroca5\sqlexpress].ZETONE.dbo.CWPARAMETERS SET NORMALVALUE='" + formato_sql + "'\n" +
            "WHERE ISDEFAULT = 0 AND NAME = 'VT_PERDES'\n" +
            "and COMPANYNAME='" + business + "'")
        consula_update3 = ("UPDATE [serverroca5\sqlexpress].ZETONE.dbo.CWPARAMETERS SET NORMALVALUE='" + formato_sql + "'\n" +
            "WHERE ISDEFAULT = 0 AND NAME = 'CJ_PERDES'\n" +
            "and COMPANYNAME='" + business + "'")
        consula_update4 = ("UPDATE [serverroca5\sqlexpress].ZETONE.dbo.CWPARAMETERS SET NORMALVALUE='" + formato_sql + "'\n" +
            "WHERE ISDEFAULT = 0 AND NAME = 'pv_PERDES'\n" +
            "and COMPANYNAME='" + business + "'")
        consula_update5 = ("UPDATE [serverroca5\sqlexpress].ZETONE.dbo.CWPARAMETERS SET NORMALVALUE='" + formato_sql + "'\n" + 
            "WHERE ISDEFAULT = 0 AND NAME = 'st_PERDES'\n" +
            "and COMPANYNAME='" + business + "'")

        cursor_roca5.execute(consula_update1)
        server_roca5.commit()
        #cursor_roca5.execute(consula_update2)
        #cursor_roca5.execute(consula_update3)
        #cursor_roca5.execute(consula_update4)
        #cursor_roca5.execute(consula_update5)

        
        if day_aplicable == "1":
            retorno = "El período se cerró correctamente."
            return retorno
        else:
            retorno = "El período se habilitó correctamente."
            return retorno
    except Exception as retorno:
        print(retorno)
        retorno = "Hubo un error al procesar la solicitud"
        return retorno