import pygame
from constantes import *
class Jogador:
    def __init__(self, posicao_inicial):
        self.posicao = posicao_inicial

    def mover_esquerda(self, ilha):
        if self.posicao in ilha.arestas and ilha.arestas[self.posicao]:
            self.posicao = ilha.arestas[self.posicao][0]

    def mover_direita(self, ilha):
        if self.posicao in ilha.arestas and len(ilha.arestas[self.posicao]) > 1:
            self.posicao = ilha.arestas[self.posicao][1]

    def desenhar_personagem(self, screen, ilha):
        pygame.draw.circle(screen, VERMELHO, ilha.vertices[self.posicao], 20)
