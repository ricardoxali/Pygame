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
            cor = 'white'
            maze[1][1] = 2
          elif maze[y][x] == 2:
            cor = cor_pintura
          else:
            cor = 'black'
          pygame.draw.rect(screen, cor, (x * cell_size, y * cell_size, cell_size, cell_size))

def tela_abertura():
  # Fundo preto com transparência
  fundo = pygame.Surface([screen_width, screen_height])
  fundo.fill((0,0,0))
  fundo.set_alpha(190)
  screen.blit(fundo, (0,0))

  # Texto
  font_bold = pygame.font.SysFont('Arial', 38, bold = True)
  objetivo = font_bold.render(f'OBJETIVO:', True, 'white')
  x = (screen_width // 2) - objetivo.get_width() // 2
  screen.blit(objetivo, (x, 35))

  font = pygame.font.SysFont('Arial', 35)
  explicacao = font.render(f'ESCAPAR DO LABIRINTO NO', True, 'white')
  explicacao1 = font.render(f'MENOR TEMPO QUE CONSEGUIR', True, 'white')
  x = (screen_width // 2) - explicacao.get_width() // 2
  screen.blit(explicacao, (x, 100))
  x = (screen_width // 2) - explicacao1.get_width() // 2
  screen.blit(explicacao1, (x, 150))

  escolha = font_bold.render(f'ESCOLHA A COR DO SEU PERSONAGEM:', True, 'white')
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

def cor():
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

def mover_jogador():
    global player_x, player_y
    dx, dy = 0, 0
    if teclas_pressionadas.get(pygame.K_w) or teclas_pressionadas.get(pygame.K_UP):
        dy = -1
    if teclas_pressionadas.get(pygame.K_s) or teclas_pressionadas.get(pygame.K_DOWN):
        dy = 1
    if teclas_pressionadas.get(pygame.K_a) or teclas_pressionadas.get(pygame.K_LEFT):
        dx = -1
    if teclas_pressionadas.get(pygame.K_d) or teclas_pressionadas.get(pygame.K_RIGHT):
        dx = 1
    nx, ny = player_x + dx, player_y + dy
    if maze[ny][nx] == 0 or maze[ny][nx] == 2:
        player_x, player_y = nx, ny
        maze[ny][nx] = 2  # Marca o caminho percorrido

def cor_escolhida(a):
  if a == 'r':
    cor = (255, 0, 0) # Vermelho
    light_cor = (255, 125, 125) # Vermelho claro
    triadico1 = (0, 255, 0) # Verde
    triadico2 = (0, 0, 255) # Azul
  if a == 'g':
    cor = (0, 255, 0) # Verde
    light_cor = (125, 255, 125) # Verde claro
    triadico1 = (255, 0, 0) # Vermelho
    triadico2 = (0, 0, 255) # Azul
  if a == 'b':
    cor = (0, 0, 255) # Azul
    light_cor = (125, 125, 255) # Azul claro
    triadico1 = (255, 0 ,0) # Vermelho
    triadico2 = (0, 255, 0) # Verde
  if a == 'c':
    cor = (0, 255, 255) # Ciano
    light_cor = (200, 255, 225) # Ciano claro
    triadico1 = (255, 0, 255) # Magenta
    triadico2 = (255, 255, 0) # Amarelo
  if a == 'm':
    cor = (255, 0, 255) # Magenta
    light_cor = (255, 200, 255) # Magenta claro
    triadico1 = (0, 255, 255) # Ciano
    triadico2 = (255, 255, 0) # Amarelo
  if a == 'y':
    cor = (255, 255, 0) # Amarelo
    light_cor = (255, 255, 200) # Amarelo claro
    triadico1 = (0, 255, 255) # Ciano
    triadico2 = (255, 0, 255) # Magenta
  return cor, light_cor, triadico1, triadico2

def cronometro(t):
  tempo_total = pygame.time.get_ticks() - t # Milissegundos
  minutos = (tempo_total // 1000) // 60
  segundos = (tempo_total // 1000) % 60
  font = pygame.font.SysFont('Arial', 35, bold=True)
  cronometro = font.render(f'{minutos:02}:{segundos:02}', True, cor_jogador)
  x = (screen_width // 2) - cronometro.get_width() // 2
  screen.blit(cronometro, (x, -2))

def verificar_vitoria():
  if player_x == 41 and player_y == 20:
    return True
  else:
    return False
  
def tela_vitoria(v):
  if v == False:
    return None
  if v == True:
    # Fundo preto com transparência
    fundo = pygame.Surface([screen_width, screen_height])
    fundo.fill((0,0,0))
    fundo.set_alpha(190)
    screen.blit(fundo, (0,0))
    

cell_size = 32
maze_width = 41
maze_height = 21 
screen_width = maze_width * cell_size
screen_height = maze_height * cell_size

start_time = pygame.time.get_ticks()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Labirinto')

player_x, player_y = 1, 1  # Posição inicial do jogado

maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)] # 1 = parede; 0 = caminho; 2 = caminho pintado
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

cor_jogador = 'grey'
mostrar_abertura = True
teclas_pressionadas = {
    pygame.K_w: False, pygame.K_UP: False,
    pygame.K_s: False, pygame.K_DOWN: False,
    pygame.K_a: False, pygame.K_LEFT: False,
    pygame.K_d: False, pygame.K_RIGHT: False,
}

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # Sair do jogo
      running = False
    if event.type == pygame.KEYDOWN: # Mover o jogador
        teclas_pressionadas[event.key] = True
    if event.type == pygame.KEYUP: # Parar de mover o jogador
        teclas_pressionadas[event.key] = False

  screen.fill('black')
  desenhar_maze(maze)
  cronometro(start_time)
  if mostrar_abertura:
    tela_abertura()
    pygame.display.flip()
    cor_jogador, cor_pintura, contraste1, contraste2 = cor_escolhida(cor())
    mostrar_abertura = False
  pygame.draw.rect(screen, cor_jogador, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))
  mover_jogador()

  pygame.display.flip()
  clock.tick(12)

pygame.quit()