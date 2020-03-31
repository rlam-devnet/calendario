import sqlite3

conexion = sqlite3.connect("basededatos1.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS")

personas = cursor.fetchall()

print(personas[0][2])

for persona in personas:
    print(persona)

conexion.close()
