from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        #creates the rectangular shape of the paddle
        paddle = Turtle()
        paddle.penup()
        paddle.color("white") # paddle color
        paddle.shape("square") # paddle shape
        paddle.resizemode("user")
        paddle.turtlesize(stretch_wid=3,stretch_len=1,outline=2) #paddle resize
        paddle.goto(x=500, y=0)
        
        
        