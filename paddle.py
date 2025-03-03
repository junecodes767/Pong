from turtle import Turtle

class Paddle:
    def __init__(self):
        paddle = Turtle()
        paddle.shape("square")
        paddle.resizemode("user")
        paddle.turtlesize(stretch_wid=3,stretch_len=1,outline=1)