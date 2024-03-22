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
        self.tempo = 0

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

    def mover_jogador(self, relogio):
        tempo_do_relogio = relogio.time
        if tempo_do_relogio != self.tempo:
            self.tempo = tempo_do_relogio
            # Acessar os índices dos vizinhos do vértice atual
            vertice_atual = self.ilha.vertices[self.posicao]
            vizinhos_vertice_atual = self.ilha.grafo[vertice_atual] #lista com vizinhos do vértice atual
            if vizinhos_vertice_atual:
                proximo_vertice_indice = random.choice(vizinhos_vertice_atual).indice # Movendo de forma aleatoria
                self.posicao = proximo_vertice_indice



    def desenhar_personagem(self, tela):
        posicao_x, posicao_y = self.ilha.vertices[self.posicao].posicao
        pygame.draw.circle(tela, VERMELHO, (posicao_x, posicao_y), 20)


