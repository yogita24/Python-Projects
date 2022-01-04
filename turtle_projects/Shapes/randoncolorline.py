from turtle import Turtle,Screen,colormode
import random 
tim=Turtle()
tim.shape("turtle")
tim.speed("fastest")
tim.pensize(15)
colormode(255)
def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color
tim.color(randomcolor())
for i in range(30):
    tim.color(randomcolor())
    tim.forward(24)
    #tim.right(random.choice([0,90,180,270]))
    tim.setheading(random.choice([0,90,180,270]))

screen=Screen()
screen.exitonclick()