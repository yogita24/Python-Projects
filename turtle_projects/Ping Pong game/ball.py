from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("Blue")
        self.y_move=10
        self.x_move=10
        #self.speed("slowest")
        self.shapesize(stretch_len=0.8,stretch_wid=0.8)
    def mover(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
        # print(new_x,new_y,self.y_move,self.x_move)
    def bounce_y(self):
        self.y_move=self.y_move*-1
    def bounce_x(self):
        self.x_move=self.x_move*-1
    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()