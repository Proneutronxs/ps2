import pyodbc
import mysql.connector


###SERVIDOR EMPRESA ZETONE
zt_server = '191.97.47.105'
zt_user = 'sa'
zt_psw = 'Sideswipe348'

###SERVIDOR PRONEUTRONXS
ps_server = 'localhost'
#ps_user = 'Sideswipe'
#ps_psw = 'Sideswipe348'
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
        print("EXCEPT - CONEXIÓN.PY RONDIN") 

db_SQLRoca5_Zetoneapp = 'Zetoneapp'



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
        return e

ps_db_permisos = 'Permisos'

def ps_Permisos():
    try:
        ps_permisos = mysql.connector.connect(host = ps_server, port = ps_port, user = ps_user, password = ps_psw, db = ps_db_permisos)
        return ps_permisos
    except Exception as e:
        print(e)
        print("EXCEPT - CONEXIÓN.PY")

ps_db_permisos_zetone = 'ZetoneApp'

def ps_Permisos_zetone():
    try:
        ps_permisos = mysql.connector.connect(host = ps_server, port = ps_port, user = ps_user, password = ps_psw, db = ps_db_permisos_zetone)
        return ps_permisos
    except Exception as e:
        print(e)
        print("EXCEPT - CONEXIÓN.PY")


#VARIABLE DATABASE
ps_db_VikoSur = 'VikoSur'

def ps_VikoSur():
    try:
        ps_VikoSur = mysql.connector.connect(host = ps_server, port = ps_port, user = ps_user, password = ps_psw, db = ps_db_VikoSur)
        return ps_VikoSur
    except Exception as e:
        
        print(e)
        print("EXCEPT - VIKOSUR-CONEXIÓN.PY") 
        return e
