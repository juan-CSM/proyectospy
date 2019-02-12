#!/usr/bin/env python3

import distancia as miprog
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

import tkinter as Tk
import sys
from matplotlib import style
style.use('fivethirtyeight')
from mpl_toolkits.mplot3d import Axes3D



def infoprog():
    informacionPrograma = 'Programa que busca el punto medio entre 2 puntos)'
    Tk.messagebox.showinfo('Info del programa',informacionPrograma)

def infoprogramador():
    informacionProgramador = 'por: Juan Carlos'
    Tk.messagebox.showinfo('Info del programador',informacionProgramador)

root = Tk.Tk()
root.title("Ventana que incluye una grafica")
root.geometry("600x650")

barramenu = Tk.Menu(root)
menuopcion = Tk.Menu(barramenu)
menuopcion.add_command(label="Salir", command=sys.exit)
barramenu.add_cascade(label='opciones', menu = menuopcion)
menuinfo = Tk.Menu(barramenu)
menuinfo.add_command(label='programa', command=infoprog)
menuinfo.add_command(label='desarrollador',command=infoprogramador)
barramenu.add_cascade(label='informacion',menu=menuinfo)
root.config(menu=barramenu)


#variables de entrada
p1x = Tk.DoubleVar()
p2x = Tk.DoubleVar()
p1y = Tk.DoubleVar()
p2y = Tk.DoubleVar()
p1z = Tk.DoubleVar()
p2z = Tk.DoubleVar()
px = Tk.DoubleVar()
py = Tk.DoubleVar()
pz = Tk.DoubleVar()


f = plt.Figure(figsize=(6,4))
def grafica():
    x1, y1, z1 = p1x.get(), p1y.get(), p1z.get()
    x2, y2, z2 = p2x.get(), p2y.get(), p2z.get()
    x0, y0, z0 = px.get(), py.get(), pz.get()
    a = np.array([x1,y1,z1])
    b = np.array([x2,y2,z2])
    c = np.array([x0,y0,z0])
    ax = f.add_subplot(111, projection = '3d')
    vectores = miprog.findpm(a,b,c)
    respmedio = vectores[3]
    mostrarResultado.configure(text = str(respmedio))
    for i in vectores:
        ax.scatter(i[0],i[1],i[2])
    ax.set_title("Punto medio")
    canvas.draw()

def borra():
    entradaX0.delete(0,Tk.END)
    entradaX0.insert(0,0)
    entradaY0.delete(0,Tk.END)
    entradaY0.insert(0,0)
    entradaZ0.delete(0,Tk.END)
    entradaZ0.insert(0,0)
    entradaX1.delete(0,Tk.END)
    entradaX1.insert(0,0)
    entradaY1.delete(0,Tk.END)
    entradaY1.insert(0,0)
    entradaZ1.delete(0,Tk.END)
    entradaZ1.insert(0,0)
    entradaX2.delete(0,Tk.END)
    entradaX2.insert(0,0)
    entradaY2.delete(0,Tk.END)
    entradaY2.insert(0,0)
    entradaZ2.delete(0,Tk.END)
    entradaZ2.insert(0,0)
    mostrarResultado.configure(text = '')

def pordef():
    entradaX0.delete(0,Tk.END)
    entradaX0.insert(0,1)
    entradaY0.delete(0,Tk.END)
    entradaY0.insert(0,1)
    entradaZ0.delete(0,Tk.END)
    entradaZ0.insert(0,0)
    entradaX1.delete(0,Tk.END)
    entradaX1.insert(0,0)
    entradaY1.delete(0,Tk.END)
    entradaY1.insert(0,0)
    entradaZ1.delete(0,Tk.END)
    entradaZ1.insert(0,0)
    entradaX2.delete(0,Tk.END)
    entradaX2.insert(0,2)
    entradaY2.delete(0,Tk.END)
    entradaY2.insert(0,0)
    entradaZ2.delete(0,Tk.END)
    entradaZ2.insert(0,0)

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().place(x = 2, y = 2)

#toolbar = NavigationToolbar2Tk( canvas, root )
#toolbar.update()
#canvas._tkcanvas.pack(side=Tk.BOTTOM, fill=Tk.BOTH)

etp1 = Tk.Label(root, text = 'coordenadas del punto 1')
etp1.place(x = 45 ,y = 410)

etp1X = Tk.Label(root,text = 'x')
etp1X.place(x = 60,y = 440)

entradaX1 = Tk.Entry(master = root, text = '0', textvariable = p1x, width = 7)
entradaX1.place(x = 100, y = 440)

etp1Y = Tk.Label(root,text = 'y')
etp1Y.place(x = 160,y = 440)

entradaY1 = Tk.Entry(master = root, text = '0', textvariable = p1y, width = 7)
entradaY1.place(x = 200, y = 440)

etp1Z = Tk.Label(root,text = 'z')
etp1Z.place(x = 260,y = 440)

entradaZ1 = Tk.Entry(master = root, text = '0', textvariable = p1z, width = 7)
entradaZ1.place(x = 300, y = 440)

etp2 = Tk.Label(root, text = 'coordenadas del punto 2')
etp2.place(x = 45 ,y = 460)

etp2X = Tk.Label(root,text = 'x')
etp2X.place(x = 60 ,y = 490)

entradaX2 = Tk.Entry(master = root, text = '2', textvariable = p2x, width = 7)
entradaX2.place(x = 100, y = 490)

etp2Y = Tk.Label(root,text = 'y')
etp2Y.place(x = 160,y = 490)

entradaZ2 = Tk.Entry(master = root, text = '0', textvariable = p2y, width = 7)
entradaZ2.place(x = 200, y = 490)

etp2Z = Tk.Label(root,text = 'z')
etp2Z.place(x = 260,y = 490)

entradaY2 = Tk.Entry(master = root, text = '0', textvariable = p2z, width = 7)
entradaY2.place(x = 300, y = 490)

etp0 = Tk.Label(root, text = 'coordenadas tentativas del punto medio')
etp0.place(x = 45 ,y = 510)

etp0X = Tk.Label(root,text = 'x')
etp0X.place(x = 60,y = 540)

entradaX0 = Tk.Entry(master = root, text = '1', textvariable = px, width = 7)
entradaX0.place(x = 100, y = 540)

etp0Y = Tk.Label(root,text = 'y')
etp0Y.place(x = 160,y = 540)

entradaY0 = Tk.Entry(master = root, text = '1', textvariable = py, width = 7)
entradaY0.place(x = 200, y = 540)

etp0Z = Tk.Label(root,text = 'z')
etp0Z.place(x = 260,y = 540)

entradaZ0 = Tk.Entry(master = root, text = '1', textvariable = pz, width = 7)
entradaZ0.place(x = 300, y = 540)


buttonGraf = Tk.Button(master=root, text='graficar', command=grafica)
buttonGraf.place(x = 10,y = 580)
buttonSal = Tk.Button(master=root, text='salir', command=sys.exit)
buttonSal.place(x = 100, y = 580)

buttonBorra = Tk.Button(master = root, text = 'Borrar', command=borra)
buttonBorra.place(x = 190, y = 580)

buttonPordef = Tk.Button(master = root, text = 'default', command=pordef)
buttonPordef.place(x = 280, y = 580)

mostrarResultado = Tk.Label(root, text = '')
mostrarResultado.place(x = 400, y = 580)

Tk.mainloop()
