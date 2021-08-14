from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -280)

    def go_left(self):
        if self.xcor() > -380:
            new_x = self.xcor() - 20
            self.goto(x=new_x, y=self.ycor())

    def go_right(self):
        if self.xcor() < 380:
            new_x = self.xcor() + 20
            self.goto(x=new_x, y=self.ycor())
