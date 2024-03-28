from tkinter import *

ventanaprincipal = Tk()
ventanaprincipal.title("Registrate")
ventanaprincipal.minsize(width=300,height=400)
ventanaprincipal.config(padx=35, pady=35)
ventanaprincipal.configure(bg="spring green")

etiqueta1 = Label(text="Bienvenido al english day", font=("arial",14),bg="spring green")
etiqueta1.grid(column=0, row=1)

vertical_space = Label(text="", height=2,bg="spring green")
vertical_space.grid(column=0, row=2)

etiqueta2 = Label(text="Crea tu nombre de usuario", font=("arial",14),bg="spring green")
etiqueta2.grid(column=0, row=3)

vertical_space = Label(text="", height=1, bg="spring green")
vertical_space.grid(column=0, row=4)

nombre = Entry(width=20,font=("Arial",14))
nombre.grid(column=0, row=5)


ventanaprincipal.mainloop()