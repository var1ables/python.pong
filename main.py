from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import time



#Creating screen
screen = Screen()
screen.bgcolor('black')
screen.screensize(800,600)
screen.tracer(0)
screen.title('pong')
scoreboard = Scoreboard()



#creating paddles from Paddles
r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))

#creating the ball
ball = Ball()

#making paddles go up
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_down, 's')

game = True
while game:
    time.sleep(.075)
    screen.update()
    ball.move()

    #detect collision with top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()


    if ball.distance(r_paddle) < 60 and ball.xcor() >330 or ball.distance(l_paddle) < 60 and ball.xcor() < -330:
        ball.ricochet()

    if ball.xcor() > 360:
        ball.reset_position()
        scoreboard.l_increase_score()

    if ball.xcor() < -360:
        ball.reset_position()
        scoreboard.r_increase_score()


screen.exitonclick()