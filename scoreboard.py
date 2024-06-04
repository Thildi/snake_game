from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.high_score = 0
        self.color("white")
        self.goto(x=0, y=270)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))
