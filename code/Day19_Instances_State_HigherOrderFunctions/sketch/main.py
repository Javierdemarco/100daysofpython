from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def moveForwards():
    tim.forward(10)

def moveBackwards():
    tim.backward(10)

def moveCounterClockwise():
    tim.circle(radius=50, extent=10)

def moveClockwise():
    tim.circle(radius=-50, extent=10)

def clearDraw():
    screen.resetscreen()

screen.listen()
screen.onkey(key="w", fun=moveForwards)
screen.onkey(key="s", fun=moveBackwards)
screen.onkey(key="a", fun=moveCounterClockwise)
screen.onkey(key="d", fun=moveClockwise)
screen.onkey(key="c", fun=clearDraw)
screen.exitonclick()
