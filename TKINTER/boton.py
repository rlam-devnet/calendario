import tkinter

raiz = tkinter.Tk()
raiz.title(" Boton")


def accion():
    print("Hola Mundo")


boton = tkinter.Button(raiz, text="Ejecutar", command=accion)
boton.pack()

raiz.mainloop()
