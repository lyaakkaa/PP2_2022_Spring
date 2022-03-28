import pygame
import math
import datetime

pygame.init()

screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()


def convert_degrees_to_pygame(R, theta):
    y = math.cos(2 * math.pi* theta / 360) * R
    x = math.sin(2 * math.pi* theta / 360) * R
    return x + 400 - 15 , -(y - 400) - 15

FPS = 50

def print_text(text, pos):
    font = pygame.font.SysFont("Castellar", 40, True, False)
    surface = font.render(text, True, (0, 0 ,0) )
    screen.blit(surface, pos)

finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    curr_time = datetime.datetime.now()
    seconds = curr_time.second
    min = curr_time.minute
    hour = curr_time.hour

    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0, 0, 0), (400, 400), 400,4 )
    
    for num in range(1,13):
        print_text(f'{num}',convert_degrees_to_pygame(350, num * 30))
    #minute
    R = 350 
    theta = (min + seconds / 60 ) * (360/60)
    pygame.draw.line(screen, (0,0,0), (400, 400), convert_degrees_to_pygame(R, theta), 8)
    

    #second
    R = 300 
    theta = seconds * (360/60)
    pygame.draw.line(screen, (255,0,0), (400, 400), convert_degrees_to_pygame(R, theta), 8)

    #hour
    R = 250 
    theta = hour * (360 / 12)
    pygame.draw.line(screen, (0,0,0), (400, 400), convert_degrees_to_pygame(R, theta), 8)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()