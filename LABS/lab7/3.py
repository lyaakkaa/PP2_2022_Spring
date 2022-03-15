 
from turtle import circle
import pygame 
pygame.init()

WIDTH, HEIGHT = 850, 650
FPS = 30

#color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0 )
GREEN = (0,255,0)
BLUE = (0,0,255)

#Initialization 
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Red Ball")
clock = pygame.time.Clock()

finished = False

circ_x,circ_y = WIDTH//2, HEIGHT//2
RAD = 25
step = 20

dx, dy = 0, 0 

while not finished:
    clock.tick(FPS)

    screen.fill(WHITE)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            finished = True

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT and circ_x + RAD  < WIDTH:
                circ_x += step

            if event.key == pygame.K_LEFT and circ_x - RAD > 0:
                circ_x -= step

            if event.key == pygame.K_UP and circ_y - RAD > 0:
                circ_y -= step

            if event.key == pygame.K_DOWN and circ_y + RAD < HEIGHT:
                circ_y += step



    pygame.draw.circle(screen, RED, (circ_x,circ_y),RAD)

    pygame.display.flip()

pygame.quit()