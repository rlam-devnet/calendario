import tkinter

raiz = tkinter.Tk()
raiz.title("Mi Label")

# agregamos nuevo componente Label
texto = "mi etiqueta"
etiqueta = tkinter.Label(raiz, text=texto)
etiqueta.config(fg="green", bg="lightgrey", font=("Cortana", 15))
etiqueta.pack()

raiz.mainloop()
