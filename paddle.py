from turtle import Turtle, xcor
from ball import Ball

class Paddle(Turtle):
    def __init__(self, initialPosition):
        super(Paddle, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(initialPosition)

    def movePaddleUp(self):
        newY = self.ycor() + 20
        if newY <= 260 :
            self.penup()
            self.goto(self.xcor(), newY)

    def movePaddleDown(self):
        newY = self.ycor() - 20
        if newY >= -240 :
            self.penup()
            self.goto(self.xcor(), newY)

    def checkBallCollision(self, ball: Ball):
        if self.xcor() < 0:
            if ball.xcor() < 0:
                if ball.xcor() < -330 and ball.distance(self.pos()) < 50:
                    ball.reflect_x()
        else:
            if ball.xcor() > 0:
                if ball.xcor() > 330 and ball.distance(self.pos()) < 50:
                    ball.reflect_x()