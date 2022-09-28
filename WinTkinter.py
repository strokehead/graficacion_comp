from ctypes import sizeof
import tkinter


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

titleW = tkinter.Label(win, text= "ALGORITMOS DE LÍNEA", font= "Arial 20")
#titleW.pack()
buttonE = tkinter.Button(win, text = "Ecuación cartesiana", font= "Helvetica 14", height= "2", width= "20")
#buttonE.pack()
buttonB = tkinter.Button(win, text = "De Bresenham", font= "Helvetica 14", height= "2", width= "20")
#buttonB.pack()

titleW.grid  (row = 0, column= 0, pady = (30,0))
buttonE.grid (row = 1, column= 0, pady = (70,20))
buttonB.grid (row = 2, column= 0)

win.mainloop()