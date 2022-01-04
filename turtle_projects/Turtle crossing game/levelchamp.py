from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial','10','normal')
class ScoreBoard(Turtle):
    def __init__(self,name):
        super().__init__()
        self.level=0
        self.name=name
        self.penup()
        self.hideturtle()
        self.color("yellow")
        self.goto(0,260)
        self.update_level()
    def level_up(self):
        self.level+=1
        self.clear()
        self.update_level()
    def update_level(self):
        self.write(f"Level:{self.level} \n Champ Name: {self.name}",align=ALIGNMENT,font=FONT)
    def gameover(self):
        self.goto(0,0)
        self.write(f"{self.name},Game over!!",align=ALIGNMENT,font=FONT)
