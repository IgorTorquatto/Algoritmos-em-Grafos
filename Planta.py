class Planta:
    def __init__(self):
        self.cura = 30
        self.descricao = "Planta[CURA "+str(self.cura)+"]: útil para fazer chá e recuperar pontos de vida. Pressione espaço para consumir"

    def get_cura(self):
        return self.cura