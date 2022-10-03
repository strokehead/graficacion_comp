import tkinter

master=tkinter.Tk()
master.title("pack() method")
master.geometry("450x350")

fr = tkinter.Frame(master=master)

button1=tkinter.Button(fr, text="LEFT")
button1.pack(side=tkinter.LEFT)

button2=tkinter.Button(fr, text="RIGHT")
button2.pack(side=tkinter.LEFT)

button3=tkinter.Button(fr, text="TOP")
button3.pack(side=tkinter.LEFT)

button4=tkinter.Button(fr, text="BOTTOM")
button4.pack(side=tkinter.LEFT)

fr.pack(side=tkinter.RIGHT)

master.mainloop()
