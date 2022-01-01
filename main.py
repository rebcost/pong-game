# Criar o screen
from turtle import Screen, Turtle
from ball import Ball
from cenario import Cenario
from paddle import Paddle
from time import sleep
from scoreboard import ScoreBoard


screen = Screen()
cenario = Cenario()

screen.tracer(0)
cenario.desenharBorda()

# Mostrar o scoreboard
score = ScoreBoard()

# Desenha Paddle
r_paddle = Paddle()
r_paddle.desenhaPaddle((350,0))

l_paddle = Paddle()
l_paddle.desenhaPaddle((-350,0))

# Desenha bola
ball = Ball()

# Mapeamento de teclas
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down, "s")

gameON = True
while gameON: 
    screen.update()
    sleep(ball.move_speed)   
    ball.mover()

    # Dectando colisão com a parede de cima e a debaixo
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.rebater_y()

    # Detectando a colisão com o r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.rebater_x()

    # Detectando se a bola ultrapassar o r_paddle :
    if ball.xcor() > 380:
        score.l_point()
        ball.resetPosicao()

    # Detectando se a bola ultrapassar o l_paddle :
    if ball.xcor() < -380:
        score.r_point()
        ball.resetPosicao()

screen.exitonclick()