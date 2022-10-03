from tkinter import *

class popup_sqo(Frame):
    def __init__(self, out_val:list, master: Tk, *args, **kargs):
        self.out = out_val
        super().__init__(master=master, *args, **kargs)
        self.top_level = Toplevel(master)
        #incluir botones para entradas, etc.
        Button(master = self.top_level, text='Aceptar', command=self.destroy).pack()
        self.top_level.protocol('MW_DELETE_WINDOW', self.destroy)
    
    def destroy(self):
        self.top_level.destroy()