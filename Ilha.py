import pygame
from constantes import *
from Onca import Onca
from Crocodilo import Crocodilo
import random


class Ilha:
    def __init__(self, vertices, arestas, jogador):
        self.vertices = vertices
        self.arestas = arestas
        self.jogador = jogador
        self.recursos_por_vertice = {}

    def desenhar_ilha(self, screen):
        # Desenhe os vértices
        for vertice in self.vertices:
            pygame.draw.circle(screen, MARROM, vertice, 10)

        # Desenhe as arestas
        for vertice, vizinhos in self.arestas.items():
            for vizinho in vizinhos:
                pygame.draw.line(screen, MARROM, self.vertices[vertice], self.vertices[vizinho], 2)

    def distribuir_inimigos(self):
        inimigos = [Onca(), Crocodilo()]

        for vertice in range(1,25):

            inimigo = random.choice(inimigos)
            # Adicione o inimigo ao vértice
            self.recursos_por_vertice[vertice] = [inimigo]

    def obter_descricao_vertice(self):
        vertice_atual = self.jogador.posicao
        if vertice_atual in self.recursos_por_vertice:
            recurso = self.recursos_por_vertice[vertice_atual][0]  # Acessar o primeiro item da lista
            descricao = recurso.descricao
            return descricao
        else:
            return "Nenhum recurso neste vértice"
