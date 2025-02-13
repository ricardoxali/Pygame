import pygame
import random

pygame.init()

# Configurações da tela
cell_size = 32
maze_width = 41
maze_height = 21
screen_width = maze_width * cell_size
screen_height = maze_height * cell_size

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Inicializa a tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Labirinto")

# Carregar imagens de cada cor
imagens_cores = {
    "r": pygame.image.load("vermelho.png"),
    "g": pygame.image.load("vermelho.png"),
    "b": pygame.image.load("vermelho.png"),
    "c": pygame.image.load("vermelho.png"),
    "m": pygame.image.load("vermelho.png"),
    "y": pygame.image.load("vermelho.png"),
}

# Posições das imagens (ajuste conforme necessário)
posicoes_cores = {
    "r": (screen_width // 2 - 200, screen_height // 2),
    "g": (screen_width // 2 - 100, screen_height // 2),
    "b": (screen_width // 2, screen_height // 2),
    "c": (screen_width // 2 - 200, screen_height // 2 + 100),
    "m": (screen_width // 2 - 100, screen_height // 2 + 100),
    "y": (screen_width // 2, screen_height // 2 + 100),
}

# Criar o labirinto (1 = parede, 0 = caminho)
maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]
direcoes = [(0, -2), (0, 2), (-2, 0), (2, 0)]

def gerar_maze(x, y):
    maze[y][x] = 0
    random.shuffle(direcoes)
    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        if 0 < nx < maze_width - 1 and 0 < ny < maze_height - 1 and maze[ny][nx] == 1:
            maze[ny - dy // 2][nx - dx // 2] = 0
            gerar_maze(nx, ny)

# Gera o labirinto e cria a saída no canto inferior direito
gerar_maze(1, 1)
maze[maze_height - 2][maze_width - 1] = 0
maze[maze_height - 2][maze_width - 2] = 0

def desenhar_maze():
    for y in range(maze_height):
        for x in range(maze_width):
            cor = branco if maze[y][x] == 0 else preto
            pygame.draw.rect(screen, cor, (x * cell_size, y * cell_size, cell_size, cell_size))

def tela_abertura():
    fonte_titulo = pygame.font.Font(None, 50)
    fonte_texto = pygame.font.Font(None, 30)

    titulo = fonte_titulo.render("OBJETIVO:", True, branco)
    objetivo = fonte_texto.render("ESCAPAR DO LABIRINTO NO MENOR TEMPO POSSÍVEL", True, branco)
    escolha_cor = fonte_titulo.render("ESCOLHA A COR DO SEU PERSONAGEM:", True, branco)

    rodando = True
    cor_jogador = None

    while rodando:
        screen.fill(preto)
        desenhar_maze()

        # Criar sobreposição preta semi-transparente
        overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))  # Preto com transparência
        screen.blit(overlay, (0, 0))

        # Desenhar textos
        screen.blit(titulo, (screen_width // 2 - titulo.get_width() // 2, 50))
        screen.blit(objetivo, (screen_width // 2 - objetivo.get_width() // 2, 100))
        screen.blit(escolha_cor, (screen_width // 2 - escolha_cor.get_width() // 2, 180))

        # Desenhar imagens das opções de cores
        for tecla, imagem in imagens_cores.items():
            screen.blit(imagem, posicoes_cores[tecla])

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.unicode in imagens_cores:
                    cor_jogador = event.unicode
                    rodando = False

    return cor_jogador

# Chama a tela de abertura
cor_selecionada = tela_abertura()

# Agora o jogo pode continuar usando 'cor_selecionada' como a cor do personagem
print(f"Cor selecionada: {cor_selecionada}")
