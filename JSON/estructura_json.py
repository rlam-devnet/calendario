import json

producto1 = { "nombre":"silla", "color":"azul", "precio":100 }

#convertimos un diccionario de python a estructura json
estructura_json = json.dumps(producto1)

print(estructura_json)
print(type(estructura_json))
print(type(producto1))

#convertimos una estructura json a estructura diccionario de python

estructura_python = json.loads(estructura_json)
print(estructura_python)
print(type(estructura_python))
print(estructura_python["precio"])





