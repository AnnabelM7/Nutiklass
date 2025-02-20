import pygame
import sys

pygame.init()

# Akna suurus
window_width, window_height = 800, 600

# Loo Pygame aken
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Liigutan 2 palli")

# Värvid
background_color = (255, 255, 255)  # Valge taust
ball_color1 = (255, 0, 0)  # Punane pall
ball_color2 = (0, 0, 255)  # Sinine pall

# Palli omadused
ball_radius = 20
x1, y1 = 200, 200  # Palli algkoordinaadid
x2, y2 = 400, 200
step = 10  # Samm, kui klahvi vajutatakse


# Luba klahvide korduv vajutus
pygame.key.set_repeat(1, 10)

# Peamine tsükkel
running = True
while running:
    # Kontrolli sündmusi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Liigu nooleklahvidega (punane)
            if event.key == pygame.K_UP and y1 - ball_radius > 0:
                y1 -= step
            elif event.key == pygame.K_DOWN and y1 + ball_radius < window_height:
                y1 += step
            elif event.key == pygame.K_LEFT and x1 - ball_radius > 0:
                x1 -= step
            elif event.key == pygame.K_RIGHT and x1 + ball_radius < window_width:
                x1 += step
                
            # Liigu WASD-klahvidega (sinine pall)
            if event.key == pygame.K_w and y2 - ball_radius > 0:
                y2 -= step
            elif event.key == pygame.K_s and y2 + ball_radius < window_height:
                y2 += step
            elif event.key == pygame.K_a and x2 - ball_radius > 0:
                x2 -= step
            elif event.key == pygame.K_d and x2 + ball_radius < window_width:
                x2 += step

            # Algpositsioonile viimine (HOME klahv)
            if event.key == pygame.K_HOME:
                x1, y1 = 200, 200  # Punane pall
                x2, y2 = 400, 200  # Sinine pall

    # Täida taust
    screen.fill(background_color)

    # Joonista pall (punane)
    pygame.draw.circle(screen, ball_color1, (x1, y1), ball_radius)

    # Joonista pall (sinine)
    pygame.draw.circle(screen, ball_color2, (x2, y2), ball_radius)
    
    # Värskenda ekraani
    pygame.display.flip()

# Sulge Pygame
pygame.quit()
sys.exit()


