import pygame

# Inicializa o Pygame
pygame.init()

# Defina as configurações da tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Cronômetro no Pygame")

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonte para exibir o tempo
font = pygame.font.SysFont(None, 40)

# Inicializar variáveis
start_time = pygame.time.get_ticks()  # marca o tempo de início
running = True

# Loop principal
while running:
    screen.fill(BLACK)
    
    # Calcular o tempo decorrido
    elapsed_time = pygame.time.get_ticks() - start_time
    seconds = elapsed_time // 1000  # Converte milissegundos para segundos
    milliseconds = elapsed_time % 1000  # O restante em milissegundos

    # Exibir o cronômetro na tela
    timer_text = font.render(f"{seconds:02}:{milliseconds // 10:02}", True, WHITE)
    screen.blit(timer_text, (350, 250))

    # Processar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

# Finaliza o Pygame
pygame.quit()
