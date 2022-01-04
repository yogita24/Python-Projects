from turtle import Turtle
cor=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments=[]
        self.create()
        self.head=self.segments[0]
    def create(self):
        for i in cor:
            self.add_segment(i)
    def add_segment(self,i):
        newturtle=Turtle("square")
        newturtle.penup()
        newturtle.color("white")
        newturtle.goto(i)
        self.segments.append(newturtle)
    def extend(self):
        self.add_segment(self.segment[-1].position())


    def move(self):
        for position in range(len(self.segments)-1,0,-1):
            newcor_x=self.segments[position-1].xcor()
            newcor_y=self.segments[position-1].ycor()
            self.segments[position].goto((newcor_x,newcor_y))
        #segments[0].left(90)
        self.segments[0].forward(20)
    def up(self):
        if self.head.heading()!=DOWN:
           self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
           self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
           self.head.setheading(RIGHT)
