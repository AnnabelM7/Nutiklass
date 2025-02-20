import pygame, sys
import random

pygame.init()

#Ekraan
WIDTH, HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pong!")

#Värvid
BLACK=(0,0,0)
WHITE=(255,255,255)

#Plaadid
PADDLE_WIDTH, PADDLE_HEIGHT = 15, 100
left_paddle_y = right_paddle_y = HEIGHT // 2 - PADDLE_HEIGHT // 2  # Algpositsioon keskel
left_paddle_x = 30
right_paddle_x = WIDTH - 30 - PADDLE_WIDTH

#Skoor
left_score = 0
right_score = 0

#Liikumiskiirus
PADDLE_SPEED = 10

# PALLI OMADUSED
BALL_SIZE = 20
ball_x = WIDTH // 2 - BALL_SIZE // 2
ball_y = HEIGHT // 2 - BALL_SIZE // 2
#ball_speed_x = 3
#ball_speed_y = 3

# Juhuslik suund ja kõrgus
ball_speed_x = random.choice([-3, 3])  # Vasakule või paremale
ball_speed_y = random.randint(-3, 3)  # Juhuslik kõrgus

# STEP 5 Funktsioon loenduse kuvamiseks
def countdown():
    for num in range(3, 0, -1):
        SCREEN.fill(BLACK)
        text = pygame.font.SysFont(None, 36).render(str(num), True, WHITE)
        SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        pygame.display.flip()
        pygame.time.delay(1000)  # 1 sekund

# Enne mängu algust
countdown()


running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            
    #Ekraan mustaks
    SCREEN.fill(BLACK)

    #Valge joon keskele
    pygame.draw.line(SCREEN, WHITE, (WIDTH//2,0), (WIDTH//2, HEIGHT), 5)

    #Joonista vasak ja parem löögiplaat
    pygame.draw.rect(SCREEN, WHITE, (left_paddle_x, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(SCREEN, WHITE, (right_paddle_x, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT))

    # Kuvame skoori otse
    left_score_text = pygame.font.SysFont(None, 36).render(str(left_score), True, WHITE)
    right_score_text = pygame.font.SysFont(None, 36).render(str(right_score), True, WHITE)

    # Kuvame skoori vasakule ja paremale
    SCREEN.blit(left_score_text, (WIDTH // 4, 20))  # Vasak pool
    SCREEN.blit(right_score_text, (WIDTH * 3 // 4 - right_score_text.get_width(), 20))  # Parem pool
    
    # Klahvide kontroll
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle_y < HEIGHT - PADDLE_HEIGHT:
        left_paddle_y += PADDLE_SPEED
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and right_paddle_y < HEIGHT - PADDLE_HEIGHT:
        right_paddle_y += PADDLE_SPEED
        
    # Joonista pall
    pygame.draw.ellipse(SCREEN, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))  
        
    #Palli liigutamine
    ball_x += ball_speed_x
    ball_y += ball_speed_y
        
    # Palli põrkamine ülevalt ja alt
    if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
        ball_speed_y *= -1  # Muuda suunda
        
     # Palli põrkamine löögiplaatidelt
    if (ball_x <= left_paddle_x + PADDLE_WIDTH and left_paddle_y < ball_y < left_paddle_y + PADDLE_HEIGHT) or (ball_x >= right_paddle_x - BALL_SIZE and right_paddle_y < ball_y < right_paddle_y + PADDLE_HEIGHT):
        ball_speed_x *= -1  # Muuda suunda
      
    # Skoori määramine (kui pall läheb ekraanist välja)
    if ball_x < 0:  # Parem mängija sai punkti
        right_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Läheb tagasi keskele
        ball_speed_x = random.choice([-3, 3])
        ball_speed_y = random.randint(-3, 3)

    if ball_x > WIDTH:  # Vasak mängija sai punkti
        left_score += 1
        ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        ball_speed_x = random.choice([-3, 3])
        ball_speed_y = random.randint(-3, 3)
        
    pygame.display.flip()
    pygame.time.delay(10) 
     
     
pygame.quit()
sys.exit()

