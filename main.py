from turtle import Screen, Turtle
from paddle import Paddle
#initalise the  screen object
screen = Screen()

screen.tracer(0)
#set up the screen size
screen.setup(width=1080, height=600)

#set the background color
screen.bgcolor("black")

# initialise the turtle class
dotted_line = Turtle()
dotted_line.color("white")
dotted_line.hideturtle()
dotted_line.penup()
dotted_line.goto(x=0,y=300)

dotted_line.setheading(270)
for _ in range(40):
    dotted_line.forward(10) #go forward by 10 paces
    dotted_line.pendown()
    dotted_line.forward(5)
    dotted_line.penup()


 
paddle = Paddle()
 
screen.update()
screen.listen()

screen.onkey(paddle.move_up,"Up")
screen.onkey()

# to exit the screen
screen.exitonclick()