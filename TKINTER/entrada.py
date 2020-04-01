import tkinter

raiz = tkinter.Tk()
raiz.title("Campo de Entrada")

entrada = tkinter.Entry(raiz)
entrada.configure(justify="center", show="*")
entrada.pack()

raiz.mainloop()
