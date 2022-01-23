###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
from turtle import Turtle, Screen
from random import random

def change_color(t):
    R = random()
    G = random()
    B = random()
    t.color(R, G, B)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

tim = Turtle()
rows = 10
columns = 10
distance = 50.0
dot_size = 20

tim.hideturtle()
tim.speed(20)
tim.up()
tim.setx(-200)
orx = tim.xcor()
tim.sety(-200)
for _ in range(0, columns):
    for _ in range(0, rows):
        change_color(tim)
        tim.dot(dot_size)
        tim.setx(tim.xcor() + distance)
    tim.setx(orx)
    tim.sety(tim.ycor() + distance)


screen = Screen()
screen.exitonclick()
