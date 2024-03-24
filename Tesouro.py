import random

class Tesouro:

    def __init__(self):
        self.valor = random.choice([10,20,30,40,50,60,70,80,100])
        self.descricao = "Esse vértice contém " + str(self.valor) + " de tesouro ! Pressione C para capturar."