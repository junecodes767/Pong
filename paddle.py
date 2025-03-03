from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        #creates the rectangular shape of the paddle
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.color("white") # paddle color
        self.paddle.shape("square") # paddle shape
        self.paddle.resizemode("user")
        self.paddle.turtlesize(stretch_wid=3,stretch_len=1,outline=2) #paddle resize
        self.paddle.goto(x=500, y=0)
         
        
    def move_up(self):
        self.paddle.setheading(90)
        self.paddle.forward(10)
        