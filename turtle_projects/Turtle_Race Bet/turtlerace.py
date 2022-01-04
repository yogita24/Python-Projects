from turtle import Turtle,Screen,colormode
import random
#tim=Turtle()
is_race_on=False
screen=Screen()
#tim.shape("turtle")
screen.setup(width=600,height=500)
colors=["purple","yellow","green","aquamarine","orange","red"]
random.shuffle(colors)
y=[-80,-50,-20,20,50,80]
all_turtles=[]
for t_index in range(0,6):
    tim=Turtle(shape="turtle")
    all_turtles.append(tim)
    tim.penup()
    tim.color(colors[t_index])
    tim.goto(-290,y[t_index])
bet_on=screen.textinput(title="Turtle's Race" , prompt= "Which turtle you want to bet on,Choose the color:")
if bet_on:
    is_race_on=True
while is_race_on:
    for turtles in all_turtles:
        if turtles.xcor()>280:
            is_race_on=False
            if bet_on==turtles.pencolor():
                print(f"You've won!! The {turtles.pencolor()} turtle is winning turtle.")
                break
            else: 
                print(f"You lost!! The {turtles.pencolor()} turtle is winning turtle.")
                break
        random_step=random.randint(10,20)
        turtles.forward(random_step)

screen.exitonclick()