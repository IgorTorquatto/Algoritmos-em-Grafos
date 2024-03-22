import pygame
from constantes import *
from Onca import Onca
from Crocodilo import Crocodilo
from Formiga import Formiga
from Planta import Planta
from Adaga import Adaga
from Pistola import Pistola
from Espada import Espada
from AreiaMovediça import AreiaMovedica
from GasVenenoso import GasVenenoso
from PVenenosa import PVenenosa
from Vertice import Vertice
import random


class Grafo:
        def __init__(self):
            self.qtd_vertices = LINHAS * COLUNAS
            self.vertices = [Vertice(i) for i in range(self.qtd_vertices)]
            self.qtd_inimigos = 0
            self.qtd_plantas = 0
            self.qtd_armas = 0
            self.qtd_perigos = 0
            self.grafo = {i: [] for i in range(self.qtd_vertices)}
            self.preencher_grafo()

        def adicionar_aresta(self, u, v):
            if v not in self.grafo[u]:
                self.grafo[u].append(v)
            if u not in self.grafo[v]:
                self.grafo[v].append(u)

        def adicionar_objeto(self, vertice, objeto):
            if vertice in self.grafo:
                self.grafo[vertice].append(objeto)
            else:
                print("Erro: Vértice inválido.")

        def preencher_grafo(self):
            for i in range(self.qtd_vertices):
                linha = i // COLUNAS
                coluna = i % COLUNAS
                vizinhos = []
                if linha > 0:
                    vizinhos.append(i - COLUNAS)
                if linha < LINHAS - 1:
                    vizinhos.append(i + COLUNAS)
                if coluna > 0:
                    vizinhos.append(i - 1)
                if coluna < COLUNAS - 1:
                    vizinhos.append(i + 1)
                for vizinho in vizinhos:
                    self.adicionar_aresta(i, vizinho)

            # Atualizar o dicionário grafo com os vértices corretos
            for vertice in self.vertices:
                self.grafo[vertice.indice] = [vizinho for vizinho in self.grafo[vertice.indice]]

        #Função para testar se todos os indices foram associados corretamente
        def imprimir_indices_vertices(self):
            for vertice in self.vertices:
                print(f"Índice do vértice: {vertice.indice}")

        def associar_posicoes_aos_vertices(self):
            posicao_vertices = []  # conjunto de posicoes (x,y) dos vértices

            espacamento_x = TELA_MENU_LARGURA // (COLUNAS + 1)
            espacamento_y = 100

            for linha in range(LINHAS):
                for coluna in range(COLUNAS):
                    x = (coluna * espacamento_x) + 200
                    y = (linha * espacamento_y) + 100
                    posicao_vertices.append((x, y))

            for i, vertice in enumerate(self.vertices):  # de 0 a 24
                vertice.posicao = posicao_vertices[i]

        def desenhar_ilha(self, tela):

            for vertice in range(self.qtd_vertices):
                # Desenha vértices
                pygame.draw.circle(tela, MARROM, self.vertices[vertice].posicao, 10)

            for vertice, vizinhos in self.grafo.items():
                for vizinho in vizinhos:
                    # Desenha uma linha entre o vértice atual e seu vizinho
                    pygame.draw.line(tela, MARROM, self.vertices[vertice].posicao, self.vertices[vizinho].posicao, 2)

        def distribuir_plantas(self):
            vertices = list(range(1, self.qtd_vertices))  # Lista de todos os vértices possíveis
            random.shuffle(vertices)  # Embaralha os vértices

            # Distribui as plantas entre os vértices
            for i in range(min(self.qtd_plantas, len(vertices))):
                vertice = vertices[i]
                planta = Planta()  # Supondo que Planta seja a classe dos objetos de planta
                self.adicionar_objeto(vertice, planta)