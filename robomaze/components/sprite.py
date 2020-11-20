import os
import warnings

import pygame
from pygame import Vector2

import game

import utilities
import components

class Sprite(components.Component):
    def __init__(self, filename, size = None):
        '''
        size - the width, height of the in-game sprite as a Vector2.
                if None, defaults to scaling image by Game.PIXEL_ART_SCALE
        '''
        super().__init__()
        self.filename = filename
    
        # Load the image
        self.image = pygame.image.load(os.path.join(utilities.ROOT_DIR, 'assets', self.filename))
        
        # Store the original width, height of the pixel art
        rect = self.image.get_bounding_rect()
        self.pixel_size = Vector2(rect.size)
        # The correct size has each pixel scaled by PIXEL_ART_SCALE
        self.correct_size = self.pixel_size * game.Game.PIXEL_ART_SCALE
        # If no size given, use the self.correct_size
        self.size = size or self.correct_size
        # Ensure that self.size has int coords
        for i in self.size:
            if not i == int(i):
                raise Exception('Sprite size must have int coords')

        # Because pygame is picky, it can only scale sprites by int tuples
        int_size = tuple(int(x) for x in self.size)     
        # Scale the image to the desired size
        self.image = pygame.transform.scale(self.image, int_size)

        # Check that the pixel art is to the correct scale
        if not self.size == self.correct_size:
            warnings.warn('Sprite pixels are not correct size. Sprite is {}, should be {}.'.format(self.size, self.correct_size))        

    # TODO: these inputs should really be referenced from game, right?
    def draw(self, display, camera):
        screen_center_pos = Vector2(pygame.display.get_surface().get_size()) / 2
        # TODO: Make this a func in game
        cam_pos = camera.components[components.Physics].body.position
        delta_from_cam = self.gameobject.components[components.Physics].body.position - self.size/2 - cam_pos
        display.blit(self.image, screen_center_pos + delta_from_cam)