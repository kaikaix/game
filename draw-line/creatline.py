from tkinter import *
import time

tk = Tk()
canvas = Canvas(tk,height=500,width=500)
canvas.pack()
canvas.create_line(0,0,500,500)#(0,0) is first coordinate (500,500) is last
time.sleep(10)