import pygame
from constantes import *
from Planta import Planta

class Jogador:
    def __init__(self, posicao_inicial):
        self.posicao = posicao_inicial
        self.vida = 100
        self.ataque = 50
        self.tesouro_capturado = 0
        self.tesouro_transportado = 0

    def get_posicao(self):
        return self.posicao

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

    def desenhar_personagem(self, screen, ilha):
       pygame.draw.circle(screen, VERMELHO, ilha.grafo[self.posicao][0], 20)  # ilha.grafo[self.posicao][0] o primiero indice é o [vertice] o segundo indice é a [posicao daquele vertice]

    def consumir_planta(self,ilha,planta):
        self.aumentar_vida(planta.get_cura()) #tem que passar um valor que é a cura da planta
        planta.descricao = "Planta consumida"
