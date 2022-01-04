from turtle import Turtle
Font=("Arial",16,"normal")
Alignment="center"
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("yellow")
        self.penup()
        self.goto((0,270))
        self.hideturtle()
        self.update_score()
    def update_score(self):
        self.write(f"Score:{self.score}",align=Alignment,font=Font)
    def score_increment(self):
        self.score+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto((0,0))
        self.write("Game Over",align="center",font=("Arial",24,"normal"))
   
    
