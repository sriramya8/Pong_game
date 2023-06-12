from turtle import Turtle
class Paddle(Turtle):
        def __init__(self,x_cor,y_cor):
                self.x_cor=x_cor
                self.y_cor=y_cor
                super().__init__()
                self.shape("square")
                self.color("white")
                self.penup()
                self.shapesize(stretch_len=1, stretch_wid=5)
                self.goto(x_cor, y_cor)


        def moveUp(self):
                new_y= self.ycor()+20
                self.goto(self.x_cor,new_y)

        def moveDown(self):
                new_y=self.ycor()-20
                self.goto(self.x_cor,new_y)
