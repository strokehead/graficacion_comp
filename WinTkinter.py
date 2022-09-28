from ctypes import sizeof
import tkinter
from typing_extensions import IntVar


win = tkinter.Tk()
win.title("Graficación por computadora")
win.geometry("500x500")

def botonEc():
    winEc = tkinter.Toplevel()
    winEc.title("Algoritmo de ecuación cartesiana")
    winEc.geometry("400x400")

def botonBr():
    winBr = tkinter.Toplevel()
    winBr.title("Algoritmo de Bresenham")
    winBr.geometry("400x400")
    

#win.grid_rowconfigure(0, weight=3)
win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=2)
win.grid_columnconfigure(2, weight=2)

titleW = tkinter.Label(win, text= "ALGORITMOS DE LÍNEA", font= "Arial 20")

lblP1 = tkinter.Label(win, text= "Punto 1", font= "Helvetica 10")
lblP2 = tkinter.Label(win, text= "Punto 2", font= "Helvetica 10")

valueX1 = tkinter.IntVar()
valueY1 = tkinter.IntVar()
valueX2 = tkinter.IntVar()
valueY2 = tkinter.IntVar()

entryX1 = tkinter.Entry(win, textvariable=valueX1)
entryY1 = tkinter.Entry(win, textvariable=valueY1)
entryX2 = tkinter.Entry(win, textvariable=valueX2)
entryY2 = tkinter.Entry(win, textvariable=valueY2)

buttonE = tkinter.Button(win, text = "Ecuación cartesiana", font= "Helvetica 14", height= "2", width= "20")
buttonB = tkinter.Button(win, text = "De Bresenham", font= "Helvetica 14", height= "2", width= "20")

#titleW.grid  (row = 0, column= 0, columnspan=2, pady = (30,0))
titleW.grid  (row = 0, column= 0, columnspan=3, pady = (30,10))#, sticky=tkinter.EW)

lblP1.grid  (row= 1, column= 0)
entryX1.grid(row= 1, column= 1, sticky='E')
entryY1.grid(row= 1, column= 2, sticky='W')
lblP2.grid  (row= 2, column= 0)
entryX2.grid(row= 2, column= 1, sticky='E')
entryY2.grid(row= 2, column= 2, sticky='W')

buttonE.grid (row = 3, column= 0, columnspan=3, pady = (70,20))
buttonB.grid (row = 4, column= 0, columnspan=3)
#frame.place(relx)

win.mainloop()