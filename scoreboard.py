from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_scoreboard()
        self.game_speed = 0.1

    def point(self, color: str):
        if color == "yellow":
            self.score += 1
        elif color == "green":
            self.score += 3
        elif color == "orange":
            self.score += 5
        else:
            self.score += 7
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-340, 270)
        self.write(f"Score: {self.score}", align="center", font=("courier", 20, "normal"))
        self.goto(280, 270)
        self.write(f"Lives Remaining: {self.lives}", align="center", font=("courier", 20, "normal"))

    def game_over(self):
        self.goto(0, -100)
        self.write(f"GAME OVER! Final Score: {self.score}",
                   align="center",
                   font=("courier", 40, "bold"))
        self.goto(0, -130)
        self.write("Press 'y' to play again. Otherwise, click to exit.",
                   align="center",
                   font=("courier", 20, "normal"))

    def game_won(self):
        self.goto(0, 50)
        self.write(f"YOU WON! Final Score: {self.score}",
                   align="center",
                   font=("courier", 40, "bold"))
        self.goto(0, 20)
        self.write("Press 'y' to play again. Otherwise, click to exit.",
                   align="center",
                   font=("courier", 20, "normal"))
