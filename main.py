import pygame
from pygame import Vector2

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
FPS = 60

def get_move_vector(pressed):
    move_vector = Vector2(0, 0)
    if pressed[pygame.K_w]:
        move_vector += Vector2(0, -1)
    if pressed[pygame.K_s]:
        move_vector += Vector2(0, 1)
    if pressed[pygame.K_a]:
        move_vector += Vector2(-1, 0)
    if pressed[pygame.K_d]:
        move_vector += Vector2(1, 0)

    if move_vector == Vector2(0, 0):
        return move_vector
    else:
        return move_vector.normalize()

pygame.init()

clock = pygame.time.Clock()
display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.FULLSCREEN)

run = True

background_color = (20, 25, 79)
red = (255, 0, 0)

pos = Vector2(DISPLAY_WIDTH/2, DISPLAY_HEIGHT / 2)
player = pygame.Rect(pos, (50, 50))

while run:
    clock.tick(FPS)
    display.fill(background_color)

    pressed = pygame.key.get_pressed()
    move_vector = get_move_vector(pressed)
    player = player.move(9 * move_vector)

    pygame.draw.rect(display, red, player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
