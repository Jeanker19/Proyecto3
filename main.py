import tkinter
import random
import time
from threading import *

configuracion=[[["a"],["b"]]]
nombre=[" "]
dificultad=["facil"]
timer=["no"]

listaFacil=[[]]

listaFacil1=[]
listaMedio1=[]
listaDificil1=[]
contador=0

archivo=open("futoshiki2021partidas.dat","r")
texto=archivo.readlines()
for i in range(len(texto)):
    texto[i] = texto[i].rstrip("\n")

listaGrande=[[]]

for i in range(len(texto)):
    if texto[i]=="":
        contador=contador+1
        if contador<=3:
            listaFacil1.append(listaGrande[0])
            listaGrande[0]=[]
        if contador>3 and contador<=6:
            listaMedio1.append(listaGrande[0])
            listaGrande[0]=[]
        if contador>6:
            listaDificil1.append(listaGrande[0])
            listaGrande[0]=[]

    else:
        listaGrande[0].append((texto[i][0], int(texto[i][3]), int(texto[i][6])))

if dificultad[0]=="facil":
    randon=random.randrange(0,3)
    listaFacil[0]=listaFacil1[randon]

if dificultad[0]=="medio":
    randon=random.randrange(0,3)
    listaFacil[0]=listaMedio1[randon]

if dificultad[0]=="dificil":
    randon=random.randrange(0,3)
    listaFacil[0]=listaDificil1[randon]

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

def ventanaJugar(): #Ventana jugar
    activo=[0]
    listaJugadas=[] #jugadas a guardar
    matrizJuego=[[0,".",0,".",0,".",0,".",0],
                 [".",".",".",".","."],
                 [0,".",0,".",0,".",0,".",0],
                 [".", ".", ".", ".", "."],
                 [0,".",0,".",0,".",0,".",0],
                 [".", ".", ".", ".", "."],
                 [0,".",0,".",0,".",0,".",0],
                 [".", ".", ".", ".", "."],
                 [0,".",0,".",0,".",0,".",0]]

    seleccionado=["0"]
    ventana=tkinter.Tk() #Se crea la ventana
    ventana.geometry("700x650") #Tamanno de la ventana
    ventana.title("Futoshiki") #Titulo
    #Labels
    titulo=tkinter.Label(ventana,text="FUTOSHIKI",bg='#ff0000', fg='#ffffff',width=20,height=3,font=40)
    titulo.place(x=255,y=0)
    labelNombreJugador=tkinter.Label(ventana,text="Nombre del jugador:",font=40)
    labelNombreJugador.place(x=20,y=100)
    nombreJugador=tkinter.Label(ventana,text="",font=40,borderwidth=1, relief="solid",width=35)
    nombreJugador.place(x=180,y=100)
    nombreJugador.config(text=str(nombre[0]))
    #labels y botones

    labelHorasTexto=tkinter.Label(ventana,text="HH")
    labelMinutosTexto=tkinter.Label(ventana,text="MM")
    labelSegundosTexto=tkinter.Label(ventana,text="SS")
    labelHoras=tkinter.Label(ventana,text="0")
    labelMinutos=tkinter.Label(ventana,text="0")
    labelSegundos=tkinter.Label(ventana,text="0")
    labelSegundosTexto.place(x=410,y=580)
    labelMinutosTexto.place(x=385,y=580)
    labelHorasTexto.place(x=360,y=580)
    labelSegundos.place(x=415,y=600)
    labelMinutos.place(x=390,y=600)
    labelHoras.place(x=365,y=600)

    labelFlecha01=tkinter.Label(ventana,text="",font=40)
    labelFlecha02 = tkinter.Label(ventana, text="",font=40)
    labelFlecha03 = tkinter.Label(ventana, text="",font=40)
    labelFlecha04 = tkinter.Label(ventana, text="",font=40)

    labelFlecha01.place(x=230,y=155)
    labelFlecha02.place(x=300,y=155)
    labelFlecha03.place(x=370, y=155)
    labelFlecha04.place(x=440, y=155)

    labelFlecha11 = tkinter.Label(ventana, text="",font=40)
    labelFlecha12 = tkinter.Label(ventana, text="",font=40)
    labelFlecha13 = tkinter.Label(ventana, text="",font=40)
    labelFlecha14 = tkinter.Label(ventana, text="",font=40)
    labelFlecha15 = tkinter.Label(ventana, text="",font=40)

    labelFlecha11.place(x=195,y=190)
    labelFlecha12.place(x=265,y=190)
    labelFlecha13.place(x=335, y=190)
    labelFlecha14.place(x=405, y=190)
    labelFlecha15.place(x=475, y=190)


    labelFlecha21 = tkinter.Label(ventana, text="",font=40)
    labelFlecha22 = tkinter.Label(ventana, text="",font=40)
    labelFlecha23 = tkinter.Label(ventana, text="",font=40)
    labelFlecha24 = tkinter.Label(ventana, text="",font=40)

    labelFlecha21.place(x=230, y=225)
    labelFlecha22.place(x=300, y=225)
    labelFlecha23.place(x=370, y=225)
    labelFlecha24.place(x=440, y=225)

    labelFlecha31 = tkinter.Label(ventana, text="",font=40)
    labelFlecha32 = tkinter.Label(ventana, text="",font=40)
    labelFlecha33 = tkinter.Label(ventana, text="",font=40)
    labelFlecha34 = tkinter.Label(ventana, text="",font=40)
    labelFlecha35 = tkinter.Label(ventana, text="",font=40)

    labelFlecha31.place(x=195, y=260)
    labelFlecha32.place(x=265, y=260)
    labelFlecha33.place(x=335, y=260)
    labelFlecha34.place(x=405, y=260)
    labelFlecha35.place(x=475, y=260)

    labelFlecha41 = tkinter.Label(ventana, text="",font=40)
    labelFlecha42 = tkinter.Label(ventana, text="",font=40)
    labelFlecha43 = tkinter.Label(ventana, text="",font=40)
    labelFlecha44 = tkinter.Label(ventana, text="",font=40)

    labelFlecha41.place(x=230, y=295)
    labelFlecha42.place(x=300, y=295)
    labelFlecha43.place(x=370, y=295)
    labelFlecha44.place(x=440, y=295)

    labelFlecha51 = tkinter.Label(ventana, text="",font=40)
    labelFlecha52 = tkinter.Label(ventana, text="",font=40)
    labelFlecha53 = tkinter.Label(ventana, text="",font=40)
    labelFlecha54 = tkinter.Label(ventana, text="",font=40)
    labelFlecha55 = tkinter.Label(ventana, text="",font=40)

    labelFlecha51.place(x=195, y=330)
    labelFlecha52.place(x=265, y=330)
    labelFlecha53.place(x=335, y=330)
    labelFlecha54.place(x=405, y=330)
    labelFlecha55.place(x=475, y=330)

    labelFlecha61 = tkinter.Label(ventana, text="",font=40)
    labelFlecha62 = tkinter.Label(ventana, text="",font=40)
    labelFlecha63 = tkinter.Label(ventana, text="",font=40)
    labelFlecha64 = tkinter.Label(ventana, text="",font=40)

    labelFlecha61.place(x=230, y=365)
    labelFlecha62.place(x=300, y=365)
    labelFlecha63.place(x=370, y=365)
    labelFlecha64.place(x=440, y=365)

    labelFlecha71 = tkinter.Label(ventana, text="",font=40)
    labelFlecha72 = tkinter.Label(ventana, text="",font=40)
    labelFlecha73 = tkinter.Label(ventana, text="",font=40)
    labelFlecha74 = tkinter.Label(ventana, text="",font=40)
    labelFlecha75 = tkinter.Label(ventana, text="",font=40)

    labelFlecha71.place(x=195, y=400)
    labelFlecha72.place(x=265, y=400)
    labelFlecha73.place(x=335, y=400)
    labelFlecha74.place(x=405, y=400)
    labelFlecha75.place(x=475, y=400)

    labelFlecha81 = tkinter.Label(ventana, text="",font=40)
    labelFlecha82 = tkinter.Label(ventana, text="",font=40)
    labelFlecha83 = tkinter.Label(ventana, text="",font=40)
    labelFlecha84 = tkinter.Label(ventana, text="",font=40)

    labelFlecha81.place(x=230, y=435)
    labelFlecha82.place(x=300, y=435)
    labelFlecha83.place(x=370, y=435)
    labelFlecha84.place(x=440, y=435)


    def cronometro():
        for hora in range(24):
            for minuto in range(60):
                for segundo in range(60):
                    time.sleep(1)
                    labelSegundos.config(text=str(segundo))
                    labelMinutos.config(text=str(minuto))
                    labelHoras.config(text=str(hora))

 #cuando gana
    def ganar():
        for i in range(len(matrizJuego)):
            for j in range(len(matrizJuego[i])):
                if matrizJuego[i][j]==0:
                    return False
        return True
    #si gana se agrega al top
    def victoria():
        mensaje2("Has ganado")
        archivo=open("futoshiki2021top10.dat","a")
        archivo.write(dificultad[0]+"\n")
        archivo.write(nombre[0]+"\n")
        archivo.write(labelHoras.cget("text")+"\n")
        archivo.write(labelMinutos.cget("text") + "\n")
        archivo.write(labelSegundos.cget("text") + "\n")
    #verificar si se cumple para agregar boton
    def verificar(x,y,numero):
        def existe():
            for i in range(len(matrizJuego)):
                if i%2==0:
                    if matrizJuego[i][y] == numero or matrizJuego[i][y] == int(numero):
                        return "No valido, ya esta en la columna"
            if int(numero) not in matrizJuego[x]:
                if numero not in matrizJuego[x]:
                    return True
                else:
                    return "No valido, ya esta en la fila"
            else:
                return "No valido, ya esta en la fila"
        if y==0:
            numeroY=0
        if y==2:
            numeroY=1
        if y==4:
            numeroY=2
        if y==6:
            numeroY=3
        if y==8:
            numeroY=4
        if y+1<8:
            if existe()==True:
                if matrizJuego[x][y+1]==">":
                    if int(matrizJuego[x][y+2])<int(numero) or int(matrizJuego[x][y+2])==0:
                        if x+1<8:
                            if matrizJuego[x+1][numeroY]==".":
                                if x-1<0:
                                    return True
                                elif matrizJuego[x-1][numeroY]==".":
                                    return True
                            if matrizJuego[x+1][numeroY]=="v":
                                if int(matrizJuego[x+2][y])<int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es mayor"
                            if matrizJuego[x+1][numeroY]=="^":
                                if int(matrizJuego[x+2][y])>int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es menor"
                            if matrizJuego[x-1][numeroY]=="^":
                                if int(matrizJuego[x-2][y])<int(numero) or  int(matrizJuego[x-2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es mayor"
                            if matrizJuego[x-1][numeroY]=="v":
                                if int(matrizJuego[x+2][y])>int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es menor"
                    else:
                        return "No valido, no es mayor"

                if matrizJuego[x][y-1]==">":
                    if int(matrizJuego[x][y-2])>int(numero) or int(matrizJuego[x][y-2])==0:
                        if x + 1 < 8:
                            if matrizJuego[x + 1][numeroY] == ".":
                                if x - 1 < 0:
                                    return True
                                elif matrizJuego[x - 1][numeroY] == ".":
                                    return True
                            if matrizJuego[x + 1][numeroY] == "v":
                                if int(matrizJuego[x + 2][y]) < int(numero) or int(matrizJuego[x + 2][y]) == 0:
                                    return True
                                else:
                                    return "No valido, no es mayor"
                            if matrizJuego[x-1][numeroY]=="v":
                                if int(matrizJuego[x+2][y])>int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es menor"
                            if matrizJuego[x+1][numeroY]=="^":
                                if int(matrizJuego[x+2][y])>int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es menor"
                            if matrizJuego[x-1][numeroY]=="^":
                                if int(matrizJuego[x-2][y])<int(numero) or  int(matrizJuego[x-2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es mayor"
                    else:
                        return "No valido, no es menor"

                if matrizJuego[x][y+1]=="<":
                    if int(matrizJuego[x][y+2])>int(numero) or int(matrizJuego[x][y+2])==0:
                        if x + 1 < 8:
                            if matrizJuego[x + 1][numeroY] == ".":
                                if x - 1 < 0:
                                    return True
                                elif matrizJuego[x - 1][numeroY] == ".":
                                    return True
                            if matrizJuego[x + 1][numeroY] == "v":
                                if int(matrizJuego[x + 2][y]) < int(numero) or int(matrizJuego[x + 2][y]) == 0:
                                    return True
                                else:
                                    return "No es valido, no es mayor"
                            if matrizJuego[x-1][numeroY]=="v":
                                if int(matrizJuego[x+2][y])>int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es menor"
                            if matrizJuego[x+1][numeroY]=="^":
                                if int(matrizJuego[x+2][y])>int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es menor"
                            if matrizJuego[x-1][numeroY]=="^":
                                if int(matrizJuego[x-2][y])<int(numero) or  int(matrizJuego[x-2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es mayor"
                    else:
                        return "No valido, no es menor"
                if matrizJuego[x][y-1]=="<":
                    if int(matrizJuego[x][y-2])<int(numero) or int(matrizJuego[x][y-2])==0:
                        if x + 1 < 8:
                            if matrizJuego[x + 1][numeroY] == ".":
                                if x - 1 < 0:
                                    return True
                                elif matrizJuego[x - 1][numeroY] == ".":
                                    return True
                            if matrizJuego[x + 1][numeroY] == "v":
                                if int(matrizJuego[x + 2][y]) < int(numero) or int(matrizJuego[x + 2][y]) == 0:
                                    return True
                                return "No valido, no es mayor"
                            if matrizJuego[x-1][numeroY]=="v":
                                if int(matrizJuego[x+2][y])>int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es menor"
                            if matrizJuego[x+1][numeroY]=="^":
                                if int(matrizJuego[x+2][y])>int(numero) or  int(matrizJuego[x+2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es menor"
                            if matrizJuego[x-1][numeroY]=="^":
                                if int(matrizJuego[x-2][y])<int(numero) or  int(matrizJuego[x-2][y])==0:
                                    return True
                                else:
                                    return "No valido, no es mayor"
                    else:
                        return "No valido, no es mayor"
                if x + 1 < 8:
                    if matrizJuego[x - 1][numeroY] == "v":
                        if int(matrizJuego[x - 2][y]) > int(numero) or int(matrizJuego[x -2][y]) == 0:
                            return True
                        else:
                            return "No valido, no es menor"
                    if matrizJuego[x + 1][numeroY] == "."  and matrizJuego[x-1][numeroY]==".":
                        return True
                    if matrizJuego[x + 1][numeroY] == "v":
                        if matrizJuego[x + 2][numeroY] < int(numero) or int(matrizJuego[x + 2][numeroY]) == 0:
                            return True
                        else:
                            return "No valido, no es mayor"
                    if matrizJuego[x - 1][numeroY] == "^":
                        if int(matrizJuego[x - 2][y]) < int(numero) or int(matrizJuego[x -2][y]) == 0:
                            return True
                        else:
                            return "No valido, no es mayor"
                    if matrizJuego[x + 1][numeroY] == "^":
                        if int(matrizJuego[x + 2][y]) > int(numero) or int(matrizJuego[x +2][y]) == 0:
                            return True
                        else:
                            return "No valido, no es mayor"
                else:
                    if matrizJuego[x - 1][numeroY] == "v":
                        if int(matrizJuego[x - 2][y]) > int(numero) or int(matrizJuego[x -2][y]) == 0:
                            return True
                        else:
                            return "No valido, no es menor"
                    if matrizJuego[x - 1][numeroY] == "^":
                        if int(matrizJuego[x - 2][y]) < int(numero) or int(matrizJuego[x -2][y]) == 0:
                            return True
                        else:
                            return "No valido, no es mayor"
                    return True
                if matrizJuego[x][numeroY+1]=="." and matrizJuego[x + 1][numeroY]==".":
                    return True

            else:
                return existe()

        else:
            if existe()==True:
                if matrizJuego[x][y-1]==">":
                    if int(matrizJuego[x][y-2])>int(numero) or int(matrizJuego[x][y-2])==0:
                        return True
                    else:
                        return "No valido, no es menor"
                if matrizJuego[x][y-1]=="<":
                    if int(matrizJuego[x][y-2])<int(numero) or int(matrizJuego[x][y-2])==0:
                        return True
                    else:
                        return "No valido, no es mayor"
                if matrizJuego[x][y-1]==".":
                    return True
            else:
                return existe()
    #por si selecciona algun boton
    def tocarBoton1():
        victoria()
        if activo[0] == 1:
            if seleccionado[0]=="1":
                boton1.config(bg='#0000ff')
                seleccionado[0]="0"
            else:
                boton1.config(bg='#00BD2D')
                boton2.config(bg='#0000ff')
                boton3.config(bg='#0000ff')
                boton4.config(bg='#0000ff')
                boton5.config(bg='#0000ff')
                seleccionado[0]="1"

    def tocarBoton2():
        if activo[0] == 1:
            if seleccionado[0]=="2":
                boton2.config(bg='#0000ff')
                seleccionado[0]="0"
            else:
                boton2.config(bg='#00BD2D')
                boton1.config(bg='#0000ff')
                boton3.config(bg='#0000ff')
                boton4.config(bg='#0000ff')
                boton5.config(bg='#0000ff')
                seleccionado[0] = "2"

    def tocarBoton3():
        if activo[0] == 1:
            if seleccionado[0]=="3":
                boton3.config(bg='#0000ff')
                seleccionado[0]="0"
            else:
                boton3.config(bg='#00BD2D')
                boton2.config(bg='#0000ff')
                boton1.config(bg='#0000ff')
                boton4.config(bg='#0000ff')
                boton5.config(bg='#0000ff')
                seleccionado[0] = "3"

    def tocarBoton4():
        if activo[0] == 1:
            if seleccionado[0]=="4":
                boton4.config(bg='#0000ff')
                seleccionado[0]="0"
            else:
                boton4.config(bg='#00BD2D')
                boton2.config(bg='#0000ff')
                boton3.config(bg='#0000ff')
                boton1.config(bg='#0000ff')
                boton5.config(bg='#0000ff')
                seleccionado[0] = "4"

    def tocarBoton5():
        if activo[0] == 1:
            if seleccionado[0]=="5":
                boton5.config(bg='#0000ff')
                seleccionado[0]="0"
            else:
                boton5.config(bg='#00BD2D')
                boton2.config(bg='#0000ff')
                boton3.config(bg='#0000ff')
                boton4.config(bg='#0000ff')
                boton1.config(bg='#0000ff')
                seleccionado[0] = "5"

    def tocarBoton11():
        if activo[0]==1:
            if type(matrizJuego[0][0]) != int or matrizJuego[0][0] == 0:
                if seleccionado[0] != "0":
                    if verificar(0, 0, seleccionado[0]) == True:
                        boton11.config(text=seleccionado)
                        matrizJuego[0][0] = seleccionado[0]
                        listaJugadas.append([seleccionado[0],0,0])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(0, 0, seleccionado[0]), boton11)
            else:
                mensaje("No valido, digito fijo", boton11)

    def tocarBoton12():
        if activo[0] == 1:
            if type(matrizJuego[0][2]) != int or matrizJuego[0][2]==0:
                if seleccionado[0]!="0":
                    if verificar(0,2,seleccionado[0])==True:
                        boton12.config(text=seleccionado)
                        matrizJuego[0][2] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 0, 2])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(0,2,seleccionado[0]),boton12)
            else:
                mensaje("No valido, digito fijo",boton12)

    def tocarBoton13():
        if activo[0] == 1:
            if type(matrizJuego[0][4]) != int or matrizJuego[0][4]==0:
                if seleccionado[0] != "0":
                    if verificar(0, 4, seleccionado[0]) == True:
                        boton13.config(text=seleccionado)
                        matrizJuego[0][4] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 0, 4])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(0, 4, seleccionado[0]), boton13)
            else:
                mensaje("No valido, digito fijo", boton13)

    def tocarBoton14():
        if activo[0] == 1:
            if type(matrizJuego[0][6]) != int or matrizJuego[0][6] == 0:
                if seleccionado[0] != "0":
                    if verificar(0, 6, seleccionado[0]) == True:
                        boton14.config(text=seleccionado)
                        matrizJuego[0][6] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 0, 6])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(0, 6, seleccionado[0]), boton14)
            else:
                mensaje("No valido, digito fijo", boton14)

    def tocarBoton15():
        if activo[0] == 1:
            if type(matrizJuego[0][8]) != int or matrizJuego[0][8] == 0:
                if seleccionado[0] != "0":
                    if verificar(0, 8, seleccionado[0]) == True:
                        boton15.config(text=seleccionado)
                        matrizJuego[0][8] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 0, 8])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(0, 8, seleccionado[0]), boton15)
            else:
                mensaje("No valido, digito fijo", boton15)

    def tocarBoton21():
        if activo[0] == 1:
            if type(matrizJuego[2][0]) != int or matrizJuego[2][0] == 0:
                if seleccionado[0] != "0":
                    if verificar(2, 0, seleccionado[0]) == True:
                        boton21.config(text=seleccionado)
                        matrizJuego[2][0] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 2, 0])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(2, 0, seleccionado[0]), boton21)
            else:
                mensaje("No valido, digito fijo", boton21)

    def tocarBoton22():
        if activo[0] == 1:
            if type(matrizJuego[2][2]) != int or matrizJuego[2][2] == 0:
                if seleccionado[0] != "0":
                    if verificar(2, 2, seleccionado[0]) == True:
                        boton22.config(text=seleccionado)
                        matrizJuego[2][2] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 2, 2])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(2, 2, seleccionado[0]), boton22)
            else:
                mensaje("No valido, digito fijo", boton22)

    def tocarBoton23():
        if activo[0] == 1:
            if type(matrizJuego[2][4]) != int or matrizJuego[2][4] == 0:
                if seleccionado[0] != "0":
                    if verificar(2, 4, seleccionado[0]) == True:
                        boton23.config(text=seleccionado)
                        matrizJuego[2][4] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 2, 4])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(2, 4, seleccionado[0]), boton23)
            else:
                mensaje("No valido, digito fijo", boton23)

    def tocarBoton24():
        if activo[0] == 1:
            if type(matrizJuego[2][6]) != int or matrizJuego[2][6] == 0:
                if seleccionado[0] != "0":
                    if verificar(2, 6, seleccionado[0]) == True:
                        boton24.config(text=seleccionado)
                        matrizJuego[2][6] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 2, 6])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(2, 6, seleccionado[0]), boton24)
            else:
                mensaje("No valido, digito fijo", boton24)

    def tocarBoton25():
        if activo[0] == 1:
            if type(matrizJuego[2][8]) != int or matrizJuego[2][8] == 0:
                if seleccionado[0] != "0":
                    if verificar(2, 8, seleccionado[0]) == True:
                        boton25.config(text=seleccionado)
                        matrizJuego[2][8] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 2, 8])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(2, 8, seleccionado[0]), boton25)
            else:
                mensaje("No valido, digito fijo", boton25)

    def tocarBoton31():
        if activo[0] == 1:
            if type(matrizJuego[4][0]) != int or matrizJuego[4][0] == 0:
                if seleccionado[0] != "0":
                    if verificar(4, 0, seleccionado[0]) == True:
                        boton31.config(text=seleccionado)
                        matrizJuego[4][0] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 4, 0])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(4, 0, seleccionado[0]), boton31)
            else:
                mensaje("No valido, digito fijo", boton31)

    def tocarBoton32():
        if activo[0] == 1:
            if type(matrizJuego[4][2]) != int or matrizJuego[4][2] == 0:
                if seleccionado[0] != "0":
                    if verificar(4,2, seleccionado[0]) == True:
                        boton32.config(text=seleccionado)
                        matrizJuego[4][2] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 4, 2])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(4, 2, seleccionado[0]), boton32)
            else:
                mensaje("No valido, digito fijo", boton32)

    def tocarBoton33():
        if activo[0] == 1:
            if type(matrizJuego[4][4]) != int or matrizJuego[4][4] == 0:
                if seleccionado[0] != "0":
                    if verificar(4, 4, seleccionado[0]) == True:
                        boton33.config(text=seleccionado)
                        matrizJuego[4][4] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 4, 4])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(4, 4, seleccionado[0]), boton33)
            else:
                mensaje("No valido, digito fijo", boton33)

    def tocarBoton34():
        if activo[0] == 1:
            if type(matrizJuego[4][6]) != int or matrizJuego[4][6] == 0:
                if seleccionado[0] != "0":
                    if verificar(4, 6, seleccionado[0]) == True:
                        boton34.config(text=seleccionado)
                        matrizJuego[4][6] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 4, 6])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(4, 6, seleccionado[0]), boton34)
            else:
                mensaje("No valido, digito fijo", boton34)

    def tocarBoton35():
        if activo[0] == 1:
            if type(matrizJuego[4][8]) != int or matrizJuego[4][8] == 0:
                if seleccionado[0] != "0":
                    if verificar(4, 8, seleccionado[0]) == True:
                        boton35.config(text=seleccionado)
                        matrizJuego[4][8] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 4, 8])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(4, 8, seleccionado[0]), boton35)
            else:
                mensaje("No valido, digito fijo", boton35)

    def tocarBoton41():
        if activo[0] == 1:
            if type(matrizJuego[6][0]) != int or matrizJuego[6][0] == 0:
                if seleccionado[0] != "0":
                    if verificar(6, 0, seleccionado[0]) == True:
                        boton41.config(text=seleccionado)
                        matrizJuego[6][0] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 6, 0])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(6, 0, seleccionado[0]), boton41)
            else:
                mensaje("No valido, digito fijo", boton41)

    def tocarBoton42():
        if activo[0] == 1:
            if type(matrizJuego[6][2]) != int or matrizJuego[6][2] == 0:
                if seleccionado[0] != "0":
                    if verificar(6, 2, seleccionado[0]) == True:
                        boton42.config(text=seleccionado)
                        matrizJuego[6][2] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 6, 2])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(6, 2, seleccionado[0]), boton42)
            else:
                mensaje("No valido, digito fijo", boton42)

    def tocarBoton43():
        if activo[0] == 1:
            if type(matrizJuego[6][4]) != int or matrizJuego[6][4] == 0:
                if seleccionado[0] != "0":
                    if verificar(6, 4, seleccionado[0]) == True:
                        boton43.config(text=seleccionado)
                        matrizJuego[6][4] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 6, 4])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(6, 4, seleccionado[0]), boton43)
            else:
                mensaje("No valido, digito fijo", boton43)

    def tocarBoton44():
        if activo[0] == 1:
            if type(matrizJuego[6][6]) != int or matrizJuego[6][6] == 0:
                if seleccionado[0] != "0":
                    if verificar(6, 6, seleccionado[0]) == True:
                        boton44.config(text=seleccionado)
                        matrizJuego[6][6] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 6, 6])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(6, 6, seleccionado[0]), boton44)
            else:
                mensaje("No valido, digito fijo", boton44)

    def tocarBoton45():
        if activo[0] == 1:
            if type(matrizJuego[6][8]) != int or matrizJuego[6][8] == 0:
                if seleccionado[0] != "0":
                    if verificar(6, 8, seleccionado[0]) == True:
                        boton45.config(text=seleccionado)
                        matrizJuego[6][8] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 6, 8])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(6, 8, seleccionado[0]), boton45)
            else:
                mensaje("No valido, digito fijo", boton45)

    def tocarBoton51():
        if activo[0] == 1:
            if type(matrizJuego[8][0]) != int or matrizJuego[8][0] == 0:
                if seleccionado[0] != "0":
                    if verificar(8, 0, seleccionado[0]) == True:
                        boton51.config(text=seleccionado)
                        matrizJuego[8][0] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 8, 0])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(8, 0, seleccionado[0]), boton51)
            else:
                mensaje("No valido, digito fijo", boton51)

    def tocarBoton52():
        if activo[0] == 1:
            if type(matrizJuego[8][2]) != int or matrizJuego[8][2] == 0:
                if seleccionado[0] != "0":
                    if verificar(8, 2, seleccionado[0]) == True:
                        boton52.config(text=seleccionado)
                        matrizJuego[8][2] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 8, 2])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(8, 2, seleccionado[0]), boton52)
            else:
                mensaje("No valido, digito fijo", boton52)

    def tocarBoton53():
        if activo[0] == 1:
            if type(matrizJuego[8][4]) != int or matrizJuego[8][4] == 0:
                if seleccionado[0] != "0":
                    if verificar(8, 4, seleccionado[0]) == True:
                        boton53.config(text=seleccionado)
                        matrizJuego[8][4] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 8, 4])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(8, 4, seleccionado[0]), boton53)
            else:
                mensaje("No valido, digito fijo", boton53)

    def tocarBoton54():
        if activo[0] == 1:
            if type(matrizJuego[8][6]) != int or matrizJuego[8][6] == 0:
                if seleccionado[0] != "0":
                    if verificar(8, 6, seleccionado[0]) == True:
                        boton54.config(text=seleccionado)
                        matrizJuego[8][6] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 8, 6])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(8, 6, seleccionado[0]), boton54)
            else:
                mensaje("No valido, digito fijo", boton54)

    def tocarBoton55():
        if activo[0] == 1:
            if type(matrizJuego[8][8]) != int or matrizJuego[8][8] == 0:
                if seleccionado[0] != "0":
                    if verificar(8, 8, seleccionado[0]) == True:
                        boton55.config(text=seleccionado)
                        matrizJuego[8][8] = seleccionado[0]
                        listaJugadas.append([seleccionado[0], 8, 8])
                        if ganar()==True:
                            victoria()
                    else:
                        mensaje(verificar(8, 8, seleccionado[0]), boton55)
            else:
                mensaje("No valido, digito fijo", boton55)

    boton1 = tkinter.Button(ventana, text="1", width=5, height=2, borderwidth=1, relief="solid", bg='#0000ff',command=tocarBoton1)
    boton2 = tkinter.Button(ventana, text="2", width=5, height=2, borderwidth=1, relief="solid", bg='#0000ff',command=tocarBoton2)
    boton3 = tkinter.Button(ventana, text="3", width=5, height=2, borderwidth=1, relief="solid", bg='#0000ff',command=tocarBoton3)
    boton4 = tkinter.Button(ventana, text="4", width=5, height=2, borderwidth=1, relief="solid", bg='#0000ff',command=tocarBoton4)
    boton5 = tkinter.Button(ventana, text="5", width=5, height=2, borderwidth=1, relief="solid", bg='#0000ff',command=tocarBoton5)

    boton1.place(x=600, y=150)
    boton2.place(x=600, y=220)
    boton3.place(x=600, y=290)
    boton4.place(x=600, y=360)
    boton5.place(x=600, y=430)

    boton11 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton11)
    boton12 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton12)
    boton13 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton13)
    boton14 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton14)
    boton15 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton15)


    boton21 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton21)
    boton22 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton22)
    boton23 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton23)
    boton24 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton24)
    boton25 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton25)

    boton31 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton31)
    boton32 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton32)
    boton33 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton33)
    boton34 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton34)
    boton35 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton35)

    boton41 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton41)
    boton42 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton42)
    boton43 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton43)
    boton44 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton44)
    boton45 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton45)

    boton51 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton51)
    boton52 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton52)
    boton53 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton53)
    boton54 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton54)
    boton55 = tkinter.Button(ventana, text="", width=5, height=2, borderwidth=1, relief="solid",command=tocarBoton55)

    boton11.place(x=180, y=150)
    boton12.place(x=250, y=150)
    boton13.place(x=320, y=150)
    boton14.place(x=390, y=150)
    boton15.place(x=460, y=150)

    boton21.place(x=180, y=220)
    boton22.place(x=250, y=220)
    boton23.place(x=320, y=220)
    boton24.place(x=390, y=220)
    boton25.place(x=460, y=220)

    boton31.place(x=180, y=290)
    boton32.place(x=250, y=290)
    boton33.place(x=320, y=290)
    boton34.place(x=390, y=290)
    boton35.place(x=460, y=290)

    boton41.place(x=180, y=360)
    boton42.place(x=250, y=360)
    boton43.place(x=320, y=360)
    boton44.place(x=390, y=360)
    boton45.place(x=460, y=360)

    boton51.place(x=180, y=430)
    boton52.place(x=250, y=430)
    boton53.place(x=320, y=430)
    boton54.place(x=390, y=430)
    boton55.place(x=460, y=430)

    def actualizar():
        hilo = Thread(target=cronometro)
        hilo.start()
        activo[0] = 1
        for i in range(len(listaFacil[0])):
            if listaFacil[0][i][0]=="<":
                x=listaFacil[0][i][1]
                y = listaFacil[0][i][2]
                if x==0:
                    if y==0:
                        matrizJuego[0][1]="<"
                    if y==1:
                        matrizJuego[0][3]="<"
                    if y==2:
                        matrizJuego[0][5]="<"
                    if y==3:
                        matrizJuego[0][7]="<"
                if x==1:
                    if y==0:
                        matrizJuego[2][1]="<"
                    if y==1:
                        matrizJuego[2][3]="<"
                    if y==2:
                        matrizJuego[2][5]="<"
                    if y==3:
                        matrizJuego[2][7]="<"
                if x==2:
                    if y==0:
                        matrizJuego[4][1]="<"
                    if y==1:
                        matrizJuego[4][3]="<"
                    if y==2:
                        matrizJuego[4][5]="<"
                    if y==3:
                        matrizJuego[4][7]="<"
                if x==3:
                    if y==0:
                        matrizJuego[6][1]="<"
                    if y==1:
                        matrizJuego[6][3]="<"
                    if y==2:
                        matrizJuego[6][5]="<"
                    if y==3:
                        matrizJuego[6][7]="<"
                if x==4:
                    if y==0:
                        matrizJuego[8][1]="<"
                    if y==1:
                        matrizJuego[8][3]="<"
                    if y==2:
                        matrizJuego[8][5]="<"
                    if y==3:
                        matrizJuego[8][7]="<"
            if listaFacil[0][i][0] == ">":
                x = listaFacil[0][i][1]
                y = listaFacil[0][i][2]
                if x == 0:
                    if y == 0:
                        matrizJuego[0][1] = ">"
                    if y == 1:
                        matrizJuego[0][3] = ">"
                    if y == 2:
                        matrizJuego[0][5] = ">"
                    if y == 3:
                        matrizJuego[0][7] = ">"
                if x == 1:
                    if y == 0:
                        matrizJuego[2][1] = ">"
                    if y == 1:
                        matrizJuego[2][3] = ">"
                    if y == 2:
                        matrizJuego[2][5] = ">"
                    if y == 3:
                        matrizJuego[2][7] = ">"
                if x == 2:
                    if y == 0:
                        matrizJuego[4][1] = ">"
                    if y == 1:
                        matrizJuego[4][3] = ">"
                    if y == 2:
                        matrizJuego[4][5] = ">"
                    if y == 3:
                        matrizJuego[4][7] = ">"
                if x == 3:
                    if y == 0:
                        matrizJuego[6][1] = ">"
                    if y == 1:
                        matrizJuego[6][3] = ">"
                    if y == 2:
                        matrizJuego[6][5] = ">"
                    if y == 3:
                        matrizJuego[6][7] = ">"
                if x == 4:
                    if y == 0:
                        matrizJuego[8][1] = ">"
                    if y == 1:
                        matrizJuego[8][3] = ">"
                    if y == 2:
                        matrizJuego[8][5] = ">"
                    if y == 3:
                        matrizJuego[8][7] = ">"
            if listaFacil[0][i][0] == "v":
                x = listaFacil[0][i][1]
                y = listaFacil[0][i][2]
                if x == 0:
                    if y == 0:
                        matrizJuego[1][0] = "v"
                    if y == 1:
                        matrizJuego[1][1] = "v"
                    if y == 2:
                        matrizJuego[1][2] = "v"
                    if y == 3:
                        matrizJuego[1][3] = "v"
                    if y == 4:
                        matrizJuego[1][4] = "v"
                if x == 1:
                    if y == 0:
                        matrizJuego[3][0] = "v"
                    if y == 1:
                        matrizJuego[3][1] = "v"
                    if y == 2:
                        matrizJuego[3][2] = "v"
                    if y == 3:
                        matrizJuego[3][3] = "v"
                    if y == 4:
                        matrizJuego[3][4] = "v"
                if x == 2:
                    if y == 0:
                        matrizJuego[5][0] = "v"
                    if y == 1:
                        matrizJuego[5][1] = "v"
                    if y == 2:
                        matrizJuego[5][2] = "v"
                    if y == 3:
                        matrizJuego[5][3] = "v"
                    if y == 4:
                        matrizJuego[5][4] = "v"
                if x == 3:
                    if y == 0:
                        matrizJuego[7][0] = "v"
                    if y == 1:
                        matrizJuego[7][1] = "v"
                    if y == 2:
                        matrizJuego[7][2] = "v"
                    if y == 3:
                        matrizJuego[7][3] = "v"
                    if y == 4:
                        matrizJuego[7][4] = "v"
            if listaFacil[0][i][0] == "^":
                x = listaFacil[0][i][1]
                y = listaFacil[0][i][2]
                if x == 0:
                    if y == 0:
                        matrizJuego[1][0] = "^"
                    if y == 1:
                        matrizJuego[1][1] = "^"
                    if y == 2:
                        matrizJuego[1][2] = "^"
                    if y == 3:
                        matrizJuego[1][3] = "^"
                    if y == 4:
                        matrizJuego[1][4] = "^"
                if x == 1:
                    if y == 0:
                        matrizJuego[3][0] = "^"
                    if y == 1:
                        matrizJuego[3][1] = "^"
                    if y == 2:
                        matrizJuego[3][2] = "^"
                    if y == 3:
                        matrizJuego[3][3] = "^"
                    if y == 4:
                        matrizJuego[3][4] = "^"
                if x == 2:
                    if y == 0:
                        matrizJuego[5][0] = "^"
                    if y == 1:
                        matrizJuego[5][1] = "^"
                    if y == 2:
                        matrizJuego[5][2] = "^"
                    if y == 3:
                        matrizJuego[5][3] = "^"
                    if y == 4:
                        matrizJuego[5][4] = "^"
                if x == 3:
                    if y == 0:
                        matrizJuego[7][0] = "^"
                    if y == 1:
                        matrizJuego[7][1] = "^"
                    if y == 2:
                        matrizJuego[7][2] = "^"
                    if y == 3:
                        matrizJuego[7][3] = "^"
                    if y == 4:
                        matrizJuego[7][4] = "^"
            if listaFacil[0][i][0]!= "<" and listaFacil[0][i][0]!= ">" and listaFacil[0][i][0]!= "v" and listaFacil[0][i][0]!= "^":
                x = listaFacil[0][i][1]
                y = listaFacil[0][i][2]
                numero=listaFacil[0][i][0]
                if x == 0:
                    if y == 0:
                        matrizJuego[0][0] = int(numero)
                    if y == 1:
                        matrizJuego[0][2] = int(numero)
                    if y == 2:
                        matrizJuego[0][4] = int(numero)
                    if y == 3:
                        matrizJuego[0][6] = int(numero)
                    if y == 4:
                        matrizJuego[0][8] = int(numero)
                if x == 1:
                    if y == 0:
                        matrizJuego[2][0] = int(numero)
                    if y == 1:
                        matrizJuego[2][2] = int(numero)
                    if y == 2:
                        matrizJuego[2][4] = int(numero)
                    if y == 3:
                        matrizJuego[2][6] = int(numero)
                    if y == 4:
                        matrizJuego[2][8] = int(numero)
                if x == 2:
                    if y == 0:
                        matrizJuego[4][0] = int(numero)
                    if y == 1:
                        matrizJuego[4][2] = int(numero)
                    if y == 2:
                        matrizJuego[4][4] = int(numero)
                    if y == 3:
                        matrizJuego[4][6] = int(numero)
                    if y == 4:
                        matrizJuego[4][8] = int(numero)
                if x == 3:
                    if y == 0:
                        matrizJuego[6][0] = int(numero)
                    if y == 1:
                        matrizJuego[6][2] = int(numero)
                    if y == 2:
                        matrizJuego[6][4] = int(numero)
                    if y == 3:
                        matrizJuego[6][6] = int(numero)
                    if y == 4:
                        matrizJuego[6][8] = int(numero)
                if x == 4:
                    if y == 0:
                        matrizJuego[8][0] = int(numero)
                    if y == 1:
                        matrizJuego[8][2] = int(numero)
                    if y == 2:
                        matrizJuego[8][4] = int(numero)
                    if y == 3:
                        matrizJuego[8][6] = int(numero)
                    if y == 4:
                        matrizJuego[8][8] = int(numero)

        for i in range(len(matrizJuego)):
            for j in range(len(matrizJuego[i])):
                if matrizJuego[i][j]!=0 and matrizJuego[i][j]!=".":
                    if matrizJuego[i][j] == ">":
                        if i==0:
                            if j==1:
                                labelFlecha01.config(text=">")
                            if j==3:
                                labelFlecha02.config(text=">")
                            if j==5:
                                labelFlecha03.config(text=">")
                            if j==7:
                                labelFlecha04.config(text=">")
                        if i==2:
                            if j==1:
                                labelFlecha21.config(text=">")
                            if j==3:
                                labelFlecha22.config(text=">")
                            if j==5:
                                labelFlecha23.config(text=">")
                            if j==7:
                                labelFlecha24.config(text=">")
                        if i==4:
                            if j==1:
                                labelFlecha41.config(text=">")
                            if j==3:
                                labelFlecha42.config(text=">")
                            if j==5:
                                labelFlecha43.config(text=">")
                            if j==7:
                                labelFlecha44.config(text=">")
                        if i==6:
                            if j==1:
                                labelFlecha61.config(text=">")
                            if j==3:
                                labelFlecha62.config(text=">")
                            if j==5:
                                labelFlecha63.config(text=">")
                            if j==7:
                                labelFlecha64.config(text=">")
                        if i==8:
                            if j==1:
                                labelFlecha81.config(text=">")
                            if j==3:
                                labelFlecha82.config(text=">")
                            if j==5:
                                labelFlecha83.config(text=">")
                            if j==7:
                                labelFlecha84.config(text=">")
                    if matrizJuego[i][j] == "<":
                        if i==0:
                            if j==1:
                                labelFlecha01.config(text="<")
                            if j==3:
                                labelFlecha02.config(text="<")
                            if j==5:
                                labelFlecha03.config(text="<")
                            if j==7:
                                labelFlecha04.config(text="<")
                        if i==2:
                            if j==1:
                                labelFlecha21.config(text="<")
                            if j==3:
                                labelFlecha22.config(text="<")
                            if j==5:
                                labelFlecha23.config(text="<")
                            if j==7:
                                labelFlecha24.config(text="<")
                        if i==4:
                            if j==1:
                                labelFlecha41.config(text="<")
                            if j==3:
                                labelFlecha42.config(text="<")
                            if j==5:
                                labelFlecha43.config(text="<")
                            if j==7:
                                labelFlecha44.config(text="<")
                        if i==6:
                            if j==1:
                                labelFlecha61.config(text="<")
                            if j==3:
                                labelFlecha62.config(text="<")
                            if j==5:
                                labelFlecha63.config(text="<")
                            if j==7:
                                labelFlecha64.config(text="<")
                        if i==8:
                            if j==1:
                                labelFlecha81.config(text="<")
                            if j==3:
                                labelFlecha82.config(text="<")
                            if j==5:
                                labelFlecha83.config(text="<")
                            if j==7:
                                labelFlecha84.config(text="<")
                    if matrizJuego[i][j] == "v":
                        if i ==1:
                            if j==0:
                                labelFlecha11.config(text="v")
                            if j==1:
                                labelFlecha12.config(text="v")
                            if j==2:
                                labelFlecha13.config(text="v")
                            if j==3:
                                labelFlecha14.config(text="v")
                            if j==4:
                                labelFlecha15.config(text="v")
                        if i ==3:
                            if j==0:
                                labelFlecha31.config(text="v")
                            if j==1:
                                labelFlecha32.config(text="v")
                            if j==2:
                                labelFlecha33.config(text="v")
                            if j==3:
                                labelFlecha34.config(text="v")
                            if j==4:
                                labelFlecha35.config(text="v")
                        if i ==5:
                            if j==0:
                                labelFlecha51.config(text="v")
                            if j==1:
                                labelFlecha52.config(text="v")
                            if j==2:
                                labelFlecha53.config(text="v")
                            if j==3:
                                labelFlecha54.config(text="v")
                            if j==4:
                                labelFlecha55.config(text="v")
                        if i ==7:
                            if j==0:
                                labelFlecha71.config(text="v")
                            if j==1:
                                labelFlecha72.config(text="v")
                            if j==2:
                                labelFlecha73.config(text="v")
                            if j==3:
                                labelFlecha74.config(text="v")
                            if j==4:
                                labelFlecha75.config(text="v")
                    if matrizJuego[i][j] == "^":
                        if i ==1:
                            if j==0:
                                labelFlecha11.config(text="^")
                            if j==1:
                                labelFlecha12.config(text="^")
                            if j==2:
                                labelFlecha13.config(text="^")
                            if j==3:
                                labelFlecha14.config(text="^")
                            if j==4:
                                labelFlecha15.config(text="^")
                        if i ==3:
                            if j==0:
                                labelFlecha31.config(text="^")
                            if j==1:
                                labelFlecha32.config(text="^")
                            if j==2:
                                labelFlecha33.config(text="^")
                            if j==3:
                                labelFlecha34.config(text="^")
                            if j==4:
                                labelFlecha35.config(text="^")
                        if i ==5:
                            if j==0:
                                labelFlecha51.config(text="^")
                            if j==1:
                                labelFlecha52.config(text="^")
                            if j==2:
                                labelFlecha53.config(text="^")
                            if j==3:
                                labelFlecha54.config(text="^")
                            if j==4:
                                labelFlecha55.config(text="^")
                        if i ==7:
                            if j==0:
                                labelFlecha71.config(text="^")
                            if j==1:
                                labelFlecha72.config(text="^")
                            if j==2:
                                labelFlecha73.config(text="^")
                            if j==3:
                                labelFlecha74.config(text="^")
                            if j==4:
                                labelFlecha75.config(text="^")
                    if matrizJuego[i][j] != "^" and matrizJuego[i][j] != "v" and matrizJuego[i][j] != "<" and matrizJuego[i][j] != ">":
                        numero=matrizJuego[i][j]
                        print("a")
                        if i==0:
                            if j==0:
                                boton11.config(text=str(numero))
                            if j==2:
                                boton12.config(text=str(numero))
                            if j==4:
                                boton13.config(text=str(numero))
                            if j == 6:
                                boton14.config(text=str(numero))
                            if j==8:
                                boton15.config(text=str(numero))
                        if i==2:
                            if j==0:
                                boton21.config(text=str(numero))
                            if j==2:
                                boton22.config(text=str(numero))
                            if j==4:
                                boton23.config(text=str(numero))
                            if j == 6:
                                boton24.config(text=str(numero))
                            if j==8:
                                boton25.config(text=str(numero))
                        if i==4:
                            if j==0:
                                boton31.config(text=str(numero))
                            if j==2:
                                boton32.config(text=str(numero))
                            if j==4:
                                boton33.config(text=str(numero))
                            if j == 6:
                                boton34.config(text=str(numero))
                            if j==8:
                                boton35.config(text=str(numero))
                        if i==6:
                            if j==0:
                                boton41.config(text=str(numero))
                            if j==2:
                                boton42.config(text=str(numero))
                            if j==4:
                                boton43.config(text=str(numero))
                            if j == 6:
                                boton44.config(text=str(numero))
                            if j==8:
                                boton45.config(text=str(numero))
                        if i==8:
                            if j==0:
                                boton51.config(text=str(numero))
                            if j==2:
                                boton52.config(text=str(numero))
                            if j==4:
                                boton53.config(text=str(numero))
                            if j == 6:
                                boton54.config(text=str(numero))
                            if j==8:
                                boton55.config(text=str(numero))

    def actualizarMatriz():
        for i in range(len(matrizJuego)):
            for j in range(len(matrizJuego[i])):
                if matrizJuego[i][j]!=0 and matrizJuego[i][j]!=".":
                    if matrizJuego[i][j] == ">":
                        if i==0:
                            if j==1:
                                labelFlecha01.config(text=">")
                            if j==3:
                                labelFlecha02.config(text=">")
                            if j==5:
                                labelFlecha03.config(text=">")
                            if j==7:
                                labelFlecha04.config(text=">")
                        if i==2:
                            if j==1:
                                labelFlecha21.config(text=">")
                            if j==3:
                                labelFlecha22.config(text=">")
                            if j==5:
                                labelFlecha23.config(text=">")
                            if j==7:
                                labelFlecha24.config(text=">")
                        if i==4:
                            if j==1:
                                labelFlecha41.config(text=">")
                            if j==3:
                                labelFlecha42.config(text=">")
                            if j==5:
                                labelFlecha43.config(text=">")
                            if j==7:
                                labelFlecha44.config(text=">")
                        if i==6:
                            if j==1:
                                labelFlecha61.config(text=">")
                            if j==3:
                                labelFlecha62.config(text=">")
                            if j==5:
                                labelFlecha63.config(text=">")
                            if j==7:
                                labelFlecha64.config(text=">")
                        if i==8:
                            if j==1:
                                labelFlecha81.config(text=">")
                            if j==3:
                                labelFlecha82.config(text=">")
                            if j==5:
                                labelFlecha83.config(text=">")
                            if j==7:
                                labelFlecha84.config(text=">")
                    if matrizJuego[i][j] == "<":
                        if i==0:
                            if j==1:
                                labelFlecha01.config(text="<")
                            if j==3:
                                labelFlecha02.config(text="<")
                            if j==5:
                                labelFlecha03.config(text="<")
                            if j==7:
                                labelFlecha04.config(text="<")
                        if i==2:
                            if j==1:
                                labelFlecha21.config(text="<")
                            if j==3:
                                labelFlecha22.config(text="<")
                            if j==5:
                                labelFlecha23.config(text="<")
                            if j==7:
                                labelFlecha24.config(text="<")
                        if i==4:
                            if j==1:
                                labelFlecha41.config(text="<")
                            if j==3:
                                labelFlecha42.config(text="<")
                            if j==5:
                                labelFlecha43.config(text="<")
                            if j==7:
                                labelFlecha44.config(text="<")
                        if i==6:
                            if j==1:
                                labelFlecha61.config(text="<")
                            if j==3:
                                labelFlecha62.config(text="<")
                            if j==5:
                                labelFlecha63.config(text="<")
                            if j==7:
                                labelFlecha64.config(text="<")
                        if i==8:
                            if j==1:
                                labelFlecha81.config(text="<")
                            if j==3:
                                labelFlecha82.config(text="<")
                            if j==5:
                                labelFlecha83.config(text="<")
                            if j==7:
                                labelFlecha84.config(text="<")
                    if matrizJuego[i][j] == "v":
                        if i ==1:
                            if j==0:
                                labelFlecha11.config(text="v")
                            if j==1:
                                labelFlecha12.config(text="v")
                            if j==2:
                                labelFlecha13.config(text="v")
                            if j==3:
                                labelFlecha14.config(text="v")
                            if j==4:
                                labelFlecha15.config(text="v")
                        if i ==3:
                            if j==0:
                                labelFlecha31.config(text="v")
                            if j==1:
                                labelFlecha32.config(text="v")
                            if j==2:
                                labelFlecha33.config(text="v")
                            if j==3:
                                labelFlecha34.config(text="v")
                            if j==4:
                                labelFlecha35.config(text="v")
                        if i ==5:
                            if j==0:
                                labelFlecha51.config(text="v")
                            if j==1:
                                labelFlecha52.config(text="v")
                            if j==2:
                                labelFlecha53.config(text="v")
                            if j==3:
                                labelFlecha54.config(text="v")
                            if j==4:
                                labelFlecha55.config(text="v")
                        if i ==7:
                            if j==0:
                                labelFlecha71.config(text="v")
                            if j==1:
                                labelFlecha72.config(text="v")
                            if j==2:
                                labelFlecha73.config(text="v")
                            if j==3:
                                labelFlecha74.config(text="v")
                            if j==4:
                                labelFlecha75.config(text="v")
                    if matrizJuego[i][j] == "^":
                        if i ==1:
                            if j==0:
                                labelFlecha11.config(text="^")
                            if j==1:
                                labelFlecha12.config(text="^")
                            if j==2:
                                labelFlecha13.config(text="^")
                            if j==3:
                                labelFlecha14.config(text="^")
                            if j==4:
                                labelFlecha15.config(text="^")
                        if i ==3:
                            if j==0:
                                labelFlecha31.config(text="^")
                            if j==1:
                                labelFlecha32.config(text="^")
                            if j==2:
                                labelFlecha33.config(text="^")
                            if j==3:
                                labelFlecha34.config(text="^")
                            if j==4:
                                labelFlecha35.config(text="^")
                        if i ==5:
                            if j==0:
                                labelFlecha51.config(text="^")
                            if j==1:
                                labelFlecha52.config(text="^")
                            if j==2:
                                labelFlecha53.config(text="^")
                            if j==3:
                                labelFlecha54.config(text="^")
                            if j==4:
                                labelFlecha55.config(text="^")
                        if i ==7:
                            if j==0:
                                labelFlecha71.config(text="^")
                            if j==1:
                                labelFlecha72.config(text="^")
                            if j==2:
                                labelFlecha73.config(text="^")
                            if j==3:
                                labelFlecha74.config(text="^")
                            if j==4:
                                labelFlecha75.config(text="^")
                    if matrizJuego[i][j] != "^" and matrizJuego[i][j] != "v" and matrizJuego[i][j] != "<" and matrizJuego[i][j] != ">":
                        numero=matrizJuego[i][j]
                        if numero!=0:
                            if i==0:
                                if j==0:
                                    boton11.config(text=str(numero))
                                if j==2:
                                    boton12.config(text=str(numero))
                                if j==4:
                                    boton13.config(text=str(numero))
                                if j == 6:
                                    boton14.config(text=str(numero))
                                if j==8:
                                    boton15.config(text=str(numero))
                            if i==2:
                                if j==0:
                                    boton21.config(text=str(numero))
                                if j==2:
                                    boton22.config(text=str(numero))
                                if j==4:
                                    boton23.config(text=str(numero))
                                if j == 6:
                                    boton24.config(text=str(numero))
                                if j==8:
                                    boton25.config(text=str(numero))
                            if i==4:
                                if j==0:
                                    boton31.config(text=str(numero))
                                if j==2:
                                    boton32.config(text=str(numero))
                                if j==4:
                                    boton33.config(text=str(numero))
                                if j == 6:
                                    boton34.config(text=str(numero))
                                if j==8:
                                    boton35.config(text=str(numero))
                            if i==6:
                                if j==0:
                                    boton41.config(text=str(numero))
                                if j==2:
                                    boton42.config(text=str(numero))
                                if j==4:
                                    boton43.config(text=str(numero))
                                if j == 6:
                                    boton44.config(text=str(numero))
                                if j==8:
                                    boton45.config(text=str(numero))
                            if i==8:
                                if j==0:
                                    boton51.config(text=str(numero))
                                if j==2:
                                    boton52.config(text=str(numero))
                                if j==4:
                                    boton53.config(text=str(numero))
                                if j == 6:
                                    boton54.config(text=str(numero))
                                if j==8:
                                    boton55.config(text=str(numero))
                if matrizJuego[i][j] == 0:
                    if matrizJuego[i][j] != "^" and matrizJuego[i][j] != "v" and matrizJuego[i][j] != "<" and matrizJuego[i][j] != ">":
                        if i==0:
                            if j==0:
                                boton11.config(text=str(""))
                            if j==2:
                                boton12.config(text=str(""))
                            if j==4:
                                boton13.config(text=str(""))
                            if j == 6:
                                boton14.config(text=str(""))
                            if j==8:
                                boton15.config(text=str(""))
                        if i==2:
                            if j==0:
                                boton21.config(text=str(""))
                            if j==2:
                                boton22.config(text=str(""))
                            if j==4:
                                boton23.config(text=str(""))
                            if j == 6:
                                boton24.config(text=str(""))
                            if j==8:
                                boton25.config(text=str(""))
                        if i==4:
                            if j==0:
                                boton31.config(text=str(""))
                            if j==2:
                                boton32.config(text=str(""))
                            if j==4:
                                boton33.config(text=str(""))
                            if j == 6:
                                boton34.config(text=str(""))
                            if j==8:
                                boton35.config(text=str(""))
                        if i==6:
                            if j==0:
                                boton41.config(text=str(""))
                            if j==2:
                                boton42.config(text=str(""))
                            if j==4:
                                boton43.config(text=str(""))
                            if j == 6:
                                boton44.config(text=str(""))
                            if j==8:
                                boton45.config(text=str(""))
                        if i==8:
                            if j==0:
                                boton51.config(text=str(""))
                            if j==2:
                                boton52.config(text=str(""))
                            if j==4:
                                boton53.config(text=str(""))
                            if j == 6:
                                boton54.config(text=str(""))
                            if j==8:
                                boton55.config(text=str(""))


    def borrarJugada(): #eliminar jugada

        if len(listaJugadas)==0:
            mensaje2("No hay jugadas")
            return
        largo=len(listaJugadas)
        matrizJuego[listaJugadas[largo - 1][1]][listaJugadas[largo - 1][2]] = 0
        del listaJugadas[largo-1]
        actualizarMatriz()

    def borrarJuego(): #borrar tod0 el juego
        if activo[0] == 1:
            ventana1 = tkinter.Tk()  # Crea una ventana
            ventana1.geometry("300x100")
            ventana1.title("Futoshiki")  # Se le pone titulo parqueo
            Mensaje = tkinter.Label(ventana1, text=str("Terminar juego?"))  # Aqui va el mensaje
            Mensaje.place(x=80, y=20)
            def muestraVentana():
                ventana.destroy()
                ventana1.destroy()
                ventanaJugar()
            Boton = tkinter.Button(ventana1, text="No", command=ventana1.destroy)  # Boton de ok para salir
            Boton.place(x=160, y=60)
            Boton2 = tkinter.Button(ventana1, text="Si", command=muestraVentana)  # Boton de ok para salir
            Boton2.place(x=80,y=60)

    def eliminarJuego(): #eliminar juego
        if activo[0] == 1:
            ventana1 = tkinter.Tk()  # Crea una ventana
            ventana1.geometry("300x100")
            ventana1.title("Futoshiki")  # Se le pone titulo parqueo
            Mensaje = tkinter.Label(ventana1, text=str("Borrar juego?"))  # Aqui va el mensaje
            Mensaje.place(x=80, y=20)

            def muestraVentana():
                ventana1.destroy()
                for i in range(len(matrizJuego)):
                    for j in range(len(matrizJuego[i])):
                        if type(matrizJuego[i][j])==str:
                            if matrizJuego[i][j]!="." and matrizJuego[i][j]!="^" and matrizJuego[i][j]!="v" and matrizJuego[i][j]!="<" and matrizJuego[i][j]!=">":
                                matrizJuego[i][j]=0

                listaJugadas.clear()
                actualizarMatriz()

            Boton = tkinter.Button(ventana1, text="No", command=ventana1.destroy)  # Boton de ok para salir
            Boton.place(x=160, y=60)
            Boton2 = tkinter.Button(ventana1, text="Si", command=muestraVentana)  # Boton de ok para salir
            Boton2.place(x=80, y=60)

    def top10(): #mostrar top 10

        listaFa=[]
        listaMe=[]
        listaDi=[]
        archivo=open("futoshiki2021top10.dat","w")
        texto=archivo.readlines()
        for i in range(len(texto)):
            texto[i]=texto[i].rstrip("\n")
        for i in range(len(texto)):
            if texto[i]=="facil":
                listaFa.append(texto[i+1])
            if texto[i]=="medio":
                listaMe.append(texto[i+1])
            if texto[i]=="dificil":
                listaDi.append(texto[i+1])
        ventana1 = tkinter.Tk()
        ventana1.geometry("600x600")
        ventana1.title("Futoshiki")
        labelDificil=tkinter.Label(ventana1,text="Dificil")
        labelDificil.place(x=0,y=0)
        dificil=tkinter.Label(ventana1,text="")
        dificil.place(x=0,y=30)
        labelMedio = tkinter.Label(ventana1, text="Medio")
        labelMedio.place(x=200, y=0)
        medio = tkinter.Label(ventana1, text="")
        medio.place(x=200,y=30)
        labelFacil = tkinter.Label(ventana1, text="Facil")
        labelFacil.place(x=400, y=0)
        facil = tkinter.Label(ventana1, text="")
        facil.place(x=400,y=30)
        if len(listaFa)>=10:
            textFa=""
            for i in range(10):
                textFa=listaFa[i]+"\n"+textFa
        if len(listaFa)<10:
            textFa = ""
            for i in range(len(listaFa)):
                textFa = listaFa[i] + "\n" + textFa
        if len(listaMe)>=10:
            textMe=""
            for i in range(10):
                textMe=listaMe[i]+"\n"+textMe
        if len(listaMe)<10:
            textMe = ""
            for i in range(len(listaMe)):
                textMe = listaMe[i] + "\n" + textMe
        if len(listaDi)>=10:
            textDi=""
            for i in range(10):
                textDi=listaDi[i]+"\n"+textDi
        if len(listaDi)<10:
            textDi = ""
            for i in range(len(listaDi)):
                textDi = listaDi[i] + "\n" + textDi
        facil.config(text=textFa)
        medio.config(text=textMe)
        dificil.config(text=textDi)

    def guardarJuego(): #para cuando se guarda
        if activo[0]==1:
            archivo=open("futoshiki2021juegoactual.dat","w")
            archivo.writelines(str(configuracion[0])+"\n")
            archivo.writelines(str(nombre[0])+"\n")
            for i in range(len(matrizJuego)):
                for j in range(len(matrizJuego[i])):
                    if type(matrizJuego[i][j]) == int:
                        archivo.writelines(str(matrizJuego[i][j])+"a" + "\n")
                    else:
                        archivo.writelines(str(matrizJuego[i][j])+"\n")

    def cargarPartida(): #para cargar
        if activo[0]==0:
            archivo=open("futoshiki2021juegoactual.dat","r")
            texto=archivo.readlines()
            matriz=[]
            for i in range(len(texto)):
                texto[i]=texto[i].rstrip("\n")
            lista=[]
            lista.append(texto[2])
            lista.append(texto[3])
            lista.append(texto[4])
            lista.append(texto[5])
            lista.append(texto[6])
            lista.append(texto[7])
            lista.append(texto[8])
            lista.append(texto[9])
            lista.append(texto[10])
            matriz.append(lista)
            lista = []
            lista.append(texto[11])
            lista.append(texto[12])
            lista.append(texto[13])
            lista.append(texto[14])
            lista.append(texto[15])
            matriz.append(lista)
            lista = []
            lista.append(texto[16])
            lista.append(texto[17])
            lista.append(texto[18])
            lista.append(texto[19])
            lista.append(texto[20])
            lista.append(texto[21])
            lista.append(texto[22])
            lista.append(texto[23])
            lista.append(texto[24])
            matriz.append(lista)
            lista=[]
            lista.append(texto[25])
            lista.append(texto[26])
            lista.append(texto[27])
            lista.append(texto[28])
            lista.append(texto[29])
            matriz.append(lista)
            lista = []
            lista.append(texto[30])
            lista.append(texto[31])
            lista.append(texto[32])
            lista.append(texto[33])
            lista.append(texto[34])
            lista.append(texto[35])
            lista.append(texto[36])
            lista.append(texto[37])
            lista.append(texto[38])
            matriz.append(lista)
            lista = []

            lista.append(texto[39])
            lista.append(texto[40])
            lista.append(texto[41])
            lista.append(texto[42])
            lista.append(texto[43])
            matriz.append(lista)
            lista = []
            lista.append(texto[44])
            lista.append(texto[45])
            lista.append(texto[46])
            lista.append(texto[47])
            lista.append(texto[48])
            lista.append(texto[49])
            lista.append(texto[50])
            lista.append(texto[51])
            lista.append(texto[52])
            matriz.append(lista)
            lista = []
            lista.append(texto[53])
            lista.append(texto[54])
            lista.append(texto[55])
            lista.append(texto[56])
            lista.append(texto[57])
            matriz.append(lista)
            lista = []
            lista.append(texto[58])
            lista.append(texto[59])
            lista.append(texto[60])
            lista.append(texto[61])
            lista.append(texto[62])
            lista.append(texto[63])
            lista.append(texto[64])
            lista.append(texto[65])
            lista.append(texto[66])
            matriz.append(lista)
            if dificultad[0] == "facil":
                randon = random.randrange(0, 3)
                listaFacil[0] = listaFacil1[randon]

            if dificultad[0] == "medio":
                randon = random.randrange(0, 3)
                listaFacil[0] = listaMedio1[randon]

            if dificultad[0] == "dificil":
                randon = random.randrange(0, 3)
                listaFacil[0] = listaDificil1[randon]

            for i in range(len(matrizJuego)):
                for j in range(len(matrizJuego[i])):
                    if len(matriz[i][j])==2:
                        matrizJuego[i][j]=int(matriz[i][j][0])
                    else:
                        matrizJuego[i][j]=matriz[i][j]
            actualizarMatriz()
            activo[0]=1


    botonIniciarJuego=tkinter.Button(ventana,text="INICIAR JUEGO",width=12, height=3, borderwidth=1, relief="solid",bg='#ff0000',command=actualizar)
    botonIniciarJuego.place(x=70,y=520)

    botonBorrarJugada=tkinter.Button(ventana,text="BORRAR JUGADA",width=14,height=3,borderwidth=1, relief="solid",bg='#3B83BD',command=borrarJugada)
    botonBorrarJugada.place(x=180,y=520)

    botonTerminarJuego=tkinter.Button(ventana,text="TERMINAR JUEGO",width=14,height=3,borderwidth=1, relief="solid",bg = '#00BD2D',command=borrarJuego)
    botonTerminarJuego.place(x=300,y=520)

    botonBorrarJuego=tkinter.Button(ventana,text="BORRAR JUEGO",width=12,height=3,borderwidth=1, relief="solid",bg = '#2271b3',command=eliminarJuego)
    botonBorrarJuego.place(x=420,y=520)

    botonTop10=tkinter.Button(ventana,text="TOP 10",width=12,height=3,borderwidth=1, relief="solid",bg = '#ffff00',command=top10)
    botonTop10.place(x=530,y=520)

    botonGuardarJuego = tkinter.Button(ventana, text="GUARDAR JUEGO", width=12, height=2, borderwidth=1, relief="solid",command=guardarJuego)
    botonGuardarJuego.place(x=70, y=590)

    botonCargarJuego = tkinter.Button(ventana, text="CARGAR JUEGO", width=12, height=2, borderwidth=1, relief="solid",command=cargarPartida)
    botonCargarJuego.place(x=180, y=590)

    ventana.mainloop()

def ventanaConfigurar(): #configuracion
    ventana = tkinter.Tk()  # Se crea la ventana
    ventana.geometry("400x400")  # Tamanno de la ventana
    ventana.title("Futoshiki")  # Titulo
    titulo = tkinter.Label(ventana, text="Configuracion")
    titulo.place(x=0, y=0)
    labelNivel=tkinter.Label(ventana,text="Nivel")
    labelNivel.place(x=0,y=40)
    labelTimer=tkinter.Label(ventana,text="Timer")
    labelTimer.place(x=0,y=210)
    def facil():
        dificultad[0]="facil"
        listaFacil[0] = listaFacil1[randon]
    def medio():
        dificultad[0]="medio"
        listaFacil[0] = listaMedio1[randon]
    def dificil():
        dificultad[0]="dificil"
        listaFacil[0] = listaDificil1[randon]
    def si():
        timer[0]="si"
    def no():
        timer[0]="no"
    def volver():
        ventana.destroy()
        ventanaMenu()
    botonFacil=tkinter.Button(ventana,text="Facil",command=facil)
    botonFacil.place(x=20,y=70)
    botonMedio = tkinter.Button(ventana, text="Medio",command=medio)
    botonMedio.place(x=20,y=110)
    botonDificil = tkinter.Button(ventana, text="Dificil",command=dificil)
    botonDificil.place(x=20,y=150)
    botonSi=tkinter.Button(ventana,text="Si",command=si)
    botonSi.place(x=20,y=250)
    botonNo=tkinter.Button(ventana,text="No",command=no)
    botonNo.place(x=20,y=290)
    botonVolver=tkinter.Button(ventana,text="Volver",command=volver)
    botonVolver.place(x=200,y=340)
    ventana.mainloop()

def ventanaNombre():
    ventana = tkinter.Tk()  # Se crea la ventana
    ventana.geometry("400x250")  # Tamanno de la ventana
    ventana.title("Futoshiki")  # Titulo
    titulo = tkinter.Label(ventana, text="Nombre")
    titulo.place(x=30, y=20)
    nombr = tkinter.Entry(ventana)
    nombr.place(x=100, y=20)


    def listo():
        if len(nombr.get())>1 and (len(nombr.get())<20):
            nombre[0] = nombr.get()
            ventana.destroy()
            ventanaMenu()
        else:
            mensaje2("Escoja un nombre apropiado")

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