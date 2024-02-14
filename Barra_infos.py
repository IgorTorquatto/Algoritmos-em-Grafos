import pygame
from constantes import *

class Barra_infos:
    def __init__(self,tela,ilha):
        self.tela= tela
        self.ilha = ilha

    def desenhar_barra(self,tela):
        fonte = pygame.font.Font(None, 20)
        texto = fonte.render("Informações: " + self.ilha.obter_descricao_vertice(), True, BRANCO)

        # dimensões do texto
        largura_texto, altura_texto = fonte.size("Informações: " + self.ilha.obter_descricao_vertice())

        pygame.draw.rect(tela, PRETO,
                         (0, 600, TELA_MENU_LARGURA, 300))  # inicio_x, inicio_y, largura_retangulo, altura_retangulo

        # posição do texto dentro do retângulo
        texto_x = 0 + (TELA_MENU_LARGURA - largura_texto) // 2
        texto_y = 620

        # Desenhe o texto na tela
        tela.blit(texto, (texto_x, texto_y))
