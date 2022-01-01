from turtle import Turtle

class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        
    def desenhaPaddle(self, pos):        
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)

    def origin(self):
        self.clear()
        self.desenhaPaddle()