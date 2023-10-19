from turtle import Turtle


class Tim(Turtle):
    def __init__(self, answer, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(answer)
    #
    # def movebro(self, answer, x, y):
    #     self.goto(x, y)
    #     self.write(answer)
