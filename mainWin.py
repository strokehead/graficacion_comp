from ctypes import sizeof
from struct import pack
import tkinter as tk
from typing_extensions import IntVar
from PIL import Image, ImageTk


winMain = tk.Tk()

winMain.state('zoomed')
winMain.title("Graficación por computadora")
winMain.geometry("1600x1000")
winMain.minsize(500,500)
# winMain.config(relief = "sunken")

#winMain.grid_rowconfigure(0, weight=3)
# winMain.grid_columnconfigure(0, weight=1)
# winMain.grid_columnconfigure(1, weight=2)
# winMain.grid_columnconfigure(2, weight=2)

titleW = tk.Label(winMain, text= "ALGORITMOS DE LÍNEA", font= "Arial 20")

# iconSquare   = tk.PhotoImage(file=r"icons/square.png")
iconSquare   = Image.open("icons/square.png")
iconSquare   = iconSquare.resize((20,20))
iconSquare   = ImageTk.PhotoImage(iconSquare)

# iconCircle   = tk.PhotoImage(file=r"icons/circle.png")
iconCircle   = Image.open("icons/circle.png")
iconCircle   = iconCircle.resize((20,20))
iconCircle   = ImageTk.PhotoImage(iconCircle)

# iconTriangle   = tk.PhotoImage(file=r"icons/triangle.png")
iconTriangle = Image.open("icons/triangle.png")
iconTriangle = iconTriangle.resize((20,20))
iconTriangle = ImageTk.PhotoImage(iconTriangle)

frameMain = tk.Frame(winMain)

buttonS = tk.Button(frameMain, image = iconSquare)
buttonC = tk.Button(frameMain, image = iconCircle)
buttonT = tk.Button(frameMain, image = iconTriangle)

frameMain.grid(row = 0, column = 0)
# frameMain.pack()
buttonS.grid(row = 0, column = 0)
buttonC.grid(row = 1, column = 0)
buttonT.grid(row = 2, column = 0)

winMain.mainloop()