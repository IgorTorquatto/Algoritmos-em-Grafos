# Trabalho Algoritmos em Grafos 2023.2

Para executar o jogo , siga as instruções abaixo:

### Pré-requisitos
- Certifique-se de ter o Python instalado em seu sistema. Você pode baixar e instalar o Python em [python.org](https://www.python.org/).
- Instale a biblioteca Pygame. Você pode instalar o Pygame usando o pip, executando o seguinte comando no terminal:

```python
pip install pygame
```

### Execução
1. Baixe o repositório.
2. Abra um terminal e navegue até o diretório onde o arquivo `main.py` está localizado.
3. Execute o seguinte comando para iniciar o jogo:

```python
python main.py
```

### Como Jogar
- A medida que o jogador caminha entre os vértices do grafo, que são pontos da ilha, a seção de descrição do vértice indica qual tecla o jogador deve pressionar em seu teclado para interagir com os objetos do vértice.
- Durante o jogo, o jogador percorrerá todos os vértices da ilha e voltará para a praia. Ao chegar na praia o jogador **deve** pressionar a tecla *space* para embarcar e deixar a ilha com máximo de tesouro coletado.
- A ilha possui vários objetos como criaturas, perigos ,plantas medicinais, tesouros e armas. Todos os valores de tesouro são escolhidos de forma aleatória. Todos os objetos são distribuídos nos vértices de forma aleatória também.
- O principal objetivo do jogador é coletar o máximo de tesouro possível e retornar à praia.
- Ao sofrer dano, a capacidade de coletar um novo tesouro reduzirá a menos que o jogador consiga se curar consumindo uma planta medicinal. O tesouro que estava com o jogador no momento que sofre dano também reduzirá. Todas as regras de redução, em porcentagem, seguem as especificações do projeto.
- Além disso, durante o jogo, o jogador receberá informações e instruções na interface gráfica do Pygame e no prompt de comando.
- Caso morra o jogador tem direito a voltar a um checkpoint somente uma vez. Os vértices 0 e 12 do grafo são esses vértices especiais. Porém, só serão restaurados seus pontos de vida e sua posição no último checkpoint, objetos que ele carregava antes de morrer como armas não serão recuperados.

### Comandos na Ilha

- Se o jogador estiver em um vértice com adaga, teclar `a` para pegar.
- Se estiver em um vértice com espada, teclar `e` para pegar.
- Para pistola, teclar `p`.
- Para planta medicinal, teclar `espaço`.
- Se o jogador estiver na praia, teclar `espaço` para embarcar e encerrar o jogo.
- Se estiver em um vértice com criatura, teclar `s` para duelar ou `n` para fugir.
- Em um vértice com perigo, teclar `s` para receber o dano e ir para o próximo vértice.
- Se estiver em um vértice com tesouro, teclar `c` para capturar.


### Saídas
- Durante a execução, o prompt de comando exibirá informações como a matriz de adjacências, lista de adjacências, lista de vértices e outras informações relevantes do que vai acontecendo durante o jogo.
- A interface gráfica do Pygame é a principal forma de mostrar ao jogador o que está acontecendo na ilha/grafo enquando ele joga.

### Autores
- Este jogo foi desenvolvido por Cicero Igor e Lucas Silva.
- Este trabalho faz parte do curso de Algoritmos em Grafos da Universidade Federal do Cariri.


#### Informações importantes:
- O jogo foi desenvolvido usando uma tela de tamanho 21,45" e resolução 1920×1080. Portanto, ao executar em uma computador com tela menor do que isso algumas informações podem não ser exibidas corretamente, mas um vídeo da execução do programa completo estará anexado junto com a entrega desse trabalho.

- A implementação de todas as funcionalidades do jogo acompanhou as especificações do projeto Algoritmos em Grafos passadas pelo professor.


Divirta-se explorando a Ilha! 🏝🎮

