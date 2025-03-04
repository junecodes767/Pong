from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        #creates the rectangular shape of the paddle
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.color("white") # paddle color
        self.paddle.shape("square") # paddle shape
        self.paddle.shapesize(stretch_wid=5,stretch_len=1, ) #paddle resize
        self.paddle.goto(x=500, y=0)
        self.paddle_2 = Turtle()
        self.paddle_2.penup()
        self.paddle_2.color("white") # paddle color
        self.paddle_2.shape("square") # paddle shape
        self.paddle_2.shapesize(stretch_wid=5,stretch_len=1, ) #paddle resize
        self.paddle_2.goto(x=-500, y=0)
         
        
    def move_up(self):
        new_ycor =self.paddle.ycor() + 20
        self.paddle.goto(x=self.paddle.xcor(),y=new_ycor)
      
    def move_down(self):
        new_ycor =self.paddle.ycor() - 20
        self.paddle.goto(x=self.paddle.xcor(),y=new_ycor)
           