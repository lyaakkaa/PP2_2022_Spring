from re import S
import pygame, os
from random import choice
pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Music player")

clock =  pygame.time.Clock()

finished = False

font = pygame.font.SysFont('Verdana', 27)

vol = 1.0


background = pygame.image.load('./music_img/bkg.jpg')
background = pygame.transform.scale(background,(WIDTH, HEIGHT))


_songs =  ['music/Glass Animals - Heat Waves.mp3', 'music/Jah Khalib - Лейла.mp3','music/OneRepublic - Counting Stars .mp3', 'music/The Weeknd - Save Your Tears.mp3', 'music/Daft Punk - Get Lucky.mp3']
pygame.mixer.music.load('music/Glass Animals - Heat Waves.mp3')
pygame.mixer.music.play()

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    
def play_prev_song():
    global _songs
    _songs =  [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
    
    


while not finished:
    clock.tick(FPS)
    screen.fill((255,255,255))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            vol -= 0.2
            pygame.mixer.music.set_volume(vol)

        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            vol += 0.2
            pygame.mixer.music.set_volume(vol)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key == pygame.K_s:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT:
               play_next_song()
            if event.key == pygame.K_LEFT:
                play_prev_song()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] in range(c1_pos[0], c1_pos[0] + c1_pos[2]) and event.pos[1] in range(c1_pos[1], c1_pos[1] + c1_pos[3]):
                play_next_song()
            if event.pos[0] in range(c2_pos[0], c2_pos[0] + c2_pos[2]) and event.pos[1] in range(c2_pos[1], c2_pos[1] + c2_pos[3]):
                play_prev_song()
    

    

 

    text_song = _songs[0].replace('music/','')
    text_song = text_song.replace('.mp3','')

    text = font.render(f'{text_song}', True, pygame.Color('black'), pygame.Color('white'))
    screen.blit(background, (0, 0))
    screen.blit(text, (125, 355))

    c1 = pygame.draw.rect(screen,pygame.Color('white'), (478, 450, 40, 25),3)
    c2 = pygame.draw.rect(screen,pygame.Color('white'), (285, 450, 38, 25),3)
    #c3 = pygame.draw.circle(screen,pygame.Color('red'), (400,460),20,3)

    c1_pos = (475, 450, 40, 25)
    c2_pos = (280, 450, 40, 25)
    #c3_pos = (400,460,20)




    
    

    pygame.display.flip() 
pygame.quit()
