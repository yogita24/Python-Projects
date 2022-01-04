from turtle import Turtle,Screen,colormode
import random 
tim=Turtle()
tim.shape("turtle")
tim.speed("fastest")
# tim.pensize(2)
colormode(255)
screen=Screen()

def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
def spirals(n):
    tim.color(randomcolor())
    for i in range(int(n)):
        tim.color(randomcolor())
        tim.circle(80)
        tim.right(360/int(n))
screen.setup(500,400)
n=screen.textinput(title="Spirographs",prompt="Enter no. of circles you wamt in spirals")
spirals(int(n))
screen.exitonclick()
