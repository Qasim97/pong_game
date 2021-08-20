import time
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.add_x = 10
        self.add_y = 10
        self.move_speed = 0.1

    def movement(self):
        self.goto(self.xcor() + self.add_x, self.ycor() + self.add_y)

    def bounce_y_axis(self):
        self.add_y *= -1

    def bounce_x_axis(self):
        self.add_x *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.move_speed = 0.1
        self.setposition(0, 0)
        time.sleep(0.1)
        self.bounce_x_axis()
