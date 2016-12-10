from tkinter import *
import random
import time

tk = Tk()
tk.title('Game')
tk.resizable(0,0)#disallow move window
tk.wm_attributes('-topmost',1)#the first window
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.y=-3
        self.x = starts[0]
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.yspeed = 1
        self.xspeed = 3

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = self.yspeed
        elif pos[3] >= self.canvas_height:
            self.y = -self.yspeed
        if pos[2] >= self.canvas_width:
            self.x = -self.xspeed
        elif pos[0] <=0:
            self.x = self.xspeed

class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn)
        self.canvas.bind_all("<KeyPress-Right>",self.turn)
        self.xspeed = 2
        self.x = 0

    def turn(self,evt):
        if evt.keysym == "Left":
            self.x = -self.xspeed
        else:
            self.x = self.xspeed

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
point = 0
word_id = canvas.create_text(100,20,text="You get %d point(s)"%point,fill="blue",font=('Courier',10))

class Middle:
    def __init__(self,ball,paddle,canvas):
        self.ball = ball
        self.paddle = paddle
        self.canvas = canvas
        
    def check(self):
        global point
        global word_id

        paddle_pos = self.canvas.coords(self.paddle.id)
        ball_pos = self.canvas.coords(self.ball.id)
        if ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2]:
            if ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]:
                ball.y = -ball.yspeed
                point+=1
                self.canvas.itemconfig(word_id,text="You get %d point(s)"%point)
    
    def hit_bottom(self):
        paddle_pos = self.canvas.coords(self.paddle.id)
        ball_pos = self.canvas.coords(self.ball.id)
        if ball_pos[3] >= ball.canvas_height:
            canvas.itemconfig(word_id,state="hidden")
            canvas.create_text(ball.canvas_width/3,ball.canvas_height/3,
                               text="You lose,you get %d points"%point,
                               font=('Courier',15))
            return False
        return True


paddle = Paddle(canvas,"blue")
ball = Ball(canvas,'gold')
middle = Middle(ball,paddle,canvas)

while 1:
    if middle.hit_bottom() == True:
        middle.check()
        paddle.draw()
        ball.draw()
        

    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)