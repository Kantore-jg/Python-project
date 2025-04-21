from importlib.resources import contents
from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial",24,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score=0
        self.update_scoreboard()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align=ALIGNMENT,font=FONT)



    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",align=ALIGNMENT,font=FONT)
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()
    def reset(self):
        if self.score>self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt",mode="w") as data:
            data.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over!",font = ("Arial",24,"normal"))

    def checking(self):
        if self.score > self.high_score:
            self.goto(0,270)
            self.write(f"High Score: {self.score}", align=ALIGNMENT, font=FONT)
        else:
            self.goto(20, 270)
            self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)



