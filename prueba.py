import tkinter
import random
import time
from tkinter import ttk
from tkinter import *

def ventanaprincipal():
    
    ventana_principal = tkinter.Toplevel()
    ventana_principal.geometry("1200x950")
    ventana_principal.configure(bg="spring green")
    ventana_principal.title("MEMORAMA")

def registrar():
    global nombre_usuario
    nombre_usuario = entry_usuario.get()
    print("Usuario registrado:", nombre_usuario)
    ventana_registro.withdraw()  # Ocultamos la ventana de registro
    ventanaprincipal()  # Abrimos la ventana principal

ventana_registro = tkinter.Tk()
ventana_registro.geometry("300x150")
ventana_registro.configure(bg="spring green")
ventana_registro.title("Registro de Usuario")

label_usuario = tkinter.Label(ventana_registro, text="Nombre de Usuario:")
label_usuario.pack()

entry_usuario = tkinter.Entry(ventana_registro)
entry_usuario.pack()

boton_registrar = tkinter.Button(ventana_registro, text="Registrar", command=registrar)
boton_registrar.pack()


def repetir_juego():
    tabla.destroy()
    lblfelicidades.destroy()
    
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


#etiqueta que muestra los intentos hechos por el usuario
repertir=tkinter.Button(ventana,text="Play again",font=("verdana",16),bg="#CB0000",fg="white", command=repetir_juego())
repertir.place(x=1040,y=450)

ventana_registro.mainloop()
