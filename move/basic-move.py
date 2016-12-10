import time
from tkinter import *
tk = Tk()
canvas=Canvas(tk,width=400,height=200)
canvas.pack()
id=canvas.create_polygon(10,10,10,60,50,35)
for x in range(0,60):
	canvas.move(id,5,1)
	tk.update()
	time.sleep(0.05)

