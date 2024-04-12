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

ventana_registro.mainloop()
