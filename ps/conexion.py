import pyodbc



server = '191.97.47.105'
db = 'MyZetto'
user = 'sa'
psw = 'Sideswipe348'
try:
    Zetone = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=' +server+'; DATABASE='+db+'; UID='+user+'; PWD='+psw)
    #print("CONECTADO")
except Exception as e: 
    print(e)
    #print("EXCEPT") 