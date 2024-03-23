from constantes import *
from Planta import Planta
from collections import deque
from Relogio import Relogio
from Grafo import Grafo
from Vertice import Vertice

class Jogador:
    def __init__(self, ilha):
        self.ilha = ilha
        self.posicao = 0  # Posição inicial do jogador é o primeiro vértice da ilha
        self.vida = 100
        self.ataque = 50
        self.duracao_arma_atual = 0
        self.tesouro_transportado = 0
        self.tempo = 1

    def aumentar_vida(self,valor):
        if self.vida + valor > 100:
            self.vida = 100
        else:
            self.vida += valor
    def diminuir_vida(self,valor):
        self.vida-= valor

    def aumentar_dano_de_ataque(self,valor):
        self.ataque+=valor

    '''def mover_jogador(self, relogio):
        tempo_do_relogio = relogio.tempo_atual
        if tempo_do_relogio != self.tempo:
            self.tempo = tempo_do_relogio
            # Acessar os índices dos vizinhos do vértice atual
            vertice_atual = self.ilha.vertices[self.posicao]
            vizinhos_vertice_atual = self.ilha.grafo[vertice_atual] #lista com vizinhos do vértice atual
            if vizinhos_vertice_atual:
                proximo_vertice_indice = random.choice(vizinhos_vertice_atual).indice # Movendo de forma aleatoria
                self.posicao = proximo_vertice_indice'''

    def BFS(self,ilha: Grafo, no: Vertice,relogio: Relogio): # Usando python annotations para definir qual tipo de dados eu vou usar dos parãmetros

        #Pegando tempo do relógio atual
        tempo_do_relogio = relogio.tempo_atual

        #Inicialiando lista para os nós visitados e a fila
        visitados = []  # List for visited nodes.
        fila = []  # Initialize a queue

        #Adicionando nó recebido na função na fila e na lista de visitados
        visitados.append(no)
        fila.append(no)

        #Criando loop para visitar cada nó
        # while len(fila) != 0 : # enquanto fila for diferente de vazio
        m = fila.pop(0) #Remove o primeiro elemento da fila ( O primeiro vértice da fila)
        for vizinho in ilha.grafo[m]: #Para cada vértice vizinho da lista de adjacências do vértice atual
            if vizinho not in visitados: #Se o vizinho ainda não foi visitado
                visitados.append(vizinho)
                fila.append(vizinho)
                self.posicao = vizinho.indice



    '''def BFS(self, grafo: Grafo, no: Vertice,relogio: Relogio):  # Usando python annotations para definir qual tipo de dados eu vou usar dos parãmetros

        # Pegando tempo do relógio atual
        tempo_do_relogio = relogio.tempo_atual

        # Inicialização das estruturas de dados
        marca = {v: 'branco' for v in range(0,grafo.qtd_vertices)} #Marcando todos os vértices de branco
        fila = []

        #Marca  vertice de inicio de cinza
        marca[no.indice] = 'cinza'

        #Inicia fila F contendo apenas no atual
        fila.append(no.indice)

        while len(fila) != 0:

            w = fila.pop(0) #Remoção de F ; remove o indice do primeiro vertice da fila
            #preciso do indice do proximo vertice da lista de adjacencias do vertice com indice w e colocar em u
            vertice_atual = grafo.vertices[w]
            lista_vertices = grafo.grafo[vertice_atual] # lista com vertices da lista de adjacencias  do vertice com indice w
            u = lista_vertices[0].indice
            
            while u != None:
                if marca[u] == 'branco':
                    marca[u] = 'cinza'
                    fila.append(u)
                #u deve receber o próximo indice de vertice dele mesmo
                vertice_atual_2 = grafo.vertices[u]
                lista_vertices_2 = grafo.grafo[vertice_atual_2]
                u=lista_vertices_2[0].indice
            marca[w] = 'preto' '''


    def desenhar_personagem(self, tela):
        posicao_x, posicao_y = self.ilha.vertices[self.posicao].posicao
        pygame.draw.circle(tela, VERMELHO, (posicao_x, posicao_y), 20)


