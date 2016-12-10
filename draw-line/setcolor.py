from tkinter import *
from random import randrange
import time

tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()

colors = ['green','red','yellow','gold']

for color in colors:
    x1 = randrange(400)
    y1 = randrange(400)
    x2 = randrange(400)
    y2 = randrange(400)
    canvas.create_rectangle(x1,y1,x2,y2,fill=color)
    time.sleep(1)