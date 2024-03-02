import pygame
from constantes import *
from Planta import Planta

class Jogador:
    def __init__(self, ilha):
        self.posicao = list(ilha.grafo.keys())[0] #transforma o dict de grafo em lista e pega o primeiro indice
        self.vida = 100
        self.ataque = 50
        self.tesouro_capturado = 0
        self.tesouro_transportado = 0

    def get_posicao(self):
        return self.posicao

    def set_posicao(self,nova_posicao):
        self.posicao = nova_posicao

    def get_vida(self):
        return self.vida

    def get_ataque(self):
        return self.ataque

    def get_tesouro_capturado(self):
        return self.tesouro_capturado

    def get_tesouro_transportado(self):
        return self.tesouro_transportado

    def aumentar_vida(self,valor):
        if self.vida + valor > 100:
            self.vida = 100
        else:
            self.vida += valor

    def diminuir_vida(self,valor):
        self.vida-=valor

    def aumentar_dano_de_ataque(self,valor):
        self.ataque+=valor

    def mover_para_cima(self, ilha):
        if self.posicao - COLUNAS >= 0:
            self.posicao -= COLUNAS

    def mover_para_baixo(self, ilha):
        if self.posicao + COLUNAS < COLUNAS * LINHAS:
            self.posicao += COLUNAS

    def mover_para_esquerda(self, ilha):
        if self.posicao % COLUNAS != 0:
            self.posicao -= 1

    def mover_para_direita(self, ilha):
        if (self.posicao + 1) % COLUNAS != 0:
            self.posicao += 1

    def desenhar_personagem(self, tela, ilha):
       pygame.draw.circle(tela, VERMELHO, ilha.grafo[self.posicao][0], 20)  # passamos a chave (self.posicao -> que é o vertice onde o jogador está) e o indice 0 da lista desse vertice (onde se encontra a posição (x,y) a ser impressa

    def consumir_planta(self,planta):
        self.aumentar_vida(planta.get_cura()) #tem que passar um valor que é a cura da planta
        planta.descricao = "Planta consumida"
