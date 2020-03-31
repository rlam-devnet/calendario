import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
cursor.execute("SELECT nombre,apellido1 FROM PERSONAS ORDER BY edad")
nombre = cursor.fetchall()

for nombres in nombre:
    print(nombres)

conexion.close()
