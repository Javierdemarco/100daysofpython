from turtle import Turtle

CONSTANT_IN_CLASS = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self, num):
        self.segments = []
        self.starting_positions = []
        self.createSnake(num)
        self.head = self.segments[0]

    def createSnake(self, num):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def move(self):
        for tpos in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[tpos - 1].xcor()
            new_y = self.segments[tpos - 1].ycor()
            self.segments[tpos].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        t = Turtle("square")
        t.width(20)
        t.color("white")
        t.penup()
        t.goto(position)
        self.segments.append(t)

    def snake_grow(self):
        self.add_segment(self.segments[-1].position())
