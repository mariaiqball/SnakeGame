from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.move = False
        self.align = "center"
        self.font = ("Courier", 20, "normal")
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align=self.align, font=self.font)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=self.align, font=self.font)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=self.align, font=self.font)