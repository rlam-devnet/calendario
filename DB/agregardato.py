import sqlite3

conexion = sqlite3.connect("basededatos1.db")

cursor = conexion.cursor()
cursor.execute("INSERT INTO PERSONAS VALUES ('danae','albornoz','fernandes',10)")
conexion.commit()
conexion.close()
