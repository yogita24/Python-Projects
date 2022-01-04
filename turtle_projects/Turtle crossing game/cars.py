from turtle import Turtle
import random
STARTING_MOVE_DISTANCE=5
MOVE_INCREMET=10
class Car_Manager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE
    def createcar(self):
        randomchance=random.randint(1,4)
        if randomchance==1:
            car=Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(stretch_wid=1,stretch_len=2)
            car.goto(300,random.randint(-280,260))
            r=random.randint(0,255)
            g=random.randint(0,255)
            b=random.randint(0,255)
            car.color(r,g,b)
            self.all_cars.append(car)
    def move(self):
        for i in self.all_cars:
            i.backward(self.car_speed)
    def level_up(self):
        self.car_speed+=MOVE_INCREMET

