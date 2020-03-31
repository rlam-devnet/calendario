import sqlite3

elementos = [("richard", "albornoz", "monsalve", 36), ("denise", "fernandez", "briceño", 40)]

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()
cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)", elementos)
conexion.commit()
conexion.close()
