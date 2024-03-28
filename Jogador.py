from constantes import *
from Planta import Planta
from collections import deque
from Relogio import Relogio
from Grafo import Grafo
from Vertice import Vertice
from Barra import Barra
from Tesouro import Tesouro
from Pistola import Pistola
from Adaga import Adaga
from Espada import Espada
class Jogador:
    def __init__(self, ilha):
        self.ilha = ilha
        self.posicao = 0  # Posição inicial do jogador é o primeiro vértice da ilha
        self.vida = 100
        self.ataque = 50
        self.arma = False
        self.nome_arma = "Nenhum"
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

        if (len(self.visitados) == grafo.qtd_vertices): # Quando chega no último vértice limpa a lista de visitados e começa a mover o jogador novamente a partir do último vértice
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

        # O jogador captura a quantidade de tesouro baseado no seu percentual de vida atual:

        numero_tesouro_total = tesouro.valor  # Valor do tesouro total
        quantidade_vida_jogador = self.vida  # Valor da vida atual do jogador
        percentual_vida_jogador = quantidade_vida_jogador / 100  # Calcula o percentual de vida do jogador com base na vida máxima que é 100

        # Calcula o número de tesouro capturado baseado no percentual de vida do jogador
        numero_tesouro_capturado = numero_tesouro_total * percentual_vida_jogador

        self.aumentar_tesouro(numero_tesouro_capturado)
        self.ilha.remover_tesouro(self.posicao, tesouro)

    def sofrer_dano_perigo(self,perigo):

        #Após sofrer dano por um perigo a quantidade de tesouro deve ser atualizada
        #Exemplo: caso possua 70 pontos de vida e já esteja voltado à praia, mas perde 10 pontos de vida, então retornará com 60% do tesouro à praia
        #Ou seja essa função deve atualizar o tesouro transportado após sofrer dano

        numero_tesouro_antes_dano = self.tesouro_transportado
        numero_dano = perigo.dano
        self.diminuir_vida(numero_dano) # Reduz a vida

        vida_apos_dano = self.vida
        percentual_vida_apos_dano = vida_apos_dano / 100

        #Atualizar novo numero do tesouro transportado
        numero_tesouro_atualizado = numero_tesouro_antes_dano * percentual_vida_apos_dano

        self.tesouro_transportado = numero_tesouro_atualizado
        print(f"Você tinha {numero_tesouro_antes_dano} de tesouro  e sofreu {numero_dano}  de dano logo seu novo numero de tesouro será {numero_tesouro_atualizado} ")
        self.ilha.remover_perigo(self.posicao,perigo)

    def equipar_arma(self,arma):

        dano_arma = arma.dano
        dano_de_ataque_base = 50

        self.arma = True
        self.ataque= dano_arma + dano_de_ataque_base
        self.duracao_arma_atual = arma.duracao
        self.nome_arma = arma.nome

        self.ilha.remover_arma(self.posicao,arma)

    def batalhar(self,inimigo,tela,turnos,vertice_jogador):

        turnos_duelo = turnos
        vertice_que_o_jogador_esta = vertice_jogador
        print("O duelo irá começar")
        fonte = pygame.font.Font(None, 25)
        print(vertice_que_o_jogador_esta)
        print(vertice_que_o_jogador_esta.indice)
        print(vertice_que_o_jogador_esta.objetos)

        #Imprimir que o duelo vai começar
        print("O duelo está acontecendo no turno: "+ str(turnos_duelo))


        pygame.draw.rect(tela, PRETO, (0, 765, TELA_MENU_LARGURA, 500))
        mensagem = fonte.render("Duelo[Turnos:"+str(turnos_duelo)+"] vida-jogador["+str(self.vida)+"] vida-criatura["+str(inimigo.vida)+"] vez do jogador (S-> continuar)", True,AMARELO)
        tela.blit(mensagem, (TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
        pygame.display.flip()


        esperando_resposta = True
        while esperando_resposta:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                            #Vez do jogador:
                            inimigo.vida= inimigo.vida - self.ataque

                            #Verifica se a criatura morreu:
                            if(inimigo.vida <= 0 ):
                                print("Você matou " + inimigo.nome)
                                vertice_que_o_jogador_esta.objetos.remove(inimigo)
                                print(inimigo.nome + "removido de vértice" + str(vertice_que_o_jogador_esta.indice))
                                self.ilha.qtd_inimigos = self.ilha.qtd_inimigos-1
                                self.posicao = vertice_que_o_jogador_esta.indice
                                return

                            turnos_duelo = turnos_duelo -1
                            esperando_resposta = False


        print("O duelo está acontecendo no turno: " + str(turnos_duelo))
        pygame.draw.rect(tela, PRETO, (0, 765, TELA_MENU_LARGURA, 500))
        mensagem = fonte.render(
            "Duelo[Turnos:" + str(turnos_duelo) + "] vida-jogador[" + str(self.vida) + "] vida-criatura[" + str(
                inimigo.vida) + "] vez da criatura (S-> continuar)", True, AMARELO)
        tela.blit(mensagem, (TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
        pygame.display.flip()

        esperando_resposta = True
        while esperando_resposta:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        # Vez da Criatura:
                        self.vida = self.vida - inimigo.ataque

                        # Verifica se o jogador morreu:
                        if (self.vida <= 0):
                            print("Você morreu no duelo contra"+inimigo.nome)
                            self.posicao = vertice_que_o_jogador_esta.indice
                            return

                        turnos_duelo = turnos_duelo - 1
                        esperando_resposta = False

        print("O duelo está acontecendo no turno: " + str(turnos_duelo))
        pygame.draw.rect(tela, PRETO, (0, 765, TELA_MENU_LARGURA, 500))
        mensagem = fonte.render(
            "Duelo[Turnos:" + str(turnos_duelo) + "] vida-jogador[" + str(self.vida) + "] vida-criatura[" + str(
                inimigo.vida) + "] vez do jogador (S-> continuar)", True, AMARELO)
        tela.blit(mensagem, (TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
        pygame.display.flip()

        esperando_resposta = True
        while esperando_resposta:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        # Vez do jogador:
                        inimigo.vida = inimigo.vida - self.ataque

                        # Verifica se a criatura morreu:
                        if (inimigo.vida <= 0):
                            print("Você matou "+inimigo.nome)
                            vertice_que_o_jogador_esta.objetos.remove(inimigo)
                            print(inimigo.nome+"removido de vértice"+str(vertice_que_o_jogador_esta.indice))
                            self.ilha.qtd_inimigos = self.ilha.qtd_inimigos - 1
                            self.posicao = vertice_que_o_jogador_esta.indice
                            return

                        turnos_duelo = turnos_duelo - 1
                        esperando_resposta = False

        print("O duelo chegou no turno: " + str(turnos_duelo))
        if(turnos_duelo == 0):
            self.posicao = vertice_que_o_jogador_esta.indice
            return


    def reviver(self):

        #Reviver em 0 | 12
        primeiro_check = [12,17,22,3,8,13,18,23,4,9,14,19,24]
        segundo_check = [0,5,10,15,20,1,6,11,16,21,2,7,12]


        #Reviver o jogador

        if(self.posicao not in segundo_check):
            self.posicao = 12
        if(self.posicao not in primeiro_check):
            self.visitados.clear()
            self.posicao = 0


        self.vida = 100
        self.ataque = 50
        self.arma = False
        self.nome_arma = "Nenhum"
        self.duracao_arma_atual = 0

        print("Jogador gastou um checkpoint!")

        return False