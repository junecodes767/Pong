from turtle import Turtle
 
class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        #create a ball
        self.shape("circle")
        self.penup()
        self.color("red")
        self.goto(0,0)
        self.x = 10
        self.y =10
        
    def move (self):
         """Move ball to the top right of the screen"""
         x =self.xcor() +self.x
         y =self.ycor() + self.y
         self.goto(x,y)
         
    def bounce (self):
        #let the ball bounce
        self.y*=-1
        

    
     
        
        
        
        
        
        
    