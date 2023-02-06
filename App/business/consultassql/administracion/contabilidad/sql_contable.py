
from ps.conexion import *
import pyodbc

def sql_periodo(formato_sql, business, day_aplicable):
    zt_server = '191.97.47.105'
    zt_user = 'sa'
    zt_psw = 'Sideswipe348'
    db_SQLRoca5_Zetoneapp = 'Zetoneapp'
    sql = (str(business), str(formato_sql))
    connection = None
    if not connection:
        try:
            connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + zt_server +'; DATABASE=' + db_SQLRoca5_Zetoneapp + '; UID=' + zt_user + '; PWD=' + zt_psw)
            with connection.cursor() as cursor:
                cursor.execute("sp_usr_periodo ?, ?", sql)                    
            if day_aplicable == "1":
                retorno = "El período se cerró correctamente."
                return retorno
            else:
                retorno = "El período se habilitó correctamente."
                return retorno

        except pyodbc.Error as retorno2:
            print("Error:", retorno2)
            if retorno2.args[0] == "08S01":
                try:
                    connection.close()
                except:
                    pass
                connection = None
            retorno = "Hubo un error al procesar la solicitud.\n" + retorno2
            return retorno