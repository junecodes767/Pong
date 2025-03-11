from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
#initalise the  screen object
screen = Screen()

screen.tracer(0)
#set up the screen size
screen.setup(width=800, height=600)

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

ball = Ball()
 
r_paddle = Paddle((350,0))
l_paddle =Paddle((-350,0))
screen.listen()

screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")


screen.onkey(l_paddle.move_up,"s")
screen.onkey(l_paddle.move_down,"x")
game_is_on =True
 
#shows the position of the ball at the end of the screen
 

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    if ball.ycor()> 290 or ball.ycor()<-290:
        ball.bounce_y()

# detect collision with right paddle
    if ball.distance(r_paddle)<500 and ball.xcor()>320  or ball.distance(l_paddle) < 500 and ball.xcor() <-320 :
       ball.bounce_x()
         
         
# to exit the screen
screen.exitonclick()