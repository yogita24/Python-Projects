from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from Scoreboard import Score 
import time
screen=Screen()
screen.tracer(0)
sl=Score((-150,280))
sr=Score((150,280))
screen.title("PingPong")
screen.setup(width=600 ,height=600)
screen.bgcolor("black")
pddlel=Paddle()
pddler=Paddle()
bll=Ball()
pddlel.goto(-290,0)
pddler.goto(280,0)
screen.listen()
screen.onkey(pddlel.go_up,"Up")
screen.onkey(pddlel.go_down,"Down")
screen.onkey(pddler.go_up,"Left")
screen.onkey(pddler.go_down,"Right")
screen.onkey(sr.game_over,"space")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    bll.mover()
   

    if bll.ycor()>290 or bll.ycor()< -290:
        bll.bounce_y()
    if bll.xcor()>290 :
        bll.reset_position()
        sl.score_increment()
    if bll.xcor()<-290:
        bll.reset_position()
        sr.score_increment()
    if bll.distance(pddler)<50 and bll.xcor()>260 or bll.distance(pddlel)<50 and bll.xcor()<-260:
        bll.bounce_x()
    if sr.game_on==False:
        game_is_on=False
        break

    
    
   


        

screen.exitonclick()