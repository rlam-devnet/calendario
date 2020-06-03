import tkinter

raiz = tkinter.Tk()
raiz.title("Campo de Texto")

campo_texto = tkinter.Text(raiz)
campo_texto.config(width=20, height=10, font=("verdana", 16),
                   selectbackground="lightgrey", padx=10, pady=10)
campo_texto.pack()

raiz.mainloop()
