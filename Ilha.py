import pygame
from constantes import *
from Onca import Onca
from Crocodilo import Crocodilo
from Formiga import Formiga
from Planta import Planta
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
        qtd_inimigos = 0
        vertices_utilizados = set()  # Conjunto para armazenar vértices já utilizados

        while qtd_inimigos < 5:  # Distribuir 5 inimigos
            indice_vertice_aleatorio = random.randint(1, 25)
            if indice_vertice_aleatorio not in self.recursos_por_vertice and indice_vertice_aleatorio not in vertices_utilizados:
                inimigo = random.choice([Onca(), Crocodilo(), Formiga()])
                self.recursos_por_vertice[indice_vertice_aleatorio] = [inimigo]
                vertices_utilizados.add(indice_vertice_aleatorio)
                qtd_inimigos += 1
       # print(qtd_inimigos)

    def distribuir_plantas(self):
        qtd_plantas = 0
        vertices_utilizados = set()  # Conjunto para armazenar vértices já utilizados

        while qtd_plantas < 5:  # Distribuir 5 plantas
            indice_vertice_aleatorio = random.randint(1, 25)
            if indice_vertice_aleatorio not in self.recursos_por_vertice and indice_vertice_aleatorio not in vertices_utilizados:
                planta = Planta()
                self.recursos_por_vertice[indice_vertice_aleatorio] = [planta]
                vertices_utilizados.add(indice_vertice_aleatorio)
                qtd_plantas += 1
        #print(qtd_plantas)

    def obter_descricao_vertice(self):
        vertice_atual = self.jogador.posicao
        if vertice_atual in self.recursos_por_vertice:
            recurso = self.recursos_por_vertice[vertice_atual][0]  # Acessar o primeiro item da lista
            descricao = recurso.descricao
            return descricao
        else:
            return "Nenhum recurso neste vértice"
