from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_move = 10
        self.y_move = 10

    def create_ball(self):
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0, -250)
        self.setheading(35)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_off_top(self):
        self.y_move *= -1

    def bounce_off_side(self):
        self.x_move *= -1

    def hit(self):
        self.y_move *= -1

    def reset(self):
        self.goto(0, -250)
        self.y_move = 10
        self.x_move *= 1
