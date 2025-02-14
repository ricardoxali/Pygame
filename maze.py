import pygame
import random

pygame.init()

def gerar_maze(x, y):
  maze[y][x] = 0 # Cria o caminho
  random.shuffle(direcoes)
  for dx, dy in direcoes: # dx e dy = deslocamento horizontal e vertical
        nx = x + dx # Nova posição de x
        ny = y + dy # Nova posição de y
        if 0 < nx < maze_width - 1 and 0 < ny < maze_height - 1 and maze[ny][nx] == 1:
            maze[ny - dy // 2][nx - dx // 2] = 0  # Remove a parede entre células
            gerar_maze(nx, ny)

def garantir_caminho_saida():
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

def desenhar_maze(m):
  for y in range(maze_height):
      for x in range(maze_width):
          if maze[y][x] == 0:
            cor = white 
          else:
            cor = black
          pygame.draw.rect(screen, cor, (x * cell_size, y * cell_size, cell_size, cell_size))

def tela_abertura():
  # Fundo preto com transparência
  fundo = pygame.Surface([screen_width, screen_height])
  fundo.fill((0,0,0))
  fundo.set_alpha(190)
  screen.blit(fundo, (0,0))

  # Texto
  font_bold = pygame.font.SysFont('Arial', 38, bold = True)
  objetivo = font_bold.render(f'OBJETIVO:', True, white)
  x = (screen_width // 2) - objetivo.get_width() // 2
  screen.blit(objetivo, (x, 35))

  font = pygame.font.SysFont('Arial', 35)
  explicacao = font.render(f'ESCAPAR DO LABIRINTO NO', True, white)
  explicacao1 = font.render(f'MENOR TEMPO QUE CONSEGUIR', True, white)
  x = (screen_width // 2) - explicacao.get_width() // 2
  screen.blit(explicacao, (x, 100))
  x = (screen_width // 2) - explicacao1.get_width() // 2
  screen.blit(explicacao1, (x, 150))

  escolha = font_bold.render(f'ESCOLHA A COR DO SEU PERSONAGEM:', True, white)
  x = (screen_width // 2) - escolha.get_width() // 2
  screen.blit(escolha, (x, 270))

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
  x /= 2
  screen.blit(red, (x, 330))
  screen.blit(cyan, (x, 500))
  x += 2 * x
  screen.blit(blue, (x, 330))
  screen.blit(yellow, (x, 500))

def cor_jogador():
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

def mover_jogador(dx, dy):
    global player_x, player_y
    nx, ny = player_x + dx, player_y + dy
    if maze[ny][nx] == 0:  # Verifica se o próximo movimento é um caminho
        player_x, player_y = nx, ny

def cor_escolhida(a):
   if a == 'r':
      cor, light_cor = (255, 0, 0), (255, 125, 125)
  if a == 


cell_size = 32
maze_width = 41
maze_height = 21 
screen_width = maze_width * cell_size
screen_height = maze_height * cell_size

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red, light_red = (255, 0, 0), (255, 125, 125)
green, light_green = (0, 255, 0), (125, 255, 125)
blue, light_blue = (0, 0, 255), (125, 125, 255)
cyan, light_cyan = (0, 255, 255), (200, 255, 225)
magenta, light_magenta = (255, 0, 255), (255, 200, 255)
yellow, light_yellow = (255, 255, 0), (225, 255, 200)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Labirinto')

player_x, player_y = 1, 1  # Posição inicial do jogado

maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)] # 1 = parede; 0 = caminho;
direcoes = [
  (0, -2), # Cima
  (0, 2), # Baixo
  (-2, 0), # Esquerda
  (2, 0) # Direira
]

gerar_maze(1, 1) # Define o primeiro caminho (a entrada) na célula 1,1
garantir_caminho_saida()

# Saída fixa
maze[maze_height - 2][maze_width - 1] = 0  # Substitui a parede pela saída
maze[maze_height - 2][maze_width - 2] = 0  # Garante caminho antes da saída

mostrar_abertura = True

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # Sair do jogo
      running = False
    if event.type == pygame.KEYDOWN: # Mover o jogador
      if event.key in (pygame.K_w, pygame.K_UP):
        mover_jogador(0, -1)  # Cima
      if event.key in (pygame.K_s, pygame.K_DOWN):
        mover_jogador(0, 1)  # Baixo
      if event.key in (pygame.K_a, pygame.K_LEFT):
        mover_jogador(-1, 0)  # Esquerda
      if event.key in (pygame.K_d, pygame.K_RIGHT):
        mover_jogador(1, 0)  # Direita

  screen.fill(black)
  desenhar_maze(maze)
  if mostrar_abertura:
    tela_abertura()
    pygame.display.flip()
    cor_escolhida = cor_jogador()
    mostrar_abertura = False
  pygame.draw.rect(screen, cor_escolhida, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
