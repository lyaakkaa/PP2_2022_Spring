
from datetime import datetime
import pygame 
import math

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

#color
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0 )
GREEN = (0,255,0)
BLUE = (0,0,255)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CLOCK")

icon = pygame.image.load("./clock/clock.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
font = pygame.font.SysFont('Verdana', 25)
finished = False

background = pygame.image.load('./clock/мики.jpg')
background = pygame.transform.scale(background,(WIDTH, HEIGHT))



hand1 = pygame.image.load('./clock/handd1.png').convert_alpha()
hand2 = pygame.image.load('./clock/handd2.png').convert_alpha()
hand1 = pygame.transform.scale(hand1,(150, 100))
hand2 = pygame.transform.scale(hand2,(115, 100))

rect1 = hand1.get_rect(bottomleft = (WIDTH//2 , HEIGHT//2)) 
rect2 = hand2.get_rect(bottomright = (WIDTH//2 , HEIGHT//2))


pygame.mixer.music.load("./music_clock/tiktak.mp3")

H_WIDTH, H_HEIGHT = WIDTH // 2, HEIGHT // 2  # начало наших стрелок 
RADIUS = H_HEIGHT - 75 # радиус часовой стрелки 
radius_list = {'sec': RADIUS - 10, 'min': RADIUS - 55, 'hour': RADIUS - 100}  # длина стрелок для каждой 
clock60 = dict(zip(range(60), range(0, 360, 6)))

def get_clock_pos(clock_dict, clock_hand, key):
    x = H_WIDTH + radius_list[key] * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = H_HEIGHT + radius_list[key] * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


while not finished:
    clock.tick(FPS)
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.blit(background, (0, 0))

    t = datetime.now()
    time_text = font.render(f'{t:%H:%M:%S}', True, BLUE, GREEN)
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    screen.blit(time_text,(45, 75))

    pygame.draw.line(screen, pygame.Color('orange'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, hour, 'hour'), 15)
    pygame.draw.line(screen, pygame.Color('green'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, minute, 'min'), 7)
    line = pygame.draw.line(screen, pygame.Color('magenta'), (H_WIDTH, H_HEIGHT), get_clock_pos(clock60, second, 'sec'), 4)
    pygame.draw.circle(screen, pygame.Color('black'), (H_WIDTH, H_HEIGHT), 8)


    screen.blit(hand1,rect2)
    screen.blit(hand2,rect2)


    pygame.display.flip()
pygame.quit()