import time

import pygame
from constantes import *
from Onca import Onca
from Crocodilo import Crocodilo
from Planta import Planta
from Formiga import Formiga
from Adaga import Adaga
from Pistola import Pistola
from Espada import Espada
from AreiaMovediça import AreiaMovedica
from GasVenenoso import GasVenenoso
from PVenenosa import PVenenosa

class Barra:
    def __init__(self,tela,ilha,jogador):
        self.tela= tela
        self.ilha = ilha
        self.jogador = jogador

    def desenhar_barra(self,tela,jogador,ilha):
        fonte = pygame.font.Font(None,21)

        #Desenhar barra
        pygame.draw.rect(tela, PRETO,(0, 550, TELA_MENU_LARGURA, 300))  # inicio_x, inicio_y, largura_retangulo, altura_retangulo

        #Mensagens padrão que devem aparecer na barra
        #Topo
        mensagens = [
            "Informações",
            "Descrição do Vértice"
        ]

        #Seção de infos
        mensagens_jogador = [
            "Pontos de vida: "+ str(self.jogador.get_vida()),
            "Dano de ataque: " + str(self.jogador.get_ataque()),
            "Tesouro capturado: "+ str(self.jogador.get_tesouro_capturado()),
            "Tesouro transportado: "+ str(self.jogador.get_tesouro_transportado())
        ]

        mensagens_ilha = [
            "Número de inimigos: " + str(self.ilha.qtd_inimigos),
            "Quantidade de plantas: "+ str(self.ilha.qtd_plantas),
            "Quantidade de perigos: " +str(self.ilha.qtd_perigos),
            "Quantidade armas: " +str(self.ilha.qtd_armas)
        ]

        #Seção de descrição do vértice

        mensagem_vertice = [
            self.ilha.obter_descricao_vertice(jogador,ilha),
            ""
        ]

        #Mostrar Topo
        texto_topo = fonte.render(mensagens[0], True, BRANCO)  # Renderiza o texto "Informações"
        largura_texto, altura_texto = texto_topo.get_size()  # Obtém a largura e altura do texto renderizado
        posicao_x = (TELA_MENU_LARGURA - largura_texto) // 2  # Calcula a posição x centralizada
        posicao_y = 560  # Define a posição y como 560
        tela.blit(texto_topo, (posicao_x, posicao_y))  # texto, (posicao x , posicao y)

        #Mostar Seção de Infos do jogador:
        posicao_x_infos_jogador = 20
        posicao_y_infos_jogador = 580

        informacoes_jogador = fonte.render("Informações jogador -> ",True,BRANCO)
        tela.blit(informacoes_jogador, (posicao_x_infos_jogador, posicao_y_infos_jogador))

        posicao_x_infos_jogador += 180
        if(self.jogador.get_vida() < 50):
            texto_vida = fonte.render(mensagens_jogador[0], True, VERMELHO)
            tela.blit(texto_vida, (posicao_x_infos_jogador, posicao_y_infos_jogador))
            posicao_x_infos_jogador += 180
        elif(self.jogador.get_vida() == 50):
            texto_vida = fonte.render(mensagens_jogador[0], True, AMARELO)
            tela.blit(texto_vida, (posicao_x_infos_jogador, posicao_y_infos_jogador))
            posicao_x_infos_jogador += 180
        else:
            texto_vida = fonte.render(mensagens_jogador[0], True, VERDE)
            tela.blit(texto_vida, (posicao_x_infos_jogador, posicao_y_infos_jogador))
            posicao_x_infos_jogador += 180

        for i in range(1,4):
            texto = fonte.render(mensagens_jogador[i],True,BRANCO)
            tela.blit(texto,(posicao_x_infos_jogador,posicao_y_infos_jogador))
            posicao_x_infos_jogador+=180

        #Mostrar Seção de infos da ilha:

        posicao_x_infos_ilha = 20
        posicao_y_infos_ilha = 600

        informacoes_ilha = fonte.render("Informações ilha -> ", True, BRANCO)
        tela.blit(informacoes_ilha, (posicao_x_infos_ilha, posicao_y_infos_ilha))

        posicao_x_infos_ilha += 180

        for i in range(0,4):
            texto = fonte.render(mensagens_ilha[i],True,BRANCO)
            tela.blit(texto,(posicao_x_infos_ilha,posicao_y_infos_ilha))
            posicao_x_infos_ilha+=200

        #Mostrar Seção de descrição do vértice:
        texto_topo_2 = fonte.render(mensagens[1], True, BRANCO)  # Renderiza o texto "Informações"
        largura_texto_2, altura_texto_2 = texto_topo_2.get_size()  # Obtém a largura e altura do texto renderizado
        posicao_x_2 = (TELA_MENU_LARGURA - largura_texto_2) // 2  # Calcula a posição x centralizada
        posicao_y_2 =625  # Define a posição y como 560
        tela.blit(texto_topo_2, (posicao_x_2, posicao_y_2))  # texto, (posicao x , posicao y)

        descricao_vertice = fonte.render(mensagem_vertice[0],True,BRANCO)
        tela.blit(descricao_vertice,(20,650))

    #Recebe a tela, uma pergunta(string), imprime na barra a pergunta e devolve a resposta "S" ou "N"
    def perguntar_sim_ou_nao(self,tela,pergunta):
        resposta = None
        fonte = pygame.font.Font(None, 21)
        clock = pygame.time.Clock()

        while resposta not in ['S', 'N']:

            # Desenhar a pergunta na tela
            pergunta_texto = fonte.render(pergunta, True, LARANJA_PERGUNTA)
            tela.blit(pergunta_texto, (400,760))

            # Atualizar a tela
            pygame.display.flip()

            # Esperar um momento antes de verificar a entrada do usuário novamente
            clock.tick(30)

            # Verificar eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        resposta = 'S'
                    elif event.key == pygame.K_n:
                        resposta = 'N'

        return resposta

    def interagir_jogador(self,tela,ilha,jogador):

        posicao_jogador = jogador.get_posicao()
        resposta = None

        for elemento in ilha.grafo[posicao_jogador]:

            if isinstance(elemento, Onca):
                # Se encontrarmos uma instância de Onca na lista, realizamos a ação
                resposta = self.perguntar_sim_ou_nao(tela, "Quer batalhar contra a Onça? (S/N)")
                if resposta == "S":
                    print("batalhou contra Onca")
                if resposta == "N":
                    print("Nao batalhou contra Onca")
                    jogador.set_posicao((jogador.get_posicao() +1)) #move para o próx vértice

            elif isinstance(elemento,Crocodilo):
                # Se encontrarmos uma instância de Crocodilo na lista, realizamos a ação
                resposta = self.perguntar_sim_ou_nao(tela, "Quer batalhar contra o Crocodilo? (S/N)")
                if resposta == "S":
                    print("batalhou contra Crocodilo")
                if resposta == "N":
                    print("Nao batalhou contra Crocodilo")
                    jogador.set_posicao((jogador.get_posicao() + 1))  # move para o próx vértice

            elif isinstance(elemento,Formiga):
                # Se encontrarmos uma instância de Formiga na lista, realizamos a ação
                resposta = self.perguntar_sim_ou_nao(tela, "Quer batalhar contra as Formigas? (S/N)")
                if resposta == "S":
                    print("batalhou contra Formigas")
                if resposta == "N":
                    print("Nao batalhou contra Formigas")
                    jogador.set_posicao((jogador.get_posicao() + 1))  # move para o próx vértice

            elif isinstance(elemento,Planta):
                # Se encontrarmos uma instância de Planta na lista, realizamos a ação
                resposta = self.perguntar_sim_ou_nao(tela, "Quer consumir uma Planta? (S/N)")
                if resposta == "S":
                    print("Consumiu Planta")
                    jogador.consumir_planta(elemento,ilha)
                if resposta == "N":
                    print("Não consumiu planta")
                    jogador.set_posicao((jogador.get_posicao() + 1))  # move para o próx vértice

            elif isinstance(elemento,Espada):
                # Se encontrarmos uma instância de Planta na lista, realizamos a ação
                resposta = self.perguntar_sim_ou_nao(tela, "Quer pegar a Espada? (S/N)")
                if resposta == "S":
                    print("Pegou espada")
                if resposta == "N":
                    print("Não pegou espada")
                    jogador.set_posicao((jogador.get_posicao() + 1))  # move para o próx vértice

            elif isinstance(elemento, Adaga):
                # Se encontrarmos uma instância de Planta na lista, realizamos a ação
                resposta = self.perguntar_sim_ou_nao(tela, "Quer pegar a Adaga (S/N)")
                if resposta == "S":
                    print("Pegou adaga")
                if resposta == "N":
                    print("Não pegou adaga")
                    jogador.set_posicao((jogador.get_posicao() + 1))  # move para o próx vértice

            elif isinstance(elemento, Pistola):
                # Se encontrarmos uma instância de Planta na lista, realizamos a ação
                resposta = self.perguntar_sim_ou_nao(tela, "Quer pegar a Pistola? (S/N)")
                if resposta == "S":
                    print("Pegou pistola")
                if resposta == "N":
                    print("Não pegou pistola")
                    jogador.set_posicao((jogador.get_posicao() + 1))  # move para o próx vértice

            elif isinstance(elemento, AreiaMovedica):
                resposta = self.perguntar_sim_ou_nao(tela,"O seu jogador sofreu dano de Areia Movediça (S para continuar)")
                jogador.passar_perigo(elemento,ilha)

            elif isinstance(elemento, GasVenenoso):
                resposta = self.perguntar_sim_ou_nao(tela, "O seu jogador sofreu dano de Gás venenoso (S para continuar)")
                if resposta == "S":
                    jogador.passar_perigo(elemento,ilha)
                    jogador.set_posicao((jogador.get_posicao() + 1))

            elif isinstance(elemento, PVenenosa):
                resposta = self.perguntar_sim_ou_nao(tela, "O seu jogador sofreu dano de Planta Venenosa (S para continuar)")
                if resposta == "S":
                    jogador.passar_perigo(elemento, ilha)
                    jogador.set_posicao((jogador.get_posicao() + 1))






