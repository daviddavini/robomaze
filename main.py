import pygame
from pygame import Vector2

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
FPS = 60

def move_vector(pressed):
    dir = Vector2(0,0)
    if pressed[pygame.K_w]:
        dir += Vector2(0,1)
    if pressed[pygame.K_d]:
        dir -= Vector2(0,-1)

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

run = True

background_color = (20, 25, 79)

x, y = DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2
dx, dy = 5, 5

while run:
    clock.tick(FPS)
    display.fill(background_color)

    pressed = pygame.key.get_pressed()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
