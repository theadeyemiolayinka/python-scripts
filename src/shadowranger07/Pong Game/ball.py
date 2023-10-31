from turtle import Turtle, Screen

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.pu()
        self.xmove = 10
        self.ymove = 10
        self.speed("fastest")
        self.move_speed = 0.1
    def move(self):
        new_x = self.xcor()+ self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.ymove*= -1

    def bounce_x(self):
        self.xmove*= -1
        self.move_speed *= 0.9
    def resetp(self):
        self.move_speed = 0.1
        self.goto(0,0)

# class Miss(Ball):
#
#      def __init__(self):
#          super().__init__()
#
#
#      def moves(self):
#         new_x = self.xcor() - self.xmove
#         new_y = self.ycor() - self.ymove
#         self.goto(new_x, new_y)