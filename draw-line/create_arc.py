from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
canvas.create_rectangle(100,100,200,200)
canvas.create_arc(100,100,200,200,extent=359,style=ARC)