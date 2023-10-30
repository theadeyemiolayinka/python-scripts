from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, posix, posiy):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.goto(posix, posiy)

    def go_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor()-20)


