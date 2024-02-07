import  pygame

class Ilha:
    def __init__(self, vertices, arestas):
        self.vertices = vertices
        self.arestas = arestas

    def desenhar_ilha(self, screen):
        # Desenhe os vértices
        for vertice in self.vertices:
            pygame.draw.circle(screen, (0, 255, 0), vertice, 10)

        # Desenhe as arestas
        for vertice, vizinhos in self.arestas.items():
            for vizinho in vizinhos:
                pygame.draw.line(screen, (0, 255, 0), self.vertices[vertice], self.vertices[vizinho], 2)
