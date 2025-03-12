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
        self.move_speed =0.1
    
     
        
    def move (self):
         """Move ball to the top right of the screen"""
         x =self.xcor() +self.x
         y =self.ycor() + self.y
         self.goto(x,y)
         
    def bounce_y (self):
        #let the ball bounce
        self.y*=-1
        
        
    def bounce_x (self):
        #let the ball bounce
        self.x*=-1
        self.move_speed *= 0.9
    
    def reset_position(self):
        #brings ball back to home
        self.goto(0,0)
        self.move_speed =0.1
        self.bounce_x()
         

    
     
        
        
        
        
        
        
    