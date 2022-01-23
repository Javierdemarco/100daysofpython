from turtle import Turtle, Screen
from random import randint, random, choice

def change_color(t):
    R = random()
    G = random()
    B = random()
    t.color(R, G, B)

tim = Turtle()
move_distance = 50
degrees = [0, 90, 180, 270]
tim.pensize(10)
tim.speed(20)

while True:
    change_color(tim)
    tim.forward(move_distance)
    tim.setheading(choice(degrees))









screen = Screen()
screen.exitonclick()
