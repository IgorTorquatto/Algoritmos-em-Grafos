import  pygame
from constantes import *

class Ilha:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas

    def desenhar_ilha(self, screen):
        # Desenhe os vértices
        for vertice in self.vertices:
            pygame.draw.circle(screen, VERDE, vertice, 10)

        # Desenhe as arestas
        for vertice, vizinhos in self.arestas.items():
            for vizinho in vizinhos:
                pygame.draw.line(screen, VERDE, self.vertices[vertice], self.vertices[vizinho], 2)
