import pygame
from constantes import *

class Barra_infos:
    def __init__(self,tela):
        self.tela= tela

    def desenhar_barra(self,tela):
         fonte = pygame.font.Font(None, 36)  # Fonte padrão com tamanho 36
         texto = fonte.render("Informações: ", True, BRANCO)

         # dimensões do texto
         largura_texto, altura_texto = fonte.size("Informações: ")

         pygame.draw.rect(tela,PRETO,(0,600,TELA_MENU_LARGURA,300)) #inicio_x,inicio_y,largura_retangulo,altura_retangulo

         #posição do texto dentro do retângulo
         texto_x = 0 + (TELA_MENU_LARGURA - largura_texto) // 2
         texto_y = 620

         # Desenhe o texto na tela
         tela.blit(texto, (texto_x, texto_y))
