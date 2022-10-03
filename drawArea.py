from tkinter import Canvas, mainloop
from pip import main
from tkinter import *

#from util.color import Color

'''clase para poder examinar color de 1 pixel en especifico'''

class ImageUtils:

    @staticmethod
    def get_pixels_of(canvas):
        width = int(canvas["width"])
        height = int(canvas["height"])
        colors = []

        for x in range(width):
            column = []
            for y in range(height):
                column.append(ImageUtils.get_pixel_color(canvas, x, y))
            colors.append(column)

        return colors

    @staticmethod
    def get_pixel_color(canvas, x, y):
        ids = canvas.find_overlapping(x, y, x, y)

        if len(ids) > 0:
            index = ids[-1]
            color = canvas.itemcget(index, "fill")
            color = color.upper()
            if color != '':
                return Color[color.upper()]

        return "WHITE"


'''clase para frame de canvas, dibujar, pintar'''
class drawA():
    def __init__(self, master : Tk, wd, ht):
        self.frame = Frame(master)
        self.canvas = Canvas(self.frame, width=wd, height=ht)
        self.frame.config(bg='white')
        self.canvas.config(bg='white')
        self.canvas.pack(side=TOP)
        self.frame.pack(side='top', fill='both', expand=True)
        pass

    def draw(self, li, col):
        for x in li:
            a = x[0]
            b = x[1]
            self.canvas.create_rectangle(a, b, 5, 5, fill=col)
        pass
    
    def paint(self, color, pos):
        '''if :
            self.canvas.create_line(pos[0], pos[1], pos[0]+1, pos[1], fill=color)
        '''
        pass