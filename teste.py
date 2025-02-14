import pygame
import random

pygame.init()

# Definições básicas
cell_size = 32
maze_width = 41
maze_height = 21
screen_width = maze_width * cell_size
screen_height = maze_height * cell_size

# Cores
white = (255, 255, 255)
black = (0, 0, 0)

# Configuração da tela
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Labirinto')

# Labirinto
maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]  # 1 = parede, 0 = caminho
direcoes = [(0, -2), (0, 2), (-2, 0), (2, 0)]  # Cima, Baixo, Esquerda, Direita

def gerar_maze(x, y):
    """Gera um labirinto aleatório com profundidade, garantindo caminhos conectados."""
    maze[y][x] = 0
    random.shuffle(direcoes)
    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        if 0 < nx < maze_width - 1 and 0 < ny < maze_height - 1 and maze[ny][nx] == 1:
            maze[ny - dy // 2][nx - dx // 2] = 0  # Remove parede entre células
            gerar_maze(nx, ny)

def garantir_caminho_saida():
    """Garante um caminho da entrada (1,1) até a saída."""
    x, y = 1, 1
    caminho = [(x, y)]
    while (y, x) != (maze_height - 2, maze_width - 2):
        random.shuffle(direcoes)
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 1 <= nx < maze_width - 1 and 1 <= ny < maze_height - 1 and maze[ny][nx] == 0:
                caminho.append((nx, ny))
                x, y = nx, ny
                break
    for cx, cy in caminho:
        maze[cy][cx] = 0  # Garante o caminho

def desenhar_maze():
    """Desenha o labirinto na tela."""
    for y in range(maze_height):
        for x in range(maze_width):
            cor = white if maze[y][x] == 0 else black
            pygame.draw.rect(screen, cor, (x * cell_size, y * cell_size, cell_size, cell_size))

def tela_abertura():
    """Exibe a tela de abertura com opções de cor."""
    fundo = pygame.Surface([screen_width, screen_height])
    fundo.fill((0, 0, 0))
    fundo.set_alpha(190)
    screen.blit(fundo, (0, 0))

    font_bold = pygame.font.SysFont('Arial', 38, bold=True)
    objetivo = font_bold.render('OBJETIVO:', True, white)
    x = (screen_width // 2) - objetivo.get_width() // 2
    screen.blit(objetivo, (x, 35))

    font = pygame.font.SysFont('Arial', 35)
    explicacao = font.render('ESCAPAR DO LABIRINTO NO', True, white)
    explicacao1 = font.render('MENOR TEMPO QUE CONSEGUIR', True, white)
    screen.blit(explicacao, ((screen_width // 2) - explicacao.get_width() // 2, 100))
    screen.blit(explicacao1, ((screen_width // 2) - explicacao1.get_width() // 2, 150))

    escolha = font_bold.render('ESCOLHA A COR DO SEU PERSONAGEM:', True, white)
    screen.blit(escolha, ((screen_width // 2) - escolha.get_width() // 2, 270))

    # Cores
    red = pygame.image.load('imagens\\red.png')
    green = pygame.image.load('imagens\\green.png')
    blue = pygame.image.load('imagens\\blue.png')
    cyan = pygame.image.load('imagens\\cyan.png')
    magenta = pygame.image.load('imagens\\magenta.png')
    yellow = pygame.image.load('imagens\\yellow.png')

    x = (screen_width // 2) - green.get_width() // 2
    screen.blit(green, (x, 330))
    screen.blit(magenta, (x, 500))
    screen.blit(red, (x - 150, 330))
    screen.blit(cyan, (x - 150, 500))
    screen.blit(blue, (x + 150, 330))
    screen.blit(yellow, (x + 150, 500))

def cor_jogador():
    """Aguarda a escolha da cor do jogador e retorna a cor selecionada."""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return 'r'
                if event.key == pygame.K_g:
                    return 'g'
                if event.key == pygame.K_b:
                    return 'b'
                if event.key == pygame.K_c:
                    return 'c'
                if event.key == pygame.K_m:
                    return 'm'
                if event.key == pygame.K_y:
                    return 'y'

# Gerando o labirinto e garantindo o caminho
gerar_maze(1, 1)
garantir_caminho_saida()

# Criando a saída fixa
maze[maze_height - 2][maze_width - 1] = 0
maze[maze_height - 2][maze_width - 2] = 0

# Variáveis de controle
mostrar_abertura = True
cor_escolhida = None

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    desenhar_maze()

    if mostrar_abertura:
        tela_abertura()
        pygame.display.flip()  # Atualiza a tela para exibir opções antes da escolha
        cor_escolhida = cor_jogador()
        mostrar_abertura = False  # Remove a tela de abertura após a escolha

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
