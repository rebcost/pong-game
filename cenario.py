from turtle import Screen, Turtle

class Cenario:
    def __init__(self):
        self.cenario = Screen()
        self.cenario.bgcolor("black")
        self.cenario.screensize(800, 600)
        self.cenario.title("Pong Game")

    def desenharBorda(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.speed("fastest")
        # Move para o ponto Inicial
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.bk(420)
        self.turtle.left(90)
        self.turtle.fd(320)
        self.turtle.right(90)
        # Desenha a borda
        self.turtle.pendown()
        self.turtle.fd(820)
        self.turtle.left(90)
        self.turtle.bk(620)
        self.turtle.left(90)
        self.turtle.fd(820)
        self.turtle.right(90)
        self.turtle.fd(620)
        
