import turtle
bruh = turtle.Turtle()
screen = turtle.Screen()
screen.colormode(255)
bruh.hideturtle() 
bruh.speed('fastest')   
bruh.right(-90)


bruh.hideturtle()        
bruh.penup()                
bruh.goto(0, -300)                 
bruh.pendown()

angle = 45


def ftree(length, lvl):  
  
    if lvl > 0:  
          
        bruh.pencolor(150, 250//lvl, 0)            
        bruh.forward(length)  
        bruh.right(angle)  
        ftree(0.7 * length, lvl-1)  
        bruh.pencolor(150, 250//lvl, 0)  
        bruh.left(2 *angle )  
        ftree(0.7 * length, lvl-1)  
        bruh.pencolor(150, 250//lvl, 0)  
        bruh.right(angle)  
        bruh.forward(-length)  


# call your function here ftree(length, level)
ftree(150, 8)



turtle.done()
