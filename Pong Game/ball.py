import turtle
import math
import random

move_ball = 20
class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        a = self.getscreen().window_height() / 2
        b = self.getscreen().window_width() / 2
        c = math.sqrt(a*a + b*b)
        self.initial_angle = int(math.degrees(math.asin(a / c)))
        self.setheading(self.initial_angle + random.randint(15, 30))
        self.setpos(0, 0)

    def move(self):
        self.forward(move_ball)

    def wall_bounce(self):
        self.setheading(360 - self.heading())

    def paddle_bounce(self):
        self.move_speed *= 0.9
        self.setheading(180 - self.heading())

    def reset_position(self, side=""):
        self.move_speed = 0.1
        if side == "left":
            self.setheading(180 + self.initial_angle + random.randint(15, 30))
        else:
            self.setheading(self.initial_angle + random.randint(15, 30))
        self.setpos(0, 0)
