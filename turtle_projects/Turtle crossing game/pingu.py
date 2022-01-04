from turtle import Turtle
import random
STARTING_POSITION=-280
MOVING_DISTANCE=10
FINAL_POSITION=260
class Pingy(Turtle):
    def __init__(self):
        super().__init__()
        self.move=MOVING_DISTANCE
        self.finalpoint=FINAL_POSITION
        self.start=STARTING_POSITION
        self.penup()
        self.shape("turtle")
        self.color('grey')
        self.goto(0,self.start)
    def up(self):
        self.forward(self.move)   
    def reset(self):
            self.goto(0,self.start)
    def is_final_position(self):
        if self.ycor()>self.finalpoint:
            return True
        else :
            return False

