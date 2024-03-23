import sys
from constantes import *
from Grafo import Grafo
from Jogador import Jogador
from Relogio import Relogio
from Barra import Barra

def iniciar_jogo(tela):

    ilha = Grafo()  # Inicializa o grafo da ilha
    ilha.preencher_grafo()

    ilha.qtd_inimigos = 5 #definindo quantidade de inimigos
    ilha.qtd_plantas = 5 #definindo quantidade de plantas
    ilha.qtd_armas = 3 #definindo quantidade de armas
    ilha.qtd_perigos = 3 #definindo quantidade de perigos na ilha

    pygame.mixer.music.stop()
    pygame.mixer.music.load(MUSICA_JOGO)
    pygame.mixer.music.play(-1)

    # Definir posições dos vértices (x,y) para mostrar na tela
    ilha.associar_posicoes_aos_vertices()

    # Distribuir inimigos,plantas,armas...
    ilha.distribuir_plantas()
    ilha.distribuir_inimigos()
    ilha.distribuir_armas()
    ilha.distribuir_perigos()

    #Jogador
    jogador = Jogador(ilha)
    barra = Barra(tela, ilha, jogador)  # barra para apresentar as informações dos eventos no grafo


    #Imprimir listas de adjacências (  MOSTRAR ISSO NA EXPLICAÇÃO PARA O PROF)
    print(ilha.grafo)
    ilha.imprimir_lista_adjacencias()
    ilha.imprimir_objetos_dos_vertices()
    #ilha.imprimir_matriz_adjacencias()

    relogio = Relogio()
    rodar = True
    resposta = None
    tempo_anterior = pygame.time.get_ticks()

    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
            # Comandos jogador mover na ilha
            #elif event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_UP:
                 #   jogador.mover_para_cima()
                 #elif event.key == pygame.K_DOWN:
                    #jogador.mover_para_baixo()
                 #elif event.key == pygame.K_LEFT:
                 #   jogador.mover_para_esquerda()
                 #elif event.key == pygame.K_RIGHT:
                 #   jogador.mover_para_direita()

        # Verifique se passaram 5 segundos
        tempo_atual = pygame.time.get_ticks()
        if (tempo_atual - tempo_anterior) >= 5000:  # 5 segundos em milissegundos
            relogio.update_time()
            tempo_anterior = tempo_atual

        # Limpe a tela
        tela.fill(AZUL_CLARO)
        tela.blit(ILHA_FUNDO, (0, -100))

        # Desenhando o relógio na tela
        relogio.draw(tela)

        # Desenhe a ilha
        ilha.desenhar_ilha(tela)

        # Personagem
        jogador.desenhar_personagem(tela)

        #Descomentar essa linha para movimentos automáticos:
        #jogador.mover_jogador(relogio)

        #Movimentar jogador com base em BFS:
        indice_vertice_jogador_esta= jogador.posicao
        vertice_jogador_esta = ilha.vertices[indice_vertice_jogador_esta]
        pygame.time.delay(2000)
        jogador.BFS(ilha,vertice_jogador_esta,relogio)

        # print(ilha.grafo[vertice_jogador_esta]) teste isso tem os vizinhos do vertice

        # Criar barra de informações
        # começando em 500 na y
        barra.desenhar_barra(tela,jogador,ilha)

        # Atualize a tela
        pygame.display.update()

        #Condição de derrota
        if ((jogador.vida == 0) or (relogio.tempo_atual == relogio.tempo_limite)):
            print("Perdeu")
            rodar = False

    # Encerre o Pygame
    pygame.quit()
    sys.exit()
