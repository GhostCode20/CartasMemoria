#importamos los módulos que necesitarémos random para barajear las imágenes
import tkinter
import random
import time
from tkinter import ttk
from tkinter import *
#from sesión import nombre_jugador

#creamos la ventana y la configuramos    s
ventana = tkinter.Tk()
ventana.geometry("1200x950")
ventana.configure(bg="#2988BC")
#ventana.resizable(0,0)
ventana.title("Encuentra la pareja")
#ventana.iconbitmap("imagenes_memorama/recordar.ico")

#cargamos las imágenes del memorama
imagen0=tkinter.PhotoImage(file="imagenes_memorama/dollar.png")
imagen1=tkinter.PhotoImage(file="imagenes_memorama/gta.png")
imagen2=tkinter.PhotoImage(file="imagenes_memorama/lakers.png")
imagen3=tkinter.PhotoImage(file="imagenes_memorama/bandera.png")
imagen4=tkinter.PhotoImage(file="imagenes_memorama/libertad.png")
imagen5=tkinter.PhotoImage(file="imagenes_memorama/mcdonalds.png")

#imagen de las tapas de las cartas
imapreg=tkinter.PhotoImage(file="imagenes_memorama/interrogante.png")

#ponemos las imagenes en un arreglo
imagenes=[imagen0,imagen1,imagen2,imagen3,imagen4,imagen5,imagen0,imagen1,imagen2,imagen3,imagen4,imagen5]

#barajeamos las imágenes del memorama con fisher-yates
def shuffle(arr):
    last_index = len(arr)-1
    while last_index > 0:
        rand_index = random.randint(0, last_index)
        temp = arr[last_index]
        arr[last_index] = arr[rand_index]
        arr[rand_index] = temp
        last_index -= 1
    return arr

def reiniciar_juego():
    global contador_gana, posiciones, emparejados, intentos, puntaje,barajeado
    contador_gana = 0
    posiciones = [None, None]
    emparejados = []
    intentos = 0
    puntaje = 0
    barajeado=shuffle(imagenes)
    for i in range(12):
        botones[i].config(image=imapreg)
    #SALUDO
    saludo2=tkinter.Label(ventana,text=" Welcome to the English day ",font=("verdana",24),bg="#CB0000",fg="white",wraplength=250)
    saludo2.place(x=965,y=100)

    #etiqueta que muestra los intentos hechos por el usuario
    etiqueta_intentos=tkinter.Label(ventana,text=" Attemps : "+str(intentos),font=("verdana",18),bg="#CB0000",fg="white")
    etiqueta_intentos.place(x=965,y=350)

    #etiqueta que muestra los intentos hechos por el usuario
    etiqueta_puntaje=tkinter.Label(ventana,text=" Score : "+str(puntaje),font=("verdana",18),bg="#CB0000",fg="white")
    etiqueta_puntaje.place(x=965,y=300)

    etiqueta_intentos.destroy()
    etiqueta_puntaje.destroy()
    saludo.destroy()
    tabla.destroy()
    lblfelicidades.destroy()

#TERMINA REINICIO
#TERMINA REINICIO
#TERMINA REINICIO

#mandamos a llamar la función de barajeo y obtenemos nuestras imagenes barajeadas
barajeado=shuffle(imagenes)

resta=0
puntaje=0
#intentos para que tome los intentos que le está tomando al usuario
intentos=0

#SALUDO
saludo=tkinter.Label(ventana,text=" Welcome to the English day ",font=("verdana",24),bg="#CB0000",fg="white",wraplength=250)
saludo.place(x=965,y=100)

#etiqueta que muestra los intentos hechos por el usuario
etiqueta_intentos=tkinter.Label(ventana,text=" Attemps : "+str(intentos),font=("verdana",18),bg="#CB0000",fg="white")
etiqueta_intentos.place(x=965,y=350)

#etiqueta que muestra puntaje del usuario
etiqueta_puntaje=tkinter.Label(ventana,text=" Score : "+str(puntaje),font=("verdana",18),bg="#CB0000",fg="white")
etiqueta_puntaje.place(x=965,y=300)

#etiqueta que muestra botón reinicio
reinicio=tkinter.Button(ventana,text="Reset",font=("verdana",16),bg="#CB0000",fg="white", command=reiniciar_juego)
reinicio.place(x=1020,y=450)

#creamos los 12 botones configurados, lo más importante es el argumento que
#le pasamos a eleccion que es la posicion que va a ser comparada en nuestro array barajeado

podio=[]
botones=[]
for i in range (12):
    boton=tkinter.Button(ventana,image=imapreg,width="180",height="180",bg="#F4EADE",command=lambda numelec=i:eleccion(numelec))
    botones.append(boton)

#variable para recorrer los botones y colocarlos
c=0

for x in range(3):
    for y in range(4):

        botones[c].grid(row=x,column=y,padx=25,pady=25)
        c+=1

miFrame=tkinter.Frame(ventana,background="gold")

#contadr_elec para que cuente los dos clickeo por turno
contador_elec=0
#contador_gana si empareja 6 pares
contador_gana=0
#posiciones va a tomar las posiciones de las cartas que se mandan desde lambda y así poder comparar las cartas de las posiciones de las cartas en el array barajeado
posiciones=[None,None]
#guarda las posiciones de las cartas emparejadas, para así no provocar un error con los contadores
emparejados=[]

def eleccion(n):
    #declaramos las variables globales para que funcionen fuera de la función
    global contador_gana,posiciones,emparejados,intentos,ventana,miFrame,puntaje,resta,registro
    #si se seleccionó una imagen de las que ya está acertada (emparejada) no hace nada
    if n in emparejados:
        pass
    else:
        #si no se ha seleccionado ninguna carta en estos 2 clickeo por turno del usuario lo que hacemos es...
        if posiciones[0]==None:
            #cambiamos la imagen que tenía como tapa en el botón
            botones[n].config(image=barajeado[n])
            #agregamos la posición del primer botón seleccionado de los 2 clickeo por turno para después comparar esa posicion con la posicion del siguiente botón
            #en el arreglo barajeado
            posiciones[0]=n
        #si ya ha seleccionado 1 botón    
        elif(posiciones[0]!=None):
            #si n es decir la posicion pasada desde el botón como argumento es igual a la de este segundo intento no hace nada
            if posiciones[0]==n:
                pass
            #si la segunda posición del clickeo por turno es distinta al primero 
            elif(posiciones[0]!=n):
                #guardamos la posición del botón de este segundo clickeo por turno
                posiciones[1]=n
                #cambiamos la imágen del botón este segundo clickeo por turno
                botones[n].config(image=barajeado[n])
                #refrescamos para que se vean los cambios en la interfaz
                ventana.update()
                #comparamos las dos posiciones de los dos clickeo por turno
                #si coinciden las imagenes en las dos posiciones de los dos clickeos por turno en el arreglo barajeado
                if barajeado[posiciones[0]]==barajeado[posiciones[1]]:
                    #acerto un par, aumenta contador_gana
                    contador_gana+=1
                    #guardamos las posiciones que emparejamos
                    emparejados.append(posiciones[0])
                    emparejados.append(posiciones[1])
                    #limpiamos las posiciones para el siguiente turno
                    posiciones=[None,None]
                    #aumentamos los intentos
                    intentos+=1
                    #puntaje aumentar
                    puntaje -=resta
                    puntaje+=50
                    #cambiamos la etiqueta_intentos con el texto de la variable intentos
                    etiqueta_intentos.config(text=" attemps : "+str(intentos))
                    etiqueta_puntaje.config(text=" score : "+str(puntaje))
                else:
                    #si no coincidieron las imagenes espera para cambiar las imagenes en los botones en las posiciones que no eran iguales las imagenes
                    time.sleep(0.25)
                    #cambiamos las imagenes a la imagen incógnita imapreg
                    botones[posiciones[0]].config(image=imapreg)
                    botones[posiciones[1]].config(image=imapreg)
                    #borramos las posiciones para el siguiente turno
                    posiciones=[None,None]
                    #aumentamos los intentos
                    intentos+=1
                    #operacionm
                    puntaje -=resta
                    puntaje -=10
                    #cambiamos la etiqueta_intentos con el texto de la variable intentos
                    etiqueta_intentos.config(text="Attemps : "+str(intentos))
                    etiqueta_puntaje.config(text=" Score : "+str(puntaje))

    #si acierta los 6 pares el usuario ganó      
    if contador_gana==6:
        #espera para destruir los widgets
        time.sleep(1)
        #destruye los botones
        for i in range(12):
            botones[i].destroy()
        #muestra un mensaje en una etiqueta
        global tabla,lblfelicidades
        lblfelicidades = tkinter.Label(ventana,text=" ¡¡Congratulations!! ", font=("verdana",50),fg="white",bg="#CB0000")
        lblfelicidades.place(x=240,y=200)
        tabla = ttk.Treeview(ventana,columns =("columna1","columna2"))
        tabla.column("#0", width=50)
        tabla.grid(row=0, column=0, padx=450, pady=350, sticky="nsew")
        #columna
        tabla.column("#0", width=50)
        tabla.column("columna1", width=80)
        tabla.column("columna2", width=80)
        #cabeza de columna
        tabla.heading("#0", text="Puesto")
        tabla.heading("columna1", text="Nombre")
        tabla.heading("columna2", text="Puntaje")
        tabla.insert("",END,text="1",values=("shary",puntaje))
        
        # Ordenar los datos por puntaje de mayor a menor
        #podio = sorted(podio, key=lambda x: x[1], reverse=True)

ventana.mainloop()
