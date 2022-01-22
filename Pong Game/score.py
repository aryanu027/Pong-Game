import turtle

FONT = ("Arial", 30, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.speed(0)
        self.penup()
        self.y_pos = int(self.getscreen().window_height() / 2 - 100)
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.clear()
        self.setpos(-80, self.y_pos)
        self.write(self.left_score, align="center", font=FONT)
        self.setpos(80, self.y_pos)
        self.write(self.right_score, align="center", font=FONT)

    def add_one_left(self):
        self.left_score += 1
        self.update()

    def add_one_right(self):
        self.right_score += 1
        self.update()

    def game_over(self):
        self.setpos(0, -self.y_pos)
        self.write("GAME OVER", align="center", font=FONT)
