class claseSilla:
    color = "rojo"
    precio = 100



nuevasilla = claseSilla()

print (nuevasilla.color)
print (nuevasilla.precio)

nuevasilla2 = claseSilla()
nuevasilla2.color = "verde"
nuevasilla2.precio = 120

print (nuevasilla2.color)
print (nuevasilla2.precio)

class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print ("Hola me llamo {} y tengo {} años".format(self.nombre, self.edad))

nombre = "richard"
edad = 36

persona1 = Persona(nombre, edad)

print (persona1.nombre)
print (persona1.edad)

print (persona1.saludar())

