import pyodbc
import mysql.connector


###SERVIDOR EMPRESA ZETONE
zt_server = '191.97.47.105'
zt_user = 'sa'
zt_psw = 'Sideswipe348'

###SERVIDOR PRONEUTRONXS
ps_server = 'localhost'
ps_user = 'psphpmyadminps'
ps_psw = 'Proneutronxs$%Sideswipe$%1722'
ps_port = '3306'


###CONEXIONES SERVIDOR EMPRESA ZETONE

#VARIABLE DATABASE
db_SQLRondin = 'MyZetto'

def SQLRondin():
    try:
        Rondin = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' + zt_server +'; DATABASE=' + db_SQLRondin + '; UID=' + zt_user + '; PWD=' + zt_psw)
        return Rondin
    except Exception as e: 
        print(e)
        print("EXCEPT - CONEXIÓN.PY") 



###CONEXIONES SERVIDOR PRONEUTRONXS

#VARIABLE DATABASE
ps_db_Rondin = 'Rondin'

def ps_Rondin():
    try:
        ps_Rondin = mysql.connector.connect(host = ps_server, port = ps_port, user = ps_user, password = ps_psw, db = ps_db_Rondin)
        return ps_Rondin
    except Exception as e:
        print(e)
        print("EXCEPT - CONEXIÓN.PY") 

ps_db_Permisos = 'Permisos'

def ps_Permisos():
    try:
        ps_Rondin = mysql.connector.connect(host = ps_server, port = ps_port, user = ps_user, password = ps_psw, db = ps_db_Permisos)
        return ps_Rondin
    except Exception as e:
        print(e)
        print("EXCEPT - CONEXIÓN.PY")