colores = ["rojo", "verde", "azul", "negro"]
# for para recorrer listas
for color in colores:
    print (color)

# for para recorrer un rango automatico
for numero in range(0,10):
    print (numero)

# for para recorrer un rango de 2 en 2
for numero in range(0,10,2):
    print (numero)


# romper un for con el break
for numero in range(0,10):
    print (numero)
    if (numero == 5):
        break

# uso del coninue para dar un salto en el cliclo for en esa evaluación
for numero in range(0, 10):
    if (numero == 5):
        continue
        print (numero)




# uso de for doble
for numero in range(1,5):
    for numero1 in range(0,4):
        print(numero, numero1)






