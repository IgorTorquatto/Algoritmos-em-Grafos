import pygame
from constantes import *
from Onca import Onca
from Crocodilo import Crocodilo
from Formiga import Formiga
from Planta import Planta

class Barra_infos:
    def __init__(self,tela,ilha):
        self.tela= tela
        self.ilha = ilha

    def desenhar_barra(self, tela):
        fonte = pygame.font.Font(None, 22)
        # Informações do personagem
        informacoes_personagem = "Informações do personagem:"
        vida_personagem = "Pontos de vida: {}".format(self.ilha.jogador.vida)
        dano_ataque = "Dano de ataque: {}".format(self.ilha.jogador.ataque)
        tesouro_capturado = "Tesouro capturado: {}".format(self.ilha.jogador.tesouro_capturado)
        tesouro_transportado = "Tesouro transportado: {}".format(self.ilha.jogador.tesouro_transportado)

        # Detalhes da ilha
        informacoes_ilha = "Detalhes da ilha:"
        # Contagem do número de inimigos e plantas disponíveis na ilha
        numero_inimigos = sum(1 for recurso in self.ilha.recursos_por_vertice.values() if
                              isinstance(recurso[0], (Onca, Crocodilo, Formiga)))
        numero_plantas = sum(1 for recurso in self.ilha.recursos_por_vertice.values() if isinstance(recurso[0], Planta))
        quantidade_perigos = "Quantidade de inimigos: {}".format(numero_inimigos)
        quantidade_plantas = "Quantidade de plantas: {}".format(numero_plantas)

        descricao_vertice = self.ilha.obter_descricao_vertice()

        texto_informacoes_personagem = fonte.render(informacoes_personagem, True, BRANCO)
        texto_vida_personagem = fonte.render(vida_personagem, True, BRANCO)
        texto_dano_ataque = fonte.render(dano_ataque, True, BRANCO)
        texto_tesouro_capturado = fonte.render(tesouro_capturado, True, BRANCO)
        texto_tesouro_transportado = fonte.render(tesouro_transportado, True, BRANCO)

        texto_informacoes_ilha = fonte.render(informacoes_ilha, True, BRANCO)
        texto_quantidade_perigos = fonte.render(quantidade_perigos, True, BRANCO)
        texto_quantidade_plantas = fonte.render(quantidade_plantas, True, BRANCO)

        texto_descricao_vertice = fonte.render(descricao_vertice, True, BRANCO)

        # dimensões dos textos
        largura_texto_informacoes_personagem, altura_texto_informacoes_personagem = fonte.size(informacoes_personagem)
        largura_texto_vida_personagem, altura_texto_vida_personagem = fonte.size(vida_personagem)
        largura_texto_dano_ataque, altura_texto_dano_ataque = fonte.size(dano_ataque)
        largura_texto_tesouro_capturado, altura_texto_tesouro_capturado = fonte.size(tesouro_capturado)
        largura_texto_tesouro_transportado, altura_texto_tesouro_transportado = fonte.size(tesouro_transportado)

        largura_texto_informacoes_ilha, altura_texto_informacoes_ilha = fonte.size(informacoes_ilha)
        largura_texto_quantidade_perigos, altura_texto_quantidade_perigos = fonte.size(quantidade_perigos)
        largura_texto_quantidade_plantas, altura_texto_quantidade_plantas = fonte.size(quantidade_plantas)

        largura_texto_descricao_vertice, altura_texto_descricao_vertice = fonte.size(descricao_vertice)

        pygame.draw.rect(tela, PRETO,
                         (0, 560, TELA_MENU_LARGURA, 300))  # inicio_x, inicio_y, largura_retangulo, altura_retangulo

        # posição dos textos na barra
        texto_x_informacoes_personagem = 20
        texto_y_informacoes_personagem = 570

        texto_x_vida_personagem = 20
        texto_y_vida_personagem = texto_y_informacoes_personagem + altura_texto_informacoes_personagem + 10
        texto_x_dano_ataque = 200
        texto_y_dano_ataque = texto_y_informacoes_personagem + altura_texto_informacoes_personagem + 10
        texto_x_tesouro_capturado = 380
        texto_y_tesouro_capturado = texto_y_informacoes_personagem + altura_texto_informacoes_personagem + 10
        texto_x_tesouro_transportado = 580
        texto_y_tesouro_transportado = texto_y_informacoes_personagem + altura_texto_informacoes_personagem + 10

        texto_x_informacoes_ilha = 20
        texto_y_informacoes_ilha = texto_y_tesouro_transportado + altura_texto_tesouro_transportado + 20

        texto_x_quantidade_perigos = 20
        texto_y_quantidade_perigos = texto_y_informacoes_ilha + altura_texto_informacoes_ilha + 10
        texto_x_quantidade_plantas = 230
        texto_y_quantidade_plantas = texto_y_informacoes_ilha + altura_texto_informacoes_ilha + 10

        texto_x_descricao_vertice = 20
        texto_y_descricao_vertice = texto_y_quantidade_perigos + altura_texto_quantidade_perigos + 20

        # Desenhe os textos na tela
        tela.blit(texto_informacoes_personagem, (texto_x_informacoes_personagem, texto_y_informacoes_personagem))
        tela.blit(texto_vida_personagem, (texto_x_vida_personagem, texto_y_vida_personagem))
        tela.blit(texto_dano_ataque, (texto_x_dano_ataque, texto_y_dano_ataque))
        tela.blit(texto_tesouro_capturado, (texto_x_tesouro_capturado, texto_y_tesouro_capturado))
        tela.blit(texto_tesouro_transportado, (texto_x_tesouro_transportado, texto_y_tesouro_transportado))

        tela.blit(texto_informacoes_ilha, (texto_x_informacoes_ilha, texto_y_informacoes_ilha))
        tela.blit(texto_quantidade_perigos, (texto_x_quantidade_perigos, texto_y_quantidade_perigos))
        tela.blit(texto_quantidade_plantas, (texto_x_quantidade_plantas, texto_y_quantidade_plantas))
        tela.blit(texto_descricao_vertice, (texto_x_descricao_vertice, texto_y_descricao_vertice))


