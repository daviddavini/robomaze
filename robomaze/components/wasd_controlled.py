import pygame
import pymunk
from pygame import Vector2

import utilities
import components

class WASDControlled(components.Component):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed

    def update(self, dt):

        new_velocity = self.speed * self.get_move_vector()
        self.gameobject.components[components.Physics].body.velocity = new_velocity
        #self.gameobject.components[components.Physics].body.apply_impulse_at_local_point(new_velocity)

    def get_move_vector(self):
        pressed = pygame.key.get_pressed()
        move_vector = pymunk.Vec2d(0, 0)
        if pressed[pygame.K_w]:
            move_vector += Vector2(0, -1)
        if pressed[pygame.K_s]:
            move_vector += Vector2(0, 1)
        if pressed[pygame.K_a]:
            move_vector += Vector2(-1, 0)
        if pressed[pygame.K_d]:
            move_vector += Vector2(1, 0)

        return utilities.try_normalize(move_vector)
