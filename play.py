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
    #barra = Barra(tela, ilha, jogador)  # barra para apresentar as informações dos eventos no grafo


    #Imprimir listas de adjacências (  MOSTRAR ISSO NA EXPLICAÇÃO PARA O PROF)
    print(ilha.grafo)
    ilha.imprimir_lista_adjacencias()
    ilha.imprimir_objetos_dos_vertices()
    #ilha.imprimir_matriz_adjacencias()

    relogio = Relogio()
    rodar = True
    resposta = None

    while rodar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False
            # Comandos jogador mover na ilha
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    jogador.mover_para_cima()
                elif event.key == pygame.K_DOWN:
                    jogador.mover_para_baixo()
                elif event.key == pygame.K_LEFT:
                    jogador.mover_para_esquerda()
                elif event.key == pygame.K_RIGHT:
                    jogador.mover_para_direita()


        # Atualizando o tempo a cada 10 segundos
        if pygame.time.get_ticks() % 5000 == 0:
             relogio.update_time()

        # Limpe a tela
        tela.fill(AZUL_CLARO)
        tela.blit(ILHA_FUNDO, (0, -100))

        # Desenhando o relógio na tela
        relogio.draw(tela)

        # Desenhe a ilha
        ilha.desenhar_ilha(tela)

        # Personagem
        jogador.desenhar_personagem(tela)
        jogador.mover_jogador(relogio)

        # Criar barra de informações
        # começando em 500 na y
       # barra.desenhar_barra(tela,jogador,ilha)

        # Atualize a tela
        pygame.display.update()


        #Condição de derrota
        #if (jogador.get_vida() == 0):
            # Adicionar tela de perdeu
           # print("Perdeu")
           # rodar = False

        #Interagir com o jogador de acordo com que tem no vértice que ele está
        #barra.interagir_jogador(tela,ilha,jogador)

    # Encerre o Pygame
    pygame.quit()
    sys.exit()
