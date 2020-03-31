import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
cursor.execute("UPDATE PERSONAS SET edad = 25 WHERE nombre = 'richard'")

conexion.commit()
conexion.close()
