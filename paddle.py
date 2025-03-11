from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position ):
        super().__init__()
        #creates the rectangular shape of the paddle
        self.penup()
        self.color("white") # paddle color
        self.shape("square") # paddle shape
        self.shapesize(stretch_wid=5,stretch_len=1, ) #paddle resize
        self.goto(position)
        
         
         
        
    def move_up(self):
        new_ycor =self.ycor() + 20
        self.goto(x=self.xcor(),y=new_ycor)
      
    def move_down(self):
        new_ycor =self.ycor() - 20
        self.goto(x=self.xcor(),y=new_ycor)
           