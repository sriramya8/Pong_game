from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
t=Turtle()
s=Screen()
s.bgcolor("black")
s.setup(800,600)
s.title("Pong")
s.tracer(0)
pr= Paddle(350,0)
pl=Paddle(-350,0)
sc=Score()
s.listen()
s.onkey(key="Up",fun=pr.moveUp)
s.onkey(key="Down",fun=pr.moveDown)
s.onkey(key="w",fun=pl.moveUp)
s.onkey(key="s",fun=pl.moveDown)
b= Ball()
x = 0.1
flag=True
while(flag):

    time.sleep(x)

    s.update()
    if(b.ycor()>280 or b.ycor()<-280):
        b.bounce_y()
    if((b.xcor()>340 and b.distance(pr)<50) or (b.xcor()<-340 and b.distance(pl)<50)):
        b.bounce_x()
        x=x*0.8
        time.sleep(x)
    if(b.xcor()>380):
        b.restart_left()
        x=0.1
        sc.inc_left()
    elif(b.xcor()<-380):
        b.restart_right()
        x=0.1
        sc.inc_right()

    b.move()



s.exitonclick()