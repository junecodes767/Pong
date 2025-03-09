from turtle import Turtle
 
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        #create a ball
        self.shape("circle")
        self.penup()
        self.color("red")
        self.goto(0,0)
         
        
    def move (self):
         """Move ball to the top right of the screen"""
         x =self.xcor() +10
         y =self.ycor() +10
         self.goto(x,y)

    
     
        
        
        
        
        
        
    