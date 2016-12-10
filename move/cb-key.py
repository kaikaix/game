from tkinter import *
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
id=canvas.create_polygon(10,10,10,60,50,35)
def movebykey(event):
	key=event.keysym
	if key=="Up":
		canvas.move(id,0,-3)
	elif key == "Down":
		canvas.move(id,0,3)
	elif key == "Left":
		canvas.move(id,-3,0)
	else:
		canvas.move(id,3,0)

allkey = ['<KeyPress-Up>','<KeyPress-Down>','<KeyPress-Left>','<KeyPress-Right>']

for key in allkey:
	canvas.bind_all(key,movebykey)


