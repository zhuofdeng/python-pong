from turtle import Turtle
import random
class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.leftScore = 0
        self.rightScore = 0
        self.printScores()
    
    def printScores(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.leftScore, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rightScore, align="center", font=("Arial", 80, "normal"))

    def addLeftScore(self):
        self.leftScore += 1
        self.printScores()
    
    def addRightScore(self):
        self.rightScore += 1
        self.printScores()
    

