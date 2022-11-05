import random
import turtle
from turtle import Turtle, Screen


# Main Code Section
is_race_on = False
screen = Screen()
turtle.colormode(255)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Make a bet on the Turtle on Who will win the Race. Enter the Color: ").lower()
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_postion = [-60, -30, 0, 30, 60, 90]
all_turtle = []
for turtle_index in range(0, 6):
    t = Turtle(shape="turtle")
    t.color(color[turtle_index])
    t.penup()
    t.goto(x=-230, y= y_postion[turtle_index])
    all_turtle.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You have won the Bet. The Winning the Turtle color is {winning_turtle}.")
            else:
                print(f"You have lost the Bet. The Winning the Turtle color is {winning_turtle}.")
        
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# Screen Ending Section
screen.exitonclick()
