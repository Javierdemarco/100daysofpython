from turtle import Turtle, Screen


tim = Turtle()
tim.shape("turtle")
tim.color("black")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

for x in range(100):
    tim.forward(5)
    if x % 2 == 0:
        tim.pendown()
    else:
        tim.penup()





screen = Screen()
screen.exitonclick()
