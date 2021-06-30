import tkinter

def ventanaMenu(): #menu
    ventana = tkinter.Tk()  # Se crea la ventana
    ventana.geometry("250x400")  # Tamanno de la ventana
    ventana.title("Futoshiki")  # Titulo
    titulo = tkinter.Label(ventana, text="FUTOSHIKI", bg='#ff0000', fg='#ffffff', width=20, height=3, font=40)
    titulo.place(x=30,y=20)

    def mostrarConfigurar():
        ventana.destroy()
        ventanaConfigurar()

    def mostrarJugar():
        ventana.destroy()
        ventanaJugar()

    def mostrarAyuda():
        ventana.destroy()
        ventanaAyuda()

    def mostrarAcerca():
        mensaje2("Creado por Jeancarlo Perez")

    botonJugar = tkinter.Button(ventana, text="Jugar", bg="#3B83BD", command=mostrarJugar)
    botonJugar.place(x=110, y=150)

    botonConfiguraciones = tkinter.Button(ventana, text="Configuraciones", bg="#3B83BD",command=mostrarConfigurar)
    botonConfiguraciones.place(x=80, y=190)

    botonAyuda = tkinter.Button(ventana, text="Ayuda", bg="#3B83BD", command=mostrarAyuda)
    botonAyuda.place(x=110, y=230)

    botonAcerca=tkinter.Button(ventana, text="Acerca", bg="#3B83BD", command=mostrarAcerca)
    botonAcerca.place(x=110, y=270)

    ventana.mainloop()