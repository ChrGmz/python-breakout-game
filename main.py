import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block_manager import BlockManager


def start_game():
    global game_on
    while game_on:
        time.sleep(scoreboard.game_speed)
        screen.update()
        ball.move()

        # Detect collision with top wall
        if ball.ycor() > 260:
            ball.bounce_off_top()

        # Detect collision with left and right walls
        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_off_side()

        # Detect collision with paddle
        if ball.ycor() <= -260 and ball.distance(paddle) <= 50 and ball.y_move < 0:
            ball.hit()

        # Detect ball past bottom
        if ball.ycor() <= -320:
            scoreboard.lives -= 1
            scoreboard.update_scoreboard()
            if scoreboard.lives == 0:
                scoreboard.game_over()
                game_on = False
            else:
                ball.reset()
                scoreboard.game_speed = 0.1
        else:
            hit_points = block_manager.has_hit(ball)
            if hit_points:
                ball.hit()
                scoreboard.score += hit_points
                scoreboard.update_scoreboard()
                scoreboard.game_speed *= .97

        if len(block_manager.blocks) == 0:
            scoreboard.game_won()
            game_on = False


def reset_game():
    global game_on
    if not game_on:
        scoreboard.lives = 3
        scoreboard.score = 0
        scoreboard.update_scoreboard()
        block_manager.reset()
        ball.reset()
        game_on = True
        start_game()


screen = Screen()
screen.title("Python Breakout!")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()
paddle = Paddle()
block_manager = BlockManager()

screen.update()

screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")
screen.onkey(reset_game, "y")

screen.listen()
game_on = True

start_game()

screen.exitonclick()
