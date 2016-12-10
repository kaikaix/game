from tkinter import *
tk=Tk()
canvas=Canvas(tk,width=550,height=550)
canvas.pack()
canvas.create_text(150,100,text="WORD1")
canvas.create_text(150,300,text="WORD2",fill='red')
canvas.create_text(150,500,text="WORD",fill='yellow',font=('Courier',30))


