from datetime import datetime
import pygame 
pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0 )
GREEN = (0,255,0)
BLUE = (0,0,255)

def blitRotate(surf, image, coord, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = coord).center)
    surf.blit(rotated_image, new_rect.topleft)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CLOCK")
icon = pygame.image.load("./clock/clock.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
font = pygame.font.SysFont('Verdana', 25)
pygame.mixer.music.load("./music_clock/tiktak.mp3")
finished = False

background = pygame.image.load('./clock/мики.jpg')
background = pygame.transform.scale(background,(WIDTH, HEIGHT))
hand1 = pygame.image.load('./clock/ruka1.png').convert_alpha()
hand2 = pygame.image.load('./clock/ruka2.png').convert_alpha()

def time_to_angle(time):
    return  360 - time*6

while not finished:

    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

    screen.blit(background, (0, 0))
    pygame.mixer.music.play(-1)

    t = datetime.now()

    time_text = font.render(f'{t:%H:%M:%S}', True, RED, BLACK)
    hour, minute, second = ((t.hour % 12) * 5 + t.minute // 12) % 60, t.minute, t.second
    screen.blit(time_text,(45, 75))

    angle_sec = time_to_angle(t.second + 1)
    angle_min = time_to_angle(t.minute)

    blitRotate(screen, hand1, (255,150), angle_sec)
    blitRotate(screen, hand2, (255,150), angle_min)

    pygame.display.flip()
pygame.quit()