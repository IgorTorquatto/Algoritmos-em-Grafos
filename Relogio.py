from constantes import *

class Relogio:
    def __init__(self):
        self.time = 0
        self.font = pygame.font.SysFont(None, 30)

    def update_time(self):
        self.time += 1

    def draw(self, screen):
        text = self.font.render(f"Tempo: {self.time}", True, VERDE)
        screen.blit(text, (TELA_MENU_LARGURA - text.get_width() - 10, 10))