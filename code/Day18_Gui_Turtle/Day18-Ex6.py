from random import randint, random, choice
from turtle import Turtle, Screen

def change_color(t):
    R = random()
    G = random()
    B = random()
    t.color(R, G, B)

tim = Turtle()
radius = 100
tim.pensize(2)
tim.speed(20)
size_of_gap = 10

for _ in range(int(360 / size_of_gap)):
    tim.setheading(tim.heading() + size_of_gap)
    change_color(tim)
    tim.circle(radius)

screen = Screen()
screen.exitonclick()
