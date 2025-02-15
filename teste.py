import pygame

pygame.init()

def tela_vitoria():
    # Fundo preto com transparência
    fundo = pygame.Surface([screen_width, screen_height])
    fundo.fill((0, 0, 0))
    fundo.set_alpha(190)
    screen.blit(fundo, (0, 0))

    # Texto
    font_bold = pygame.font.SysFont('Arial', 38, bold = True)
    tempo_levado = font_bold.render(f'TEMPO LEVADO:', True, 'white')
    x = (screen_width // 2) - tempo_levado.get_width() // 2
    screen.blit(tempo_levado, (x, 35))

    font = pygame.font.SysFont('Arial', 35)
    cronometro_levado = font.render(f'00:00:00', True, 'white')
    x = (screen_width // 2) - cronometro_levado.get_width() // 2
    screen.blit(cronometro_levado, (x, 75))

    font_bold = pygame.font.SysFont('Arial', 30, bold = True)
    melhor_tempo = font_bold.render(f'MELHOR TEMPO:', True, 'white')
    x = (screen_width // 2) - melhor_tempo.get_width() // 2
    screen.blit(melhor_tempo, (x, 150))

    font = pygame.font.SysFont('Arial', 27)
    cronometro_melhor = font.render(f'00:00:00', True, 'white')
    x = (screen_width // 2) - cronometro_melhor.get_width() // 2
    screen.blit(cronometro_melhor, (x, 190))

    font_bold = pygame.font.SysFont('Arial', 30, bold = True)
    novamente = font_bold.render(f'DESEJA JOGAR NOVAMENTE?', True, 'white')
    x = (screen_width // 2) - novamente.get_width() // 2
    screen.blit(novamente, (x, 280))    

    font_bold = pygame.font.SysFont('Arial', 27, bold = True)
    font = pygame.font.SysFont('Arial', 20)

    nao = font_bold.render(f'NÃO', True, 'white')
    x = (screen_width // 2) - nao.get_width() // 2
    screen.blit(nao, (x, 510))
    zero = font.render(f'(PRESSIONE 0)', True, 'white')
    x = (screen_width // 2) - zero.get_width() // 2
    screen.blit(zero, (x, 540))

    sim_mesmo = font_bold.render(f'SIM, NO MESMO LABIRINTO', True, 'white')
    screen.blit(sim_mesmo, (110, 410))
    enter = font.render(f'(PRESSIONE ENTER)', True, 'white')
    screen.blit(enter, (198, 440))

    sim_diferente = font_bold.render(f'SIM, EM OUTRO LABIRINTO', True, 'white')
    screen.blit(sim_diferente, (850, 410))
    espaco = font.render(f'(PRESSIONE ESPAÇO)', True, 'white')
    screen.blit(espaco, (940, 440))

cell_size = 32
maze_width = 41
maze_height = 21 
screen_width = maze_width * cell_size
screen_height = maze_height * cell_size

start_time = pygame.time.get_ticks()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Labirinto')

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Sair do jogo
            running = False
    
    tela_vitoria()
    pygame.display.flip()