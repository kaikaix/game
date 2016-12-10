from tkinter import *
from time import sleep
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_rectangle(10,10,50,50)
sleep(10)
