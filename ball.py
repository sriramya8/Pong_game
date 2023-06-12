from turtle import Turtle
import time
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move=10
        self.y_move=10
    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)
    def bounce_y(self):
        self.y_move*=-1
        self.move()
    def bounce_x(self):
        self.x_move*=-1
        self.move()
    def restart_left(self):
        self.goto(0,0)
        self.x_move *= -1
        time.sleep(0.9)
        self.move()
    def restart_right(self):
        self.goto(0, 0)
        self.x_move *= -1
        time.sleep(0.9)
        self.move()

