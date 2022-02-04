from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", align=ALIGN, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over", align=ALIGN, font=FONT)
