
from ps.conexion import *

server_roca5 = SQLRoca5()

def sql_periodo(formato_sql, business, day_aplicable):

    sql = (str(business), str(formato_sql))
    try:
        with server_roca5.cursor() as cursor:
            cursor.execute("sp_usr_periodo ?, ?", sql)
        #server_roca5.close()
                
        if day_aplicable == "1":
            retorno = "El período se cerró correctamente."
            return retorno
        else:
            retorno = "El período se habilitó correctamente."
            return retorno

    except Exception as retorno2:
        #print(retorno)
        retorno = "Hubo un error al procesar la solicitud.\n" + retorno2
        return retorno