from turtle import Turtle

class Score(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.s=0
        self.color("yellow")
        self.hideturtle()
        self.goto(position)
        self.update_score()
        self.game_on=True
    def update_score(self):
        self.write(f"Score:{self.s}",align="center",font=('Arial','10','normal'))
    def score_increment(self):
        self.s+=1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto((0,0))
        self.color("red")
        self.game_on=False
        self.write("Game Over",align="center",font=("Arial",24,"normal"))
        

   
    

      
