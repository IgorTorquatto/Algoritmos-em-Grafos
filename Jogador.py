from constantes import *
from Planta import Planta
from collections import deque
from Relogio import Relogio
from Grafo import Grafo
from Vertice import Vertice
from Barra import Barra
from Tesouro import Tesouro

class Jogador:
    def __init__(self, ilha):
        self.ilha = ilha
        self.posicao = 0  # Posição inicial do jogador é o primeiro vértice da ilha
        self.vida = 100
        self.ataque = 50
        self.duracao_arma_atual = 0
        self.tesouro_transportado = 0
        self.tempo = 0
        self.visitados = [] #lista com a sequência de vértices visitados
        self.removidos = []
        self.fila = []
        self.pilha= set()

    def aumentar_vida(self,valor):
        if self.vida + valor > 100:
            self.vida = 100
        else:
            self.vida += valor
    def diminuir_vida(self,valor):
        self.vida-= valor

    def aumentar_dano_de_ataque(self,valor):
        self.ataque+=valor

    def aumentar_tesouro(self,valor):
        self.tesouro_transportado+= valor

    #Mover jogador entre todos os vértices e depois até a praia novamente pelo caminho mais curto:
    def mover_jogador(self,vertice: Vertice , grafo: Grafo):

        if ( len(self.visitados) == grafo.qtd_vertices):
            self.visitados.clear()
            self.mover_jogador(vertice,grafo)

        self.visitados.append(vertice)
        vizinhos_vertice_atual = grafo.grafo[vertice]

        for elemento in vizinhos_vertice_atual:
            if elemento not in self.visitados:
                self.posicao = elemento.indice
                return

    def mover_jogador_bfs(self, vertice: Vertice):
       vertice_removido= self.visitados.remove(vertice)
       self.removidos.append(vertice_removido) #Adicionar na lista de removidos
       proximo= self.visitados[0] #O proximo  vertice fica sendo o primeiro indice da lista
       self.posicao = proximo.indice

    def mover_jogador_dfs(self,vertice: Vertice):
        for i in self.pilha:
            print(i.indice)

    def BFS(self,ilha: Grafo, no: Vertice): # Usando python annotations para definir qual tipo de dados eu vou usar dos parãmetros

        #Adicionando nó recebido na função na fila e na lista de visitados
        self.visitados.append(no)
        self.fila.append(no)

        #Criando loop para visitar cada nó
        while len(self.fila) != 0 : # enquanto fila for diferente de vazio
            m = self.fila.pop(0) #Remove o primeiro elemento da fila ( O primeiro vértice da fila)
            for vizinho in ilha.grafo[m]: #Para cada vértice vizinho da lista de adjacências do vértice atual
                if vizinho not in self.visitados: #Se o vizinho ainda não foi visitado
                    self.visitados.append(vizinho)
                    self.fila.append(vizinho)

    def DFS(self,grafo: Grafo,no: Vertice):
        if no not in self.pilha:
            self.pilha.add(no)
            for vizinho in grafo.grafo[no]:
                self.DFS(grafo,vizinho)



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

    def consumir_planta(self,planta: Planta):
        numero_cura = planta.cura
        self.aumentar_vida(numero_cura)
        self.ilha.remover_planta(self.posicao,planta)

    def capturar_tesouro(self,tesouro: Tesouro):
        numero_tesouro = tesouro.valor
        self.aumentar_tesouro(numero_tesouro)
        self.ilha.remover_tesouro(self.posicao,tesouro)

    def sofrer_dano_perigo(self,perigo):
        numero_dano = perigo.dano
        self.diminuir_vida(numero_dano)
        self.ilha.remover_perigo(self.posicao,perigo)

