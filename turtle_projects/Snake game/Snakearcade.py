from turtle import Turtle,Screen
from snake import Snake
from food import Food
from Scoreboard import Score
import time
screen=Screen()
screen.setup(width=600,height=600)
screen.title("Welcome To Snake Arcade")
screen.bgcolor("black")
screen.tracer(0)
snk=Snake()
snk.create()
screen.listen()
screen.onkey(snk.up,"Up")
screen.onkey(snk.down,"Down")
screen.onkey(snk.left,"Left")
screen.onkey(snk.right,"Right")
food=Food()
score=Score()


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snk.move()

    if snk.head.distance(food)<10:
        food.refresh()
        snk.extend()
        score.score_increment()
    if snk.head.xcor() > 270 or snk.head.xcor()<-270 or snk.head.ycor()>270 or snk.head.ycor()<-270:
        is_game_on=False
        score.game_over()
    for segment in snk.segments[1:]:
        if snk.head.distance(segment)<10:
            is_game_on=False
            score.game_over()

screen.exitonclick()

