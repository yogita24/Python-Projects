from turtle import Turtle,Screen,colormode
import random
tim=Turtle()
colormode(255)
tim.shape("turtle")
tim.pensize(1)
tim.speed("fastest")
def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

def direction(i):
    tim.color(randomcolor())
    for _ in range(i):
        tim.forward(100)
        tim.right(360/i)
tim.right(110)
tim.penup()
tim.forward(30)
tim.pendown()
def different_shapes(n):
    for _ in range(3,n):
        direction(_)
different_shapes(int(input("Upto which no. of sides of figures you want")))

screen=Screen()
screen.exitonclick()