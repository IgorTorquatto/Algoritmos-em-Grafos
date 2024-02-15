import pygame
from constantes import *
class Jogador:
    def __init__(self, posicao_inicial):
        self.posicao = posicao_inicial
        self.vida = 100
        self.ataque = 50
        self.tesouro_capturado = 0
        self.tesouro_transportado = 0

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
        pygame.draw.circle(screen, VERMELHO, ilha.vertices[self.posicao], 20)
