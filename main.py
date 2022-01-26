from turtle import Screen, right
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Python Pong")
screen.tracer(0)

leftPaddle = Paddle([-350, 0])
rightPaddle = Paddle([350, 0])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(rightPaddle.movePaddleUp, "Up")
screen.onkey(rightPaddle.movePaddleDown, "Down")
screen.onkey(leftPaddle.movePaddleUp, "a")
screen.onkey(leftPaddle.movePaddleDown, 'z')

gameLoop = True

while gameLoop:
    ball.move()
    leftPaddle.checkBallCollision(ball)
    rightPaddle.checkBallCollision(ball)
    winner = ball.checkWinner()
    if winner != 0:
        ball.reset()
        if winner == -1:
            scoreboard.addLeftScore()
        if winner == 1:
            scoreboard.addRightScore()
    
    screen.update()

screen.exitonclick()