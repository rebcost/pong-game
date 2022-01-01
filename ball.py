from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def mover(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def rebater_y(self):        
        self.y_move *= -1
        
    def rebater_x(self):   
        self.x_move *= -1
        self.move_speed *= 0.9

    def resetPosicao(self):
        self.move_speed = 0.1
        self.home()
        self.rebater_x()