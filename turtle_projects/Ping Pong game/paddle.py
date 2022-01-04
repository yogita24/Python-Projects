from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_len=1,stretch_wid=6)
    def go_up(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)
    def go_down(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)