import sys

import pygame

from constantes import *
from Grafo import Grafo
from Jogador import Jogador
from Relogio import Relogio
from Barra import Barra
from Planta import Planta
from Vertice import Vertice
from Tesouro import Tesouro
from AreiaMovediça import AreiaMovedica
from PVenenosa import  PVenenosa
from GasVenenoso import GasVenenoso

def iniciar_jogo(tela):

    ilha = Grafo()  # Inicializa o grafo da ilha
    ilha.preencher_grafo()

    ilha.qtd_inimigos = 5 #definindo quantidade de inimigos
    ilha.qtd_plantas = 5 #definindo quantidade de plantas
    ilha.qtd_armas = 3 #definindo quantidade de armas
    ilha.qtd_perigos = 3 #definindo quantidade de perigos na ilha
    ilha.qtd_tesouros = 5 #defininfo quantidade de tesouros

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
    ilha.distribuir_tesouros()

    #Jogador
    jogador = Jogador(ilha)
    barra = Barra(tela, ilha, jogador)  # barra para apresentar as informações dos eventos no grafo


    #Imprimir listas de adjacências (  MOSTRAR ISSO NA EXPLICAÇÃO )
    print(ilha.grafo)
    ilha.imprimir_matriz_adjacencias()
    ilha.imprimir_lista_adjacencias()
    ilha.imprimir_objetos_dos_vertices()


    relogio = Relogio()
    rodar = True
    tempo_anterior = pygame.time.get_ticks()
    fonte = pygame.font.Font(None, 25)

    while rodar:
        #Sempre capturar o vertice atual que o jogador está:
        vertice_atual = ilha.acessar_vertice_por_indice(jogador.posicao)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodar = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    if (jogador.posicao == 0):

                        mensagem = fonte.render("Você está na praia e tem " +str(jogador.tesouro_transportado)+" de tesouro, deseja finalizar o jogo (S/N)?", True, AMARELO)
                        tela.blit(mensagem,(TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
                        pygame.display.flip()

                        # Espere pela resposta do usuário
                        esperando_resposta = True
                        while esperando_resposta:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_s:
                                        print("Você terminou o jogo com "+ str(jogador.tesouro_transportado)+" de tesouro")
                                        rodar = False
                                        esperando_resposta = False
                                    elif event.key == pygame.K_n:
                                        esperando_resposta = False
                                        break

                    planta = None
                    if any(isinstance(objeto,Planta) for objeto in vertice_atual.objetos):
                        mensagem = fonte.render("Você tem " + str(jogador.vida) + " de vida deseja consumir a planta (S/N)?", True, AMARELO)
                        tela.blit(mensagem, (TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
                        pygame.display.flip()

                        # Espere pela resposta do usuário
                        esperando_resposta = True
                        while esperando_resposta:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_s:
                                        for objeto in vertice_atual.objetos:
                                            if isinstance(objeto,Planta):
                                                planta = objeto
                                        if planta is not None:
                                            jogador.consumir_planta(planta)
                                        esperando_resposta = False
                                    elif event.key == pygame.K_n:
                                        esperando_resposta = False
                                        break

                elif event.key == pygame.K_c:
                    tesouro = None
                    if any(isinstance(objeto, Tesouro) for objeto in vertice_atual.objetos):
                        mensagem = fonte.render(
                            "Você tem " + str(jogador.tesouro_transportado) + " de tesouro deseja capturar o tesouro desse vértice (S/N)?", True, AMARELO)
                        tela.blit(mensagem, (TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
                        pygame.display.flip()

                        # Espere pela resposta do usuário
                        esperando_resposta = True
                        while esperando_resposta:
                            for event in pygame.event.get():
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_s:
                                        for objeto in vertice_atual.objetos:
                                            if isinstance(objeto, Tesouro):
                                                tesouro = objeto
                                        if tesouro is not None:
                                            jogador.capturar_tesouro(tesouro)
                                        esperando_resposta = False
                                    elif event.key == pygame.K_n:
                                        esperando_resposta = False
                                        break



        # Limpe a tela
        tela.fill(AZUL_CLARO)
        tela.blit(ILHA_FUNDO, (0, -100))

        # Desenhando o relógio na tela
        relogio.draw(tela)

        # Desenhe a ilha
        ilha.desenhar_ilha(tela)

        # Personagem
        jogador.desenhar_personagem(tela)

        #Aplicar busca em largura para ter uma lista da sequência de nós que devem ser visitados
        #jogador.BFS(ilha, vertice_atual)
        #jogador.DFS(ilha,vertice_atual)

        # Verifique se passaram 5 segundos
        tempo_atual = pygame.time.get_ticks()
        if (tempo_atual - tempo_anterior) >= 5000:  # 5 segundos em milissegundos
            relogio.update_time()
            tempo_anterior = tempo_atual
            # Mover jogador com base na busca em largura
            #jogador.mover_jogador_bfs(vertice_atual)
            jogador.mover_jogador(vertice_atual, ilha)


        # Criar barra de informações
        # começando em 500 na y
        barra.desenhar_barra(tela,jogador,ilha)

        # Atualize a tela
        pygame.display.update()

        #Condição de derrota
        if ((jogador.vida == 0) or (relogio.tempo_atual == relogio.tempo_limite)):
            if(jogador.vida == 0):
                 print("Perdeu porque a vida do jogador chegou em 0")
            elif(relogio.tempo_atual == relogio.tempo_limite):
                print("Perdeu porque o tempo expirou")
            rodar = False

        for objeto in vertice_atual.objetos:

            gasVenenoso = None
            if isinstance(objeto,GasVenenoso):

                mensagem = fonte.render("Esse vértice possui um perigo seu jogador sofrerá o dano se for a primeira passagem (Pressione S para continuar)",True, AMARELO)
                tela.blit(mensagem, (TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
                pygame.display.flip()

                # Espere pela resposta do usuário
                esperando_resposta = True
                while esperando_resposta:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s:
                                for objeto in vertice_atual.objetos:
                                    if isinstance(objeto, GasVenenoso):
                                        gasVenenoso = objeto
                                if gasVenenoso is not None:
                                    jogador.sofrer_dano_perigo(gasVenenoso)
                                esperando_resposta = False
                            elif event.key == pygame.K_UNKNOWN:
                                esperando_resposta = False
                                break

            pVenenosa = None
            if isinstance(objeto,PVenenosa):


                mensagem = fonte.render( "Esse vértice possui um perigo seu jogador sofrerá o dano se for a primeira passagem (Pressione S para continuar)",  True, AMARELO)
                tela.blit(mensagem, (TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
                pygame.display.flip()

                # Espere pela resposta do usuário
                esperando_resposta = True
                while esperando_resposta:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s:
                                for objeto in vertice_atual.objetos:
                                    if isinstance(objeto, PVenenosa):
                                        pVenenosa = objeto
                                if pVenenosa is not None:
                                    jogador.sofrer_dano_perigo(pVenenosa)
                                esperando_resposta = False
                            elif event.key == pygame.K_UNKNOWN:
                                esperando_resposta = False
                                break

            areiaMovedica = None
            if isinstance(objeto,AreiaMovedica):


                mensagem = fonte.render("Esse vértice possui um perigo seu jogador sofrerá o dano se for a primeira passagem (Pressione S para continuar)",True, AMARELO)
                tela.blit(mensagem, (TELA_MENU_LARGURA // 2 - mensagem.get_width() // 2, 765))
                pygame.display.flip()

                # Espere pela resposta do usuário
                esperando_resposta = True
                while esperando_resposta:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_s:
                                for objeto in vertice_atual.objetos:
                                    if isinstance(objeto, AreiaMovedica):
                                        areiaMovedica = objeto
                                if areiaMovedica is not None:
                                    jogador.sofrer_dano_perigo(areiaMovedica)
                                esperando_resposta = False
                            elif event.key == pygame.K_UNKNOWN:
                                esperando_resposta = False
                                break


    # Encerre o Pygame
    pygame.quit()
    sys.exit()
