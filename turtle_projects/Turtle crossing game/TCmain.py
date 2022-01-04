from turtle import Turtle,Screen,colormode
import random
import time
from cars import Car_Manager
from pingu import Pingy
from levelchamp import ScoreBoard
colormode(255)
screen=Screen()
screen.tracer(0)
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title('Turtle crossing game')
pingy=Pingy()
carr=Car_Manager()
player=screen.textinput("Player Input","Enter Player's nick name:")
score=ScoreBoard(player)

pingy.setheading(90)
# playerinp=Turtle()
game_is_on=True
screen.listen()
screen.onkey(pingy.up,"Up")
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carr.createcar()
    carr.move()
    for car in carr.all_cars:
        if car.distance(pingy)<15:
            score.gameover()
            game_is_on =False
    if pingy.is_final_position():
        pingy.reset()
        carr.level_up()
        score.level_up()

screen.exitonclick()
