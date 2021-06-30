import tkinter

configuracion=[[["a"],["b"]]]
nombre=[" "]
dificultad=["facil"]
timer=["no"]

listaFacil=[
((">", 0, 0), (">", 0, 2), (">", 0, 3),
("4", 1, 0), ("2", 1, 4),
("4", 2, 2),
("<", 3, 3), ("4", 3, 4),
("<", 4, 0), ("<", 4, 1)
)
]

def mensaje(texto,boton): #Se utiliza para mostrar mensajes
    boton.config(bg='#ff0000')
    ventana = tkinter.Tk() #Crea una ventana
    ventana.geometry("300x100")
    ventana.title("Futoshiki") #Se le pone titulo
    Mensaje=tkinter.Label(ventana,text=str(texto)) #Aqui va el mensaje
    Mensaje.place(x=80,y=20)
    def destruir():
        ventana.destroy()
        boton.config(bg="SystemButtonFace")
    Boton=tkinter.Button(ventana,text="Okey",command=destruir) #Boton de ok para salir
    Boton.place(x=120,y=60)

def mensaje2(texto): #Se utiliza para mostrar mensajes
    ventana = tkinter.Tk() #Crea una ventana
    ventana.geometry("300x100")
    ventana.title("Futoshiki") #Se le pone titulo
    Mensaje=tkinter.Label(ventana,text=str(texto)) #Aqui va el mensaje
    Mensaje.place(x=80,y=20)
    Boton=tkinter.Button(ventana,text="Okey",command=ventana.destroy) #Boton de ok para salir
    Boton.place(x=120,y=60)

def ventanaNombre():
    ventana = tkinter.Tk()  # Se crea la ventana
    ventana.geometry("400x250")  # Tamanno de la ventana
    ventana.title("Futoshiki")  # Titulo
    titulo = tkinter.Label(ventana, text="Nombre")
    titulo.place(x=30, y=20)
    nombr = tkinter.Entry(ventana)
    nombr.place(x=100, y=20)

    def listo():
        nombre[0] = nombr.get()
        ventana.destroy()
        ventanaMenu()

    boton = tkinter.Button(ventana, text="Ok", command=listo)
    boton.place(x=100, y=100)
    ventana.mainloop()


def ventanaAyuda():
    ventana = tkinter.Tk()  # Se crea la ventana
    ventana.geometry("1200x600")  # Tamanno de la ventana
    ventana.title("Futoshiki")  # Titulo
    imagen1 = tkinter.PhotoImage(file='img1.png')
    imagen2 = tkinter.PhotoImage(file='img2.png')
    imagen3 = tkinter.PhotoImage(file='img3.png')
    imagen4 = tkinter.PhotoImage(file='img.png')
    imagen5 = tkinter.PhotoImage(file='img_1.png')
    imagen6 = tkinter.PhotoImage(file='img_2.png')
    label1 = tkinter.Label(ventana, image=imagen1)
    label1.place(x=0, y=0)
    label2 = tkinter.Label(ventana, image=imagen2)
    label2.place(x=350, y=0)
    label3 = tkinter.Label(ventana, image=imagen3)
    label3.place(x=750, y=0)

    def volver():
        ventana.destroy()
        ventanaMenu()

    def cambiar():
        label1.config(image=imagen4)
        label2.config(image=imagen5)
        label3.config(image=imagen6)

    def cambiar2():
        label1.config(image=imagen1)
        label2.config(image=imagen2)
        label3.config(image=imagen3)

    boton = tkinter.Button(ventana, text="Volver", command=volver)
    boton.place(x=500, y=500)
    boton2 = tkinter.Button(ventana, text="Siguiente Pagina", command=cambiar)
    boton2.place(x=600, y=500)
    boton3 = tkinter.Button(ventana, text="Pagina Anterior", command=cambiar2)
    boton3.place(x=350, y=500)
    ventana.mainloop()

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

ventanaNombre()