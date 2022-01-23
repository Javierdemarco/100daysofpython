from turtle import Turtle, Screen
from random import randint


tim = Turtle()
tim.penup()
tim.right(270)
tim.forward(300)
tim.right(90)
tim.pendown()
tim.forward(200)
for x in range(3, 9):
    for _ in range(x):
        tim.right(360/x)
        tim.forward(200)








screen = Screen()
screen.exitonclick()
