import pygame, random
from sys import exit

pygame.init()

def gerar_maze(x, y): # 1 = parede; 0 = caminho; 2 = caminho pintado
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
          if m[y][x] == 0:
            cor = 'white'
            m[1][1] = 2
          elif m[y][x] == 2:
            cor = cor_pintura
          else:
            cor = 'black'
          pygame.draw.rect(screen, cor, (x * cell_size, y * cell_size, cell_size, cell_size))

def desenhar_maze_novo(m):
  for y in range(maze_height):
      for x in range(maze_width):
          if m[y][x] == 0 or m[y][x] == 2:
            cor = 'white'
          else:
            cor = 'black'
          pygame.draw.rect(screen, cor, (x * cell_size, y * cell_size, cell_size, cell_size))

def tela_abertura():
  # Fundo preto com transparência
  fundo = pygame.Surface([screen_width, screen_height])
  fundo.fill((0,0,0))
  fundo.set_alpha(230)
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
    if teclas_pressionadas.get(pygame.K_w) or teclas_pressionadas.get(pygame.K_UP): # Cima
        dy = -1
    if teclas_pressionadas.get(pygame.K_s) or teclas_pressionadas.get(pygame.K_DOWN): # Baixo
        dy = 1
    if teclas_pressionadas.get(pygame.K_a) or teclas_pressionadas.get(pygame.K_LEFT): # Esquerda
        dx = -1
    if teclas_pressionadas.get(pygame.K_d) or teclas_pressionadas.get(pygame.K_RIGHT): # Direita
        dx = 1
    nx, ny = player_x + dx, player_y + dy
    if 0 < nx < maze_width and 0 < ny < maze_height - 1 and (maze[ny][nx] == 0 or maze[ny][nx] == 2):
        player_x, player_y = nx, ny
        maze[ny][nx] = 2 # Marca o caminho percorrido

def cor_escolhida(a):
  if a == 'r':
    cor = (255, 0, 0) # Vermelho
    light_cor = (255, 125, 125) # Vermelho claro
    triadico1 = (0, 255, 0) # Verde
    triadico2 = (0, 0, 255) # Azul
  if a == 'g':
    cor = (0, 255, 0) # Verde
    light_cor = (170, 255, 170) # Verde claro
    triadico1 = (0, 0, 255) # Azul
    triadico2 = (255, 0, 0) # Vermelho
  if a == 'b':
    cor = (0, 0, 255) # Azul
    light_cor = (125, 125, 255) # Azul claro
    triadico1 = (0, 255 ,0) # Verde
    triadico2 = (255, 0, 0) # Vermelho
  if a == 'c':
    cor = (0, 255, 255) # Ciano
    light_cor = (170, 255, 225) # Ciano claro
    triadico1 = (255, 0, 255) # Magenta
    triadico2 = (255, 255, 0) # Amarelo
  if a == 'm':
    cor = (255, 0, 255) # Magenta
    light_cor = (255, 170, 255) # Magenta claro
    triadico1 = (0, 255, 255) # Ciano
    triadico2 = (255, 255, 0) # Amarelo
  if a == 'y':
    cor = (255, 255, 0) # Amarelo
    light_cor = (255, 255, 175) # Amarelo claro
    triadico1 = (0, 255, 255) # Ciano
    triadico2 = (255, 0, 255) # Magenta
  return cor, light_cor, triadico1, triadico2

def cronometro(t):
  global tempo_total, tempo
  if verificar_vitoria():
     return None
  tempo = pygame.time.get_ticks() - t # Milissegundos
  minutos = (tempo // 1000) // 60
  segundos = (tempo // 1000) % 60
  milissegundos = (tempo % 1000) // 10
  tempo_total = f'{minutos:02}:{segundos:02}:{milissegundos:02}'
  font = pygame.font.SysFont('Arial', 35, bold = True)
  cronometro = font.render(tempo_total, True, cor_jogador)
  x = (screen_width // 2) - cronometro.get_width() // 2
  screen.blit(cronometro, (x, -2))

def verificar_vitoria():
  return maze[player_y][player_x] == maze[maze_height - 2][maze_width - 1]

def tela_vitoria():
  # Fundo preto com transparência
  fundo = pygame.Surface([screen_width, screen_height])
  fundo.fill((0, 0, 0))
  fundo.set_alpha(230)
  screen.blit(fundo, (0, 0))

  # Texto
  font_bold = pygame.font.SysFont('Arial', 38, bold = True)
  tempo_levado = font_bold.render(f'TEMPO LEVADO:', True, cor_jogador)
  x = (screen_width // 2) - tempo_levado.get_width() // 2
  screen.blit(tempo_levado, (x, 35))

  font = pygame.font.SysFont('Arial', 35)
  cronometro_levado = font.render(f'{tempo_total}', True, cor_jogador)
  x = (screen_width // 2) - cronometro_levado.get_width() // 2
  screen.blit(cronometro_levado, (x, 75))

  font_bold = pygame.font.SysFont('Arial', 30, bold = True)
  melhor_tempo = font_bold.render(f'MELHOR TEMPO:', True, cor_jogador)
  x = (screen_width // 2) - melhor_tempo.get_width() // 2
  screen.blit(melhor_tempo, (x, 150))

  font = pygame.font.SysFont('Arial', 27)
  cronometro_melhor = font.render(best_tempo(), True, cor_jogador)
  x = (screen_width // 2) - cronometro_melhor.get_width() // 2
  screen.blit(cronometro_melhor, (x, 190))

  font_bold = pygame.font.SysFont('Arial', 30, bold = True)
  novamente = font_bold.render(f'DESEJA JOGAR NOVAMENTE?', True, 'white')
  x = (screen_width // 2) - novamente.get_width() // 2
  screen.blit(novamente, (x, 280))    

  font_bold = pygame.font.SysFont('Arial', 27, bold = True)
  font = pygame.font.SysFont('Arial', 20)

  nao = font_bold.render(f'NÃO', True, cor_jogador)
  x = (screen_width // 2) - nao.get_width() // 2
  screen.blit(nao, (x, 510))
  zero = font.render(f'(PRESSIONE 0)', True, cor_jogador)
  x = (screen_width // 2) - zero.get_width() // 2
  screen.blit(zero, (x, 540))

  sim_mesmo = font_bold.render(f'SIM, NO MESMO LABIRINTO', True, contraste1)
  screen.blit(sim_mesmo, (110, 410))
  enter = font.render(f'(PRESSIONE ENTER)', True, contraste1)
  screen.blit(enter, (170, 440))

  sim_diferente = font_bold.render(f'SIM, EM OUTRO LABIRINTO', True, contraste2)
  screen.blit(sim_diferente, (850, 410))
  espaco = font.render(f'(PRESSIONE ESPAÇO)', True, contraste2)
  screen.blit(espaco, (910, 440))

def novamente():
  global running
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
              pygame.quit()
              exit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                return 'dnv'
              if event.key == pygame.K_0 or event.key == pygame.K_KP0:
                 return 'nao'
              if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                 return 'msm'

def best_tempo():
  tempos_jogador.append(tempo)
  best_time = min(tempos_jogador)
  minutos = (best_time // 1000) // 60
  segundos = (best_time // 1000) % 60
  milissegundos = (best_time % 1000) // 10
  return f'{minutos:02}:{segundos:02}:{milissegundos:02}'

def outro_maze():
  global player_x, player_y, start_time, maze, ganhou, dnv, ultimo_maze
  maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]
  gerar_maze(1, 1)  # Gera um novo labirinto    
  garantir_caminho_saida()  # Garante um caminho até a saída
  player_x, player_y = 1, 1  # Redefine a posição inicial do jogador
  start_time = pygame.time.get_ticks()  # Reinicia o cronômetro
  ganhou = False
  dnv = None
  ultimo_maze = [linha[:] for linha in maze]
  desenhar_maze_novo(maze)  # Desenha o novo labirinto
  for key in teclas_pressionadas:
    teclas_pressionadas[key] = False
  maze[maze_height - 2][maze_width - 1] = 0  # Substitui a parede pela saída
  maze[maze_height - 2][maze_width - 2] = 0  # Garante caminho antes da saída

def mesmo_maze():
  global player_x, player_y, start_time, maze, ganhou, dnv
  maze = [linha[:] for linha in ultimo_maze]
  gerar_maze(1, 1)  # Gera um novo labirinto    
  garantir_caminho_saida()  # Garante um caminho até a saída
  player_x, player_y = 1, 1  # Redefine a posição inicial do jogador
  start_time = pygame.time.get_ticks()  # Reinicia o cronômetro
  ganhou = False
  dnv = None
  desenhar_maze_novo(maze)  # Desenha o novo labirinto
  for key in teclas_pressionadas:
    teclas_pressionadas[key] = False
  maze[maze_height - 2][maze_width - 1] = 0  # Substitui a parede pela saída
  maze[maze_height - 2][maze_width - 2] = 0  # Garante caminho antes da saída

def temporizador(s):
    global running
    screen.fill((0, 0, 0))
    desenhar_maze(maze)
    pygame.draw.rect(screen, cor_jogador, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))
    fundo = pygame.Surface([screen_width, screen_height])
    fundo.fill((0, 0, 0))
    fundo.set_alpha(230)
    screen.blit(fundo, (0, 0))
    
    font_bold = pygame.font.SysFont('Arial', 100, bold=True)

    pronto = font_bold.render(f'PRONTO?', True, cor_jogador)
    x = (screen_width // 2) - pronto.get_width() // 2
    y = (screen_height // 2) - pronto.get_height() // 2
    screen.blit(pronto, (x, y))
    pygame.display.flip()

    pygame.time.wait(2000)
    screen.fill((0, 0, 0))
    desenhar_maze(maze)
    pygame.draw.rect(screen, cor_jogador, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))
    fundo = pygame.Surface([screen_width, screen_height])
    fundo.fill((0, 0, 0))
    fundo.set_alpha(230)
    screen.blit(fundo, (0, 0))

    for i in range(s, 0, -1):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Sair do jogo
                running = False
                pygame.quit()
                exit()

        numero = font_bold.render(f'{i}', True, cor_jogador)
        x = (screen_width // 2) - numero.get_width() // 2
        y = (screen_height // 2) - numero.get_height() // 2
        screen.blit(numero, (x, y))
        
        pygame.display.flip()

        pygame.time.wait(1000)
        screen.fill((0, 0, 0))
        desenhar_maze(maze)
        pygame.draw.rect(screen, cor_jogador, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))
        fundo = pygame.Surface([screen_width, screen_height])
        fundo.fill((0, 0, 0))
        fundo.set_alpha(230)
        screen.blit(fundo, (0, 0))

    vai = font_bold.render(f'VAI!', True, cor_jogador)
    x = (screen_width // 2) - vai.get_width() // 2
    y = (screen_height // 2) - vai.get_height() // 2
    screen.blit(vai, (x, y))
    pygame.display.flip()
    pygame.time.wait(100)

def tela_mesma_cor():
  # Fundo preto com transparência
  fundo = pygame.Surface([screen_width, screen_height])
  fundo.fill((0, 0, 0))
  fundo.set_alpha(230)
  screen.blit(fundo, (0, 0))

  #Texto
  font_bold = pygame.font.SysFont('Arial', 45, bold = True)
  mesma = font_bold.render(f'DESEJA JOGAR', True, 'white')
  x = (screen_width // 2) - mesma.get_width() // 2
  screen.blit(mesma, (x, 250))
  mesma1 = font_bold.render(f'COM A MESMA COR?', True, 'white')
  x = (screen_width // 2) - mesma1.get_width() // 2
  screen.blit(mesma1, (x, 285))
  font_bold = pygame.font.SysFont('Arial', 35, bold=True)
  font = pygame.font.SysFont('Arial', 28)

  sim = font_bold.render(f'SIM, COM A MESMA', True, cor_jogador)
  screen.blit(sim, (190, 325))

  enter = font.render(f'(PRESSIONE ENTER)', True, cor_jogador)
  screen.blit(enter, (210, 480))

  nao = font_bold.render(f'NÃO, QUERO MUDAR', True, contraste1)
  screen.blit(nao, (815, 450))

  espaco = font.render(f'(PRESSIONE ESPAÇO)', True, contraste1)
  screen.blit(espaco, (840, 480))
  pygame.display.flip()

def mesma_cor():
  global running
  while True:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              running = False
              pygame.quit()
              exit()
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                return 'outro'
              if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                 return 'msm'
              
def tela_outra():
  screen.fill((0, 0, 0))
  desenhar_maze(maze)
  fundo = pygame.Surface([screen_width, screen_height])
  fundo.fill((0,0,0))
  fundo.set_alpha(230)
  screen.blit(fundo, (0,0))

  font_bold = pygame.font.SysFont('Arial', 35, bold=True)
  escolha = font_bold.render(f'ESCOLHA A COR DO SEU PERSONAGEM:', True, 'white')
  x = (screen_width // 2) - escolha.get_width() // 2
  screen.blit(escolha, (x, 200))

  # Cores
  red = pygame.image.load('imagens\\red.png')
  green = pygame.image.load('imagens\\green.png')
  blue = pygame.image.load('imagens\\blue.png')
  cyan = pygame.image.load('imagens\\cyan.png')
  magenta = pygame.image.load('imagens\\magenta.png')
  yellow = pygame.image.load('imagens\\yellow.png')

  x = (screen_width // 2) - green.get_width() // 2
  screen.blit(green, (x, 300))
  screen.blit(magenta, (x, 470))
  x /= 2
  screen.blit(red, (x, 300))
  screen.blit(cyan, (x, 470))
  x += 2 * x
  screen.blit(blue, (x, 300))
  screen.blit(yellow, (x, 470))

  pygame.display.flip()

cell_size = 32
maze_width = 41
maze_height = 21 
screen_width = maze_width * cell_size
screen_height = maze_height * cell_size

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Labirinto')

player_x, player_y = 1, 1  # Posição inicial do jogado

maze = [[1 for _ in range(maze_width)] for _ in range(maze_height)]
direcoes = [
  (0, -2), # Cima
  (0, 2), # Baixo
  (-2, 0), # Esquerda
  (2, 0) # Direira
]

gerar_maze(1, 1) # Define a entrada na célula 1,1
garantir_caminho_saida()
ultimo_maze = [linha[:] for linha in maze]  # Guarda o labirinto original


# Saída fixa
maze[maze_height - 2][maze_width - 1] = 0  # Substitui a parede pela saída
maze[maze_height - 2][maze_width - 2] = 0  # Garante caminho antes da saída

mostrar_abertura = True
teclas_pressionadas = {
    pygame.K_w: False, pygame.K_UP: False,
    pygame.K_s: False, pygame.K_DOWN: False,
    pygame.K_a: False, pygame.K_LEFT: False,
    pygame.K_d: False, pygame.K_RIGHT: False,
}
tempos_jogador = []
dnv = None

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # Sair do jogo
      running = False
      pygame.quit()
      exit()
    if event.type == pygame.KEYDOWN: # Mover o jogador
        teclas_pressionadas[event.key] = True
    if event.type == pygame.KEYUP: # Parar de mover o jogador
        teclas_pressionadas[event.key] = False
  
  screen.fill('black')
  desenhar_maze(maze)
  if mostrar_abertura:
    tela_abertura()
    pygame.display.flip()
    cor_jogador, cor_pintura, contraste1, contraste2 = cor_escolhida(cor())
    mostrar_abertura = False
    temporizador(3)
    start_time = pygame.time.get_ticks()
  pygame.draw.rect(screen, cor_jogador, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))
  mover_jogador()
  pygame.draw.rect(screen, cor_jogador, (player_x * cell_size, player_y * cell_size, cell_size, cell_size))
  cronometro(start_time)
  pygame.display.flip()
  ganhou = verificar_vitoria()
  if ganhou:
    tempos_jogador.append(tempo)
    ganhou = False
    tela_vitoria()
    pygame.display.flip()
    dnv = novamente()

  if dnv == 'nao':
    running = False
  elif dnv == 'dnv':
    tempos_jogador = []
    outro_maze()
    tela_mesma_cor()
    mesma = mesma_cor()
    if mesma == 'outro':
      tela_outra()
      cor_jogador, cor_pintura, contraste1, contraste2 = cor_escolhida(cor())
    temporizador(3)
  elif dnv == 'msm':
    mesmo_maze()
    tela_mesma_cor()
    mesma = mesma_cor()
    if mesma == 'outro':
      tela_outra()
      cor_jogador, cor_pintura, contraste1, contraste2 = cor_escolhida(cor())
    temporizador(3)

  clock.tick(12)
pygame.quit()