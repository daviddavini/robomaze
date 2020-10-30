import pygame
import constants
from pygame import Vector2
import abc
import random
import math

class Component(abc.ABC):

    def __init__(self):
        self.gameobject = None

    @abc.abstractmethod
    def update(self, dt):
        pass

class Movement(Component):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed
        self.direction = Vector2(0,0)
    
    def update(self, dt):
        self.gameobject.pos += self.speed * self.direction * dt

class Wiggle(Component):
    def __init__(self, wiggle_amount):
        self.wiggle_amount = wiggle_amount

    def update(self, dt):
        self.gameobject.pos += random.uniform(0, self.wiggle_amount) * random_vector()

class WASDControlled(Component):
    def update(self, dt):
        pressed = pygame.key.get_pressed()
        self.gameobject.components[Movement].direction = self.get_move_vector(pressed)

    def get_move_vector(self, pressed):
        move_vector = Vector2(0, 0)
        if pressed[pygame.K_w]:
            move_vector += Vector2(0, -1)
        if pressed[pygame.K_s]:
            move_vector += Vector2(0, 1)
        if pressed[pygame.K_a]:
            move_vector += Vector2(-1, 0)
        if pressed[pygame.K_d]:
            move_vector += Vector2(1, 0)

        return try_normalize(move_vector)

class Follow(Component):
    def __init__(self, target):
        '''
        target - GameObject to follow
        '''
        super().__init__()
        self.target = target

    def update(self, dt):
        v = self.target.pos - self.gameobject.pos
        v = try_normalize(v)
        self.gameobject.components[Movement].direction = v

class GameObject:
    def __init__(self, components, color = None, size = Vector2(50, 50)):
        ''' 
        components -- list of Components objects
        '''
        self.pos = Vector2(constants.DISPLAY_WIDTH/2, constants.DISPLAY_HEIGHT/2)
        self.size = Vector2(size)
        self.color = color

        # self.components is a Dict mapping Component classes (the keys) to Component objects (the values)
        self.components = {type(comp) : comp for comp in components}
        for component in components:
            component.gameobject = self
    
    def update(self, dt):
        for component in self.components.values():
            component.update(dt)

    def draw(self, display):
        pygame.draw.rect(display, self.color, self.get_rect())

    def get_rect(self):
        return pygame.Rect(self.pos - self.size/2, self.size)

def try_normalize(v):
    if v == Vector2(0,0):
        return v
    return v.normalize()

def random_vector():
    theta = random.uniform(0, 2*math.pi)
    return Vector2(math.cos(theta), math.sin(theta))