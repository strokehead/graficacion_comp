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
winMain.geometry("1000x800")
winMain.minsize(500,500)

#winMain.grid_rowconfigure(0, weight=3)
# winMain.grid_columnconfigure(0, weight=1)
# winMain.grid_columnconfigure(1, weight=2)
# winMain.grid_columnconfigure(2, weight=2)

titleW = tk.Label(winMain, text= "ALGORITMOS DE LÍNEA", font= "Arial 20")

iconSquare   = iconR("square")
iconCircle   = iconR("circle")
iconTriangle = iconR("triangle")

menus = tk.Menu()
menuArchive = tk.Menu(menus, tearoff = False)
menuArchive.add_command(
    label = "Nuevo",
    # command=
)
menuArchive.add_command(
    label = "Guardar",
    # command=
)

menuArchive.add_separator()
menuArchive.add_command(label = "Salir", command = winMain.destroy)

menuOptions = tk.Menu(menus, tearoff = False)

menus.add_cascade(menu = menuArchive, label = "Archivo")
menus.add_cascade(menu = menuOptions, label = "Opciones")

winMain.config(menu = menus)

frameMenu    = tk.Frame(winMain, height = 20, relief = "raised", borderwidth = 1)
frameButtons = tk.Frame(winMain, width  = 30, relief = "raised", borderwidth = 1)

buttonS = tk.Button(frameButtons, image = iconSquare)
buttonC = tk.Button(frameButtons, image = iconCircle)
buttonT = tk.Button(frameButtons, image = iconTriangle)

frameMenu.grid(row = 0, column = 0)
frameButtons.grid(row = 1, column = 0)

buttonS.grid(row = 0, column = 0, padx = (0,3), pady = (3,3))
buttonC.grid(row = 1, column = 0, padx = (0,3), pady = (3,3))
buttonT.grid(row = 2, column = 0, padx = (0,3), pady = (3,3))

winMain.mainloop()