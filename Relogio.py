from constantes import *

class Relogio:
    def __init__(self):
        self.fonte = pygame.font.SysFont(None, 30)
        self.tempo_atual = 0  # Inicializa o tempo
        self.tempo_limite = 3 * 25

    def update_time(self):
        # Atualiza o tempo a cada 5 segundos
        self.tempo_atual += 1

    def draw(self, tela):
        texto = self.fonte.render(f"Tempo: {self.tempo_atual}", True, VERDE)
        texto2 = self.fonte.render(f"Tempo Limite: {self.tempo_limite}", True, VERMELHO)
        tela.blit(texto, (10, 10))
        tela.blit(texto2, (750, 10))