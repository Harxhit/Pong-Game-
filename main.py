from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Paddle setup
right_paddle = Paddle((350, 0))  
left_paddle = Paddle((-350, 0))

# Ball setup
ball = Ball()

# Scoreboard setup
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Main game loop
on = True
while on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball out of right boundary
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()
        time.sleep(0.1)  

    # Ball out of left boundary
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.right_point()
        time.sleep(0.1)  

    # Ball collision with paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

screen.exitonclick()
