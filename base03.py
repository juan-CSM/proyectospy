#!/usr/bin/env python

import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

import tkinter as Tk
import sys

def destroy(e): sys.exit()

root = Tk.Tk()
root.wm_title("Embedding in TK")
#root.bind("<Destroy>", destroy)


f = plt.Figure()
def grafica():
    ax=f.add_subplot(111)
    ax.plot([1,2,3,4,5], [2,3,4,5,6])
    canvas.draw()

# a tk.DrawingArea
canvas = FigureCanvasTkAgg(f, master=root)

canvas.get_tk_widget().pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk( canvas, root )
toolbar.update()
canvas._tkcanvas.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)

button = Tk.Button(master=root, text='graficar', command=grafica)
button.pack(side=Tk.TOP)
button = Tk.Button(master=root, text='salir', command=sys.exit)
button.pack(side=Tk.TOP)

Tk.mainloop()
