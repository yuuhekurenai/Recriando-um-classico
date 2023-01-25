from turtle import Turtle

FONTE= "courier"
TAMANHO = 15
TIPO = "bold"

class Placar(Turtle):
    def __init__(self):
        super().__init__()
        self.contagem = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.atualizar_placar()
        self.hideturtle()

    def atualizar_placar(self):
        self.write(f"Pontuação {self.contagem}", move=False, align="center", font=(FONTE, TAMANHO, TIPO))

    def acrescentar_ponto(self):
        self.contagem += 1
        self.clear()
        self.atualizar_placar()

    def colisao(self):
        self.goto(0,0)
        self.write("VOCÊ PERDEU!", move=False, align="center", font=(FONTE, TAMANHO, TIPO))

