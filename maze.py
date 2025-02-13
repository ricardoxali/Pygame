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
  font = pygame.font.SysFont('Arial', 38, bold = True)
  objetivo = font.render(f'OBJETIVO:', True, 'white')
  screen.blit(objetivo, (200, 35))
 
  # Cores
  red = pygame.image.load('imagens\\red.png')
  screen.blit(red, (0,0))

cell_size = 32
maze_width = 41
maze_height = 21 
screen_width = maze_width * cell_size
screen_height = maze_height * cell_size



# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
yellow = (255, 255, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Labirinto')

maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)] # 1 = parede; 0 = caminho;
direcoes = [
  (0, -2), # Cima
  (0, 2), # Baixo
  (-2, 0), # Esquerda
  (2, 0) # Direira
]

gerar_maze(1, 1) # Define o primeiro caminho (a entrada) na célula 1,1

# Saída fixa
maze[maze_height - 2][maze_width - 1] = 0  # Substitui a parede pela saída
maze[maze_height - 2][maze_width - 2] = 0  # Garante caminho antes da saída


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(black)
  desenhar_maze(maze)
  tela_abertura()

  pygame.display.flip()
  clock.tick(60)

pygame.quit()
