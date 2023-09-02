from turtle import Turtle, Screen
from paddel import Paddel
import time
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.listen()

screen.tracer(0)

r_paddel = Paddel((350, 0))
l_paddle = Paddel((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(r_paddel.up, "Up")
screen.onkey(r_paddel.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.06)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddel) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() > 390:
        time.sleep(1.0)
        ball.goal()
        r_paddel.refresh((350, 0))
        l_paddle.refresh((-350, 0))
        scoreboard.l_point()

    if ball.xcor() < -390:
        time.sleep(1.0)
        ball.goal()
        l_paddle.refresh((-350, 0))
        r_paddel.refresh((350, 0))
        scoreboard.r_point()



screen.exitonclick()
