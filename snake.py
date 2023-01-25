from turtle import Turtle


POSICAO_INICIAL = [(0, -0), (-20, 0), (-40, 0)]
MOVER_DISTANCIA = 7

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Coordenadas para direção da cobra
class Cobra:
    def __init__(self):
        self.posicoes = []
        self.criar_cobra()
        self.direcao = self.posicoes[0]

    # Configuração da cobra
    def criar_cobra(self):
        for posicao in POSICAO_INICIAL:
            self.adicionar_seguimento(posicao)

    def adicionar_seguimento(self, posicao):
        cobra = Turtle(shape="square")
        cobra.color("white")
        cobra.penup()
        cobra.goto(posicao)
        self.posicoes.append(cobra)

    def extender(self):
        # Aumenta o tamanho da cobra a cada ponto
        self.adicionar_seguimento(self.posicoes[-1].position())


    # coordenadas da cobra
    def mover(self):
        for posicao_numero in range(len(self.posicoes) - 1, 0, -1):
            nova_posicao_x = self.posicoes[posicao_numero - 1].xcor()
            nova_posicao_y = self.posicoes[posicao_numero - 1].ycor()
            self.posicoes[posicao_numero].goto(nova_posicao_x, nova_posicao_y)
            self.direcao.forward(MOVER_DISTANCIA)

    def up(self):
        self.direcao.setheading(UP)

    def down(self):
        self.direcao.setheading(DOWN)

    def left(self):
        self.direcao.setheading(LEFT)

    def right(self):
        self.direcao.setheading(RIGHT)


