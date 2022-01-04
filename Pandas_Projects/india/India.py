import turtle
import pandas as pd
from pandas._libs import missing
# from Indicor import cor
screen=turtle.Screen()
image="India1.gif"
screen.title("India State Game")
screen.addshape(image) #loads in a new image as newshape
turtle.shape(image)
data=pd.read_csv("Coordinates.txt")
guessed_states=[]
all_states=data.state.to_list()
while len(guessed_states)<38:
       answer_state=screen.textinput(title=f"{len(guessed_states)}/37 States Correct",prompt="What's another state?").title()
       if answer_state =="Exit":
           states_to_be_learned=set(all_states)-set(guessed_states)
           missing_states=pd.DataFrame(list(states_to_be_learned),columns=["States"])
           missing_states.to_csv("States to Learn.csv",header=True)
           break
       if answer_state in all_states:
           t=turtle.Turtle()
           t.hideturtle()
           t.penup()
           state_answered= data[data.state==answer_state]          
           t.goto(int(state_answered.x),int(state_answered.y))
           t.write(answer_state)
           guessed_states.append(answer_state)

screen.exitonclick()

