import pyodbc



server = '191.97.47.105'
db = 'MyZetto'
user = 'sa'
psw = 'Sideswipe348'

def SQLRondin():
    try:
        Rondin = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' +server+'; DATABASE='+db+'; UID='+user+'; PWD='+psw)
        return Rondin
    except Exception as e: 
        print(e)
        #print("EXCEPT - CONEXIÓN.PY") 