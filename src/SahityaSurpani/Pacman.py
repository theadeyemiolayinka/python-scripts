import random
import turtle
from random import choice
from turtle import *
from freegames import floor, vector

mes = Turtle(visible=False)      # mes arrow hide


def restart():
    mes.undo()


def game():
    restart()
    initialState = {'score': 0}  # initial score
    turtle.title("PacMan")  # window title
    path = Turtle(visible=False)  # turtle arrow invisible
    writer = Turtle(visible=False)  # writer arrow invisible
    mes2 = Turtle(visible=False)
    aim = vector(5, 0)  # pacman movement at the beginning
    pacman = vector(-40, -80)  # pac man initial position
    colors = ["red", "blue"]  # ghost colors
    ghosts = [
        [vector(0, -10), vector(5, 0)],
        [vector(-20, 0), vector(0, 5)],
        [vector(-10, 5), vector(0, -5)],
        [vector(0, 0), vector(-5, 0)],
    ]  # initial positions of ghosts and where to go
    tiles = [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0,
        0, 1, 1, 0, 1, 0, 3, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0,
        0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 3, 1, 1, 0, 1, 0, 0,
        0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 0, 3, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0,
        0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0,
        0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
        0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    ]

    def block():  # styling window
        bgcolor('black')
        path.color('green')
        for index in range(len(tiles)):  # for drawing walls, dota and fruits according to tile value
            tile = tiles[index]
            if tile > 0:
                x = (index % 20) * 20 - 200
                y = 180 - (index // 20) * 20
                square(x, y)
                if tile == 3:
                    path.up()
                    # path.goto(x + 10, y + 10)
                    path.goto(x + 10, y + 10)
                    path.dot(12, '#FF8C00')
                elif tile == 1:
                    path.up()
                    path.goto(x + 10, y + 10)
                    path.dot(3, 'orange')

        update()  # updates every time pacman moves

    def square(x, y):  # to draw a square and fill it
        path.up()  # pen up
        path.goto(x, y)
        path.down()  # pen down
        path.begin_fill()  # draw

        for count in range(4):  # all sides of a square
            path.forward(20)
            path.left(90)

        path.end_fill()

    def offset(point):  # gives the position just like a shadow
        x = (floor(point.x, 20) + 200) / 20
        y = (180 - floor(point.y, 20)) / 20
        return int(x + y * 20)

    def valid(point):  # to stop pacman from going into the walls
        index = offset(point)

        if tiles[index] == 0:
            return False

        index = offset(point + 19)

        if tiles[index] == 0:
            return False

        return point.x % 20 == 0 or point.y % 20 == 0

    def change(x, y):  # change the co ordinates when keys are applied
        if valid(pacman + vector(x, y)):
            aim.x = x
            aim.y = y

    listen()
    onkey(lambda: change(5, 0), 'Right')
    onkey(lambda: change(-5, 0), 'Left')
    onkey(lambda: change(0, 5), 'Up')
    onkey(lambda: change(0, -5), 'Down')



    def move():
        writer.undo()  # for score
        writer.write('Score : ' + str(initialState['score']), font=('Arial', 16, "normal"))
        clear()  # for ghosts and pacman
        if valid(pacman + aim):
            pacman.move(aim)
        index = offset(pacman)
        if tiles[index] == 1 or tiles[index] == 3:
            if tiles[index] == 3:
                initialState['score'] += 10
            else:
                initialState['score'] += 1
            tiles[index] = 2  # to prevent adding marks everytime he comes to the same position
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)
        up()
        goto(pacman.x + 10, pacman.y + 10)
        dot(15, 'YELLOW')
        for point, course in ghosts:
            if valid(point + course):
                point.move(course)
            else:
                options = [
                    vector(5, 0),
                    vector(-5, 0),
                    vector(0, 5),
                    vector(0, -5),
                ]
                plan = choice(options)
                course.x = plan.x
                course.y = plan.y
                up()
            goto(point.x + 10, point.y + 10)
            thecolor = random.choice(colors)
            dot(15, thecolor)
        update()
        for point, course in ghosts:
            if abs(pacman - point) < 20:
                mes.goto(-100, 200)
                mes.color('white')
                mes.write('Game over \n press space to restart!!', align="left", font=("Verdana", 15, "normal"))
                clear()
                writer.undo()
                listen()
                # onkey(lambda: game(), 'Up')
                return onkey(lambda: game(), 'space')
        ontimer(move, 50)

    Screen().setup(600, 500, 370, 0)
    hideturtle()  # to hide turtles
    tracer(False)
    writer.goto(70, 180)
    writer.color('pink')
    writer.write(initialState['score'], font=("Arial", 15, "normal"))
    block()
    move()
    done()    # last statement in turtle graphic


game()



