import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS")
datos = cursor.fetchall()

for elementos in datos:
    print(elementos)

conexion.close()
