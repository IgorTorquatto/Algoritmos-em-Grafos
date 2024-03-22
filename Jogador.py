import pygame
from constantes import *
from Planta import Planta

class Jogador:
    def __init__(self, ilha):
        self.ilha = ilha
        self.posicao = 0  # Posição inicial do jogador é o primeiro vértice da ilha
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
        self.vida-= valor

    def aumentar_dano_de_ataque(self,valor):
        self.ataque+=valor

    def mover_para_cima(self):
        vizinhos = self.ilha.grafo[self.posicao]
        if self.posicao - COLUNAS in vizinhos:
            self.posicao -= COLUNAS

    def mover_para_baixo(self):
        vizinhos = self.ilha.grafo[self.posicao]
        if self.posicao + COLUNAS in vizinhos:
            self.posicao += COLUNAS

    def mover_para_esquerda(self):
        vizinhos = self.ilha.grafo[self.posicao]
        if self.posicao - 1 in vizinhos:
            self.posicao -= 1

    def mover_para_direita(self):
        vizinhos = self.ilha.grafo[self.posicao]
        if self.posicao + 1 in vizinhos:
            self.posicao += 1

    def desenhar_personagem(self, tela, ilha):
        posicao_x, posicao_y = ilha.vertices[self.posicao].posicao
        pygame.draw.circle(tela, VERMELHO, (posicao_x, posicao_y), 20)

    def consumir_planta(self, planta, ilha):
        self.aumentar_vida(planta.get_cura())  # Aumentar a vida do jogador com base na cura da planta
        ilha.grafo[self.posicao].remove(planta)  # Remover a planta consumida da lista do vértice
        ilha.diminui_planta(-1)  # Reduzir a quantidade de plantas na ilha

    def passar_perigo(self,perigo,ilha):
        self.diminuir_vida(perigo.get_dano())
        ilha.grafo[self.posicao].remove(perigo)
        ilha.diminui_perigo(-1)
