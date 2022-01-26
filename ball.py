from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.x_move = 2
        self.y_move = 2
    
    def move(self):
        self.penup()
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.reflect_y()
        self.pendown()

    def reflect_y(self):
        self.y_move *= -1
    
    def reflect_x(self):
        self.x_move *= -1

    def checkWinner(self):
        if self.xcor() > 380:
            return -1
        if self.xcor() < -380:
            return 1
        return 0

    def reset(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.y_move *= -1
        self.x_move *= -1