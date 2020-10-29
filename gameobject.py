import pygame
import constants
from pygame import Vector2

class GameObject:
    def __init__(self):
        self.pos = Vector2(constants.DISPLAY_WIDTH/2, constants.DISPLAY_HEIGHT/2)
        self.speed = 200
        self.direction = Vector2(0,0)
        self.size = Vector2(50,50)
    
    def update(self, dt):
        pressed = pygame.key.get_pressed()
        self.direction = get_move_vector(pressed)
        self.pos += self.speed * self.direction * dt
        self.rect = pygame.Rect(self.pos, self.size)

    def draw(self, display):
        pygame.draw.rect(display, constants.RED, self.rect)

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