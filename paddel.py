from turtle import Turtle, Screen


class Paddel(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)



    def up(self):
        current_y= self.ycor()
        self.goto(self.xcor(),current_y +20)


    def down(self):
        current_y = self.ycor()
        self.goto(self.xcor(), current_y-20)


    def refresh(self,position):
        self.goto(position)





