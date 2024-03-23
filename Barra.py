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
            "Pontos de vida: " +str(self.jogador.vida),
            "Dano de ataque: " + str(self.jogador.ataque),
            "Duracao Arma: "+ str(self.jogador.duracao_arma_atual),
            "Tesouro transportado: "+ str(self.jogador.tesouro_transportado)
        ]

        mensagens_ilha = [
            "Número de inimigos: " + str(self.ilha.qtd_inimigos),
            "Quantidade de plantas: "+ str(self.ilha.qtd_plantas),
            "Quantidade de perigos: " +str(self.ilha.qtd_perigos),
            "Quantidade armas: " +str(self.ilha.qtd_armas)
        ]

        #Seção de descrição do vértice

        mensagem_vertice = [
            self.ilha.obter_descricao_vertice(jogador),
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
        if(self.jogador.vida < 50):
            texto_vida = fonte.render(mensagens_jogador[0], True, VERMELHO)
            tela.blit(texto_vida, (posicao_x_infos_jogador, posicao_y_infos_jogador))
            posicao_x_infos_jogador += 180
        elif(self.jogador.vida == 50):
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

        descricao_vertice= ["","","","",""]
        if len(mensagem_vertice[0]) >0:
            quantidade_de_descricoes = len(mensagem_vertice[0])
            posicao_descricao_y = 650
            for i in range(0,quantidade_de_descricoes):
                descricao_vertice[i] = fonte.render(mensagem_vertice[0][i], True, BRANCO)
                posicao_descricao_y+=18
                tela.blit(descricao_vertice[i], (20, posicao_descricao_y))
        else:
            descricao_vertice = fonte.render(mensagem_vertice[0][0],True,BRANCO)
            tela.blit(descricao_vertice,(20,650))

    def interagir_com_objeto(self):
        pass





