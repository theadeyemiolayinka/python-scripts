from turtle import Turtle, Screen

class Scoreboard(Turtle):
     def __init__(self):
         super().__init__()
         self.color("white")
         self.hideturtle()
         self.pu()
         self.lscore = 0
         self. rscore = 0
         self.update()

     def update(self):
         self.goto(-100,200)
         self.write(self.lscore, align="center", font=( "Arial", 50, "normal"))
         self.goto(100, 200)
         self.write(self.rscore, align="center", font=("Arial", 50, "normal"))

     def l_point(self):
         self.clear()
         self.lscore+=1
         self.update()

     def r_point(self):
         self.clear()
         self.rscore+=1
         self.update()