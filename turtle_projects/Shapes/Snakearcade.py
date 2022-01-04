from turtle import Turtle,Screen
from snake import Snake
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.title("Welcome To Snake Arcade")
screen.bgcolor("black")
screen.tracer(0)
tim=Turtle("square")
screen.onlisten()
s=Snake()
s.create()
s.move()

    
        
screen.exitonclick()

