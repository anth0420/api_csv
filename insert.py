import csv
import sqlite3
from urllib import request


url = "https://raw.githubusercontent.com/anth0420/bot-para-recordar-cumpleanos/main/data.csv"
url_data = request.urlopen(url)
count = dict()
for line in url_data:
    nombres = line.decode().split()
    filas = csv.reader(nombres,delimiter=",")
    lista = list(filas)
    tuplaa = tuple(lista)
    
    conexion = sqlite3.connect("db.db")
    cursor = conexion.cursor()
    cursor.executemany("INSERT INTO usuario_full ('id','name','lastname','firstname','articleNum', 'bithDate','brintMonth','brithDay', 'zodiac') VALUES (?,?,?,?,?,?,?,?,?)",tuplaa)

    conexion.commit()
    conexion.close()

    #insertar

# conexion = sqlite3.connect("db.db")
# cursor = conexion.cursor()
# cursor.executemany("INSERT INTO usuario_full ('id','name','lastname','firstname','articleNum', 'bithDate','brintMonth','brithDay', 'zodiac') VALUES (?,?,?,?,?,?,?,?,?)",tuplaa)

# conexion.commit()
# conexion.close()





