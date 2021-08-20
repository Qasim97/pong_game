import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard

game_over = False
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

player1_paddle = Paddle((350, 0))
player2_paddle = Paddle((-350, 0))
ball = Ball()
scoreBoard = ScoreBoard()
scoreBoard.show_score()
screen.listen()

screen.onkey(player1_paddle.move_up, "Up")
screen.onkey(player1_paddle.move_down, "Down")
screen.onkey(player2_paddle.move_up, "w")
screen.onkey(player2_paddle.move_down, "s")
bounce = None
while not game_over:
    scoreBoard.clear()
    time.sleep(ball.move_speed)
    screen.update()
    ball.movement()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()
    if ball.distance(player1_paddle) < 50 and ball.xcor() > 320 or\
            ball.distance(player2_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_axis()
    if ball.distance(player1_paddle) > 50 and ball.xcor() > 390:
        ball.refresh()
        scoreBoard.add_score_player2()
    if ball.distance(player2_paddle) > 50 and ball.xcor() < -390:
        ball.refresh()
        scoreBoard.add_score_player1()
    scoreBoard.show_score()
    game_over = scoreBoard.check_score()

screen.exitonclick()
