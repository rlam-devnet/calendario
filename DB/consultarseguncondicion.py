import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

cursor.execute("SELECT nombre FROM PERSONAS WHERE edad > 20")
nombres = cursor.fetchall()

print(type(nombres))

for nombre in nombres:
    print(nombre)

conexion.close()
