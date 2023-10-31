from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(800,600)
screen.bgcolor("blue")
screen.title("Pong")

r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)

ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor()> 290 or ball.ycor()< -290 :
        ball.bounce_y()

    elif ball.distance(r_paddle) < 50 and ball.xcor()> 320:
        ball.bounce_x()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    elif ball.xcor()> 390:
        ball.resetp()
        ball.bounce_x()
        score.l_point()

    elif ball.xcor() < -390:
        ball.resetp()
        ball.bounce_x()
        score.r_point()


        # miss.showturtle()
        # miss.moves()
        #
        # if miss.ycor() > 290 or miss.ycor() < -290:
        #     miss.bounce_y()
        #
        # elif miss.distance(r_paddle) < 50 and miss.xcor() > 320:
        #     miss.bounce_x()
        #
        # elif miss.distance(l_paddle) < 50 and miss.xcor() < -320:
        #     miss.bounce_x()
        #
        # elif miss.xcor() > 390 or miss.xcor() < -390:
        #     miss.hideturtle()
        #     ball = Ball()
        #     ball.move()

screen.exitonclick()