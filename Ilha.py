import pygame
from constantes import *
from Onca import Onca
from Crocodilo import Crocodilo
from Formiga import Formiga
from Planta import Planta
import random


class Ilha:
        def __init__(self):
            self.qtd_vertices = LINHAS * COLUNAS #Criar um grafo tabuleiro 5*5
            self.qtd_inimigos = 0
            self.qtd_plantas = 0
            self.grafo = {v: [] for v in range(self.qtd_vertices)}
            #inicializa o atributo grafo com um dicionário em que as chaves são os números de 1 até qtd_vertices (que representa o número total de vértices no grafo) e os valores são listas vazias.
            # Isso cria a estrutura básica para armazenar a lista de adjacências do grafo, que será atualizada conforme as arestas são adicionadas.
            # Cada vértice do grafo é representado como uma chave no dicionário, e cada chave tem uma lista associada a ela. Essa lista pode conter vários objetos,
             # e esses objetos são os elementos armazenados nos vértices do grafo.
            self.arestas = []  # Lista para armazenar todas as arestas do grafo
            #cada aresta na lista self.arestas é representada como uma tupla contendo dois números, que são os índices dos vértices que a aresta conecta.
            # O primeiro número na tupla é o índice do vértice de origem e o segundo número é o índice do vértice de destino.

        def get_arestas(self):
            return self.arestas
        def get_qtd_vertices(self):
            return self.qtd_vertices

        def set_qtd_inimigos(self,quantidade_inimigos):
            self.qtd_inimigos = quantidade_inimigos

        def set_qtd_plantas(self,quantidade_plantas):
            self.qtd_plantas = quantidade_plantas

        def get_qtd_inimigos(self):
            return self.qtd_inimigos

        def adicionar_objeto(self, vertice, objeto):
            if vertice in self.grafo:
                self.grafo[vertice].append(objeto)
            else:
                print(f"Erro: Vértice {vertice} não existe no grafo.")
        def remover_objeto(self, vertice, objeto):
            if objeto in self.grafo[vertice]:
                self.grafo[vertice].remove(objeto)
            else:
                print(f"Objeto {objeto} não encontrado no vértice {vertice}.")

        def associar_posicoes_aos_vertices(self):
            posicao_vertices = []  # conjunto de posicoes (x,y) dos vértices
            qtd_vertices = self.qtd_vertices

            espacamento_x = TELA_MENU_LARGURA // (COLUNAS + 1)
            espacamento_y = 100

            for linha in range(LINHAS):
                for coluna in range(COLUNAS):
                    x = (coluna * espacamento_x) + 200
                    y = (linha * espacamento_y) + 100
                    posicao_vertices.append((x, y))

            '''Todo vértice é representado por uma chave ( numero do vertice) e o seu valor( o que contém em cada vértice) , o valor do vértice é uma lista
            Essa lista pode conter objetos que são os elementos que estão no vértice, porém a primeira posição dessa lista sempre armazenará a posição daquele vértice na tela
            Associar posições aos vértices no grafo'''
            for vertice in range(qtd_vertices): #de 0 a 24
                # Atribuir a posição ao primeiro elemento da lista de cada vértice
                self.grafo[vertice].insert(0, posicao_vertices[vertice])

        def construir_arestas(self):
            for vertice in range(self.qtd_vertices):
                linha, coluna = vertice // COLUNAS, vertice % COLUNAS

                # Vizinho à esquerda
                if coluna > 0:
                    vizinho_esquerda = vertice - 1
                    self.arestas.append((vertice, vizinho_esquerda))
                # Vizinho à direita
                if coluna < COLUNAS - 1:
                    vizinho_direita = vertice + 1
                    self.arestas.append((vertice, vizinho_direita))
                # Vizinho acima
                if linha > 0:
                    vizinho_cima = vertice - COLUNAS
                    self.arestas.append((vertice, vizinho_cima))
                # Vizinho abaixo
                if linha < LINHAS - 1:
                    vizinho_baixo = vertice + COLUNAS
                    self.arestas.append((vertice, vizinho_baixo))
        def desenhar_ilha(self, tela):

            #Para cada vértice do grafo, já que sabemos que cada indice do grafo é um vértice que contém uma lista e que em cada índice 0 da lista está a posição
            #(x,y) do vértice podemos simplesmente fazer um laço de repetição e percorrer todos os vértices desenhando eles na tela
            for vertice in range(self.qtd_vertices):
                #Desenha vértices
                pygame.draw.circle(tela, MARROM, self.grafo[vertice][0], 10)

            # Desenha arestas
            for aresta in self.arestas:
                pygame.draw.line(tela, MARROM, self.grafo[aresta[0]][0], self.grafo[aresta[1]][0], 2)
                # Esta linha desenha uma linha entre dois vértices do grafo na tela, usando as posições (x, y) desses vértices.

        def distribuir_inimigos(self):
            qtd_inimigos_inicial = 0
            vertices_utilizados = set()  # Conjunto para armazenar vértices já utilizados

            while qtd_inimigos_inicial < self.qtd_inimigos:
                indice_vertice_aleatorio = random.randint(0,
                                                          self.qtd_vertices - 1)  # Distribui inimigos em vértices aleatórios
                if indice_vertice_aleatorio not in vertices_utilizados:
                    inimigo = random.choice([Onca(), Crocodilo(), Formiga()])
                    self.adicionar_objeto(indice_vertice_aleatorio, inimigo)  # Adiciona o inimigo ao vértice
                    vertices_utilizados.add(indice_vertice_aleatorio)
                    qtd_inimigos_inicial += 1

        def distribuir_plantas(self):
            qtd_plantas_inicial = 0
            vertices_utilizados = set()  # Conjunto para armazenar vértices já utilizados

            while qtd_plantas_inicial < self.qtd_plantas:
                indice_vertice_aleatorio = random.randint(0, self.qtd_vertices - 1)
                if indice_vertice_aleatorio not in vertices_utilizados:
                    planta = Planta()
                    self.adicionar_objeto(indice_vertice_aleatorio, planta)
                    vertices_utilizados.add(indice_vertice_aleatorio)
                    qtd_plantas_inicial += 1

        def obter_descricao_vertice(self,jogador):
            vertice_atual = jogador.get_posicao()
            if vertice_atual in self.grafo:
                objetos_vertice = self.grafo[vertice_atual]
                if len(objetos_vertice) > 1:
                    # Se houver mais de um objeto no vértice (além da posição), acessa a descrição do segundo elemento
                    descricao = objetos_vertice[1].descricao
                    return descricao
            return "Nenhum recurso neste vértice"

        def imprimir_matriz_adjacencias(self):
            matriz_adjacencias = [[0] * self.qtd_vertices for _ in range(self.qtd_vertices)]

            # Preenche a matriz de adjacências
            for i in range(self.qtd_vertices):
                for j in range(self.qtd_vertices):
                    if (i, j) in self.arestas or (j, i) in self.arestas:
                        matriz_adjacencias[i][j] = 1

            # Imprime a matriz de adjacências
            for linha in matriz_adjacencias:
                print(linha)

        def imprimir_arestas(self):
            for aresta in self.arestas:
                print(f"Aresta: {aresta[0]} - {aresta[1]}")

