import turtle
from turtle import Turtle ,Screen
import random
is_race_on=False

colour = ["red","green","blue","yellow","white","indigo"]
print(colour)

screen= Screen()
screen.bgcolor("black")
screen.setup(width=500,height=600)

turtle.goto(0,240)
turtle.color('chartreuse')
style = ('Arial', 30, 'italic')
turtle.write('** BET TO WIN **', font=style, align='center')
turtle.hideturtle()

user_bet=screen.textinput(title="make a bet ", prompt="which turtle will win?? \n red, \n green, \n blue, \n yellow, \n white, \n indigo")
y=-100
all_turtles=[]

design=Turtle(shape="turtle")
design.speed("fast")
design.hideturtle()
design.color(user_bet)
design.penup()
design.goto(-250,295)
design.pendown()
design.pensize(10)
design.forward(490)
design.right(90)
design.forward(580)
design.right(90)
design.forward(488)
design.right(90)
design.forward(580)

for turtle_index in range(0,6):
    col = random.choice(colour)
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(col)
    colour.remove(col)
    new_turtle.penup()
    new_turtle.goto(-235, y)
    y+=50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on= False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"winner winner chicken dinner, {winning_color} turtle is the winner ")
                turtle.goto(0, 200)
                turtle.color(winning_color)
                style = ('Arial', 30, 'italic')
                turtle.write(f'** {winning_color} is the winner **', font=style, align='center')
                turtle.hideturtle()
            else:
                print(f"you loose the bet, {winning_color} turtle is the winner ")
                turtle.goto(0, 180)
                turtle.color(user_bet)
                style = ('Arial', 20 , 'italic')
                turtle.write(f'{user_bet} loosed the bet', font=style, align='center')
                turtle.hideturtle()

        random_distance=random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()