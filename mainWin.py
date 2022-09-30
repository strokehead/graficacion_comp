from ctypes import sizeof
from struct import pack
import tkinter as tk
from typing_extensions import IntVar
from PIL import Image, ImageTk

def iconR(nameIcon):
    dir = "icons/{}.png".format(nameIcon)
    icon = Image.open(dir)
    icon = icon.resize((20,20))
    icon = ImageTk.PhotoImage(icon)
    return icon

winMain = tk.Tk()

# winMain.state('zoomed')
winMain.title("Graficación por computadora")
# winMain.geometry("1600x1000")
winMain.geometry("1000x800")
winMain.minsize(500,500)
# winMain.config(relief = "sunken")

#winMain.grid_rowconfigure(0, weight=3)
# winMain.grid_columnconfigure(0, weight=1)
# winMain.grid_columnconfigure(1, weight=2)
# winMain.grid_columnconfigure(2, weight=2)

titleW = tk.Label(winMain, text= "ALGORITMOS DE LÍNEA", font= "Arial 20")

# iconSquare   = tk.PhotoImage(file=r"icons/square.png")
iconSquare   = iconR("square")

# iconCircle   = tk.PhotoImage(file=r"icons/circle.png")
iconCircle   = iconR("circle")

# iconTriangle   = tk.PhotoImage(file=r"icons/triangle.png")
iconTriangle = iconR("triangle")

frameMenu    = tk.Frame(winMain, height = 20)
frameButtons = tk.Frame(winMain, width  = 30, bg = "gray", relief = "solid", highlightcolor = "gray", highlightthickness = 1)
# frameButtons.config(relief="solid")
# frameButtons.config(bd = 1, )
# frameButtons.config(wi)

buttonS = tk.Button(frameButtons, image = iconSquare)
buttonC = tk.Button(frameButtons, image = iconCircle)
buttonT = tk.Button(frameButtons, image = iconTriangle)

frameMenu.grid(row = 0, column = 0)
frameButtons.grid(row = 1, column = 0)
# frameButtons.pack()
buttonS.grid(row = 0, column = 0, padx = (0,3))
buttonC.grid(row = 1, column = 0, padx = (0,3))
buttonT.grid(row = 2, column = 0, padx = (0,3))

winMain.mainloop()