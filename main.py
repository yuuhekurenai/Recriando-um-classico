from turtle import Screen
import time
from snake import Cobra
from comida import Alimento
from placar import Placar

#Configurações da tela

tela = Screen()
tela.setup(width=600, height=600)
tela.title("Cobrinha Classica")
tela.bgcolor("black")
tela.tracer(0)

snake = Cobra()
ponto = Alimento()
score = Placar()

tela.listen()
tela.onkey(snake.up, "Up")
tela.onkey(snake.down, "Down")
tela.onkey(snake.left, "Left")
tela.onkey(snake.right, "Right")

#Configuração da animaçãO
seguir = True
while seguir:
    tela.update()
    time.sleep(0.1)

    snake.mover()

    #Detecta o contato com a comida
    if snake.direcao.distance(ponto) < 15:
        ponto.resetar()
        snake.extender()
        score.acrescentar_ponto()

    #Detecta colisao com a parede
    if snake.direcao.xcor() > 280 or snake.direcao.ycor() > 280 or snake.direcao.xcor() < -280 or snake.direcao.ycor() < -280 :
        score.colisao()
        seguir = False

""" #Detecta a colisão com a calda
    for aproximacao in snake.posicoes:
        if snake.direcao.distance(aproximacao) < 10:
            score.colisao()
            seguir = False"""






tela.exitonclick()