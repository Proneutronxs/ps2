import pyodbc

zt_server = '191.97.47.105'
zt_user = 'sa'
zt_psw = 'Sideswipe348'
db_SQLRoca5_Zetoneapp = 'ZetoneApp'

def cox():
    connection = None
    if not connection:
        try:
            connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + zt_server +'; DATABASE=' + db_SQLRoca5_Zetoneapp + '; UID=' + zt_user + '; PWD=' + zt_psw)
            #with connection.cursor() as cursor:
            return connection
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