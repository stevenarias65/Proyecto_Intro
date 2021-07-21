from tkinter import * 

ventana = Tk()

ventana.title("Prueba Github")

etiqueta = Label(ventana, text="Ejemplo de como subir cosas en git").pack()
etiqueta = Label(ventana, text="Etiqueta creada por juan").pack()


def abriVentana():
    global root;
    root = Toplevel(ventana) 

    
#botton = Button(ventana, text="Click aqui", command=abriVentana).pack()



    

ventana.mainloop()

