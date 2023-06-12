from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("White")
        self.hideturtle()
        self.goto(-100, 260)
        self.write("0",False,"center",font=('Arial', 15, 'normal'))
        self.goto(100, 260)
        self.write("0", False, "center", font=('Arial', 15, 'normal'))
        self.leftscore=0
        self.rightscore=0

    def inc_left(self):
        self.goto(-100, 260)
        self.clear()
        self.leftscore+=1
        self.write(str(self.leftscore), False, "center", font=('Arial', 15, 'normal'))
        self.goto(100, 260)
        self.write(str(self.rightscore), False, "center", font=('Arial', 15, 'normal'))

    def inc_right(self):
        self.goto(100, 260)
        self.clear()
        self.rightscore+=1
        self.write(str(self.rightscore), False, "center", font=('Arial', 15, 'normal'))
        self.goto(-100, 260)
        self.write(str(self.leftscore), False, "center", font=('Arial', 15, 'normal'))