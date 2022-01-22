import turtle

Size = 20
class Paddle(turtle.Turtle):
    def __init__(self, side=""):
        super().__init__()
        self.x_pos = int(self.getscreen().window_width() * 45 / 100)
        if side == "left":
            self.x_pos *= -1
        self.shape("square")
        self.color("green")

        self.shapesize(stretch_len=5)
        self.penup()
        self.speed(5)
        self.setheading(90)
        self.setpos(self.x_pos, 0)

    def move_up(self):
        self.forward(Size)

    def move_down(self):
        self.backward(Size)
