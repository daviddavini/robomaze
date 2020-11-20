import pygame
from pygame import Vector2

import pymunk
import pymunk.pygame_util

import gameobject
import maze
import components

class Game:

    # TODO: Found out, the pythonic way of making constants is lower_case
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 800
    FPS = 60
    VIEW_GRID_SIZE = 8
    PIXEL_ART_SCALE = 4
    RED = (255, 0, 0)
    CYAN = (0, 255, 255)
    BACKGROUND_COLOR = (20, 25, 79)
    DEBUG_ALPHA = 180

    def __init__(self):
        # Setup pygame
        pygame.init()

        self.clock = pygame.time.Clock()
        # TODO: fix the display_size reference mess
        self.display_size = Vector2(self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
        self.display = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        self.is_running = True

        # Setup pymunk space
        self.space = pymunk.Space()
        self.space.gravity = 0,0  # No thank you, gravity

        # Setup pymunk's debug draw
        self.debug_surface = pygame.Surface(self.display_size, pygame.SRCALPHA)
        self.debug_surface.set_alpha(self.DEBUG_ALPHA)
        self.pymunk_draw_options = pymunk.pygame_util.DrawOptions(self.debug_surface)
        pymunk.pygame_util.positive_y_is_up = False

        self.is_drawing_debug = True

        self.gameobjects = []

        self.player = gameobject.make_player(self)
        self.gameobjects.append(self.player)
        self.gameobjects.append(gameobject.make_enemy(self))
        self.camera = gameobject.make_camera(self)
        self.gameobjects.append(self.camera)

        maze_set = maze.generate_maze_set(6,6)
        for (r,c) in maze_set:
            self.gameobjects.append(gameobject.make_wall(self, (30+r*64,30+c*64)))

    def handle_events(self):
        '''Process input and events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
                

    def update(self, dt):
        '''Update the internal state of the game'''
        self.space.step(dt)

        for gameobj in self.gameobjects:
            gameobj.update(dt)
    
    def get_display_size(self):
        return Vector2(self.display.get_size())

    def draw(self, display, camera):
        '''Draw the game objects to the screen'''
        self.display.fill(self.BACKGROUND_COLOR)

        self.draw_game(display, camera)

        if self.is_drawing_debug:
            self.draw_debug()
        
        pygame.display.flip()

    def draw_game(self, display, camera):
        '''Draws the official game stuff (not the debug stuff)'''
        for gameobj in self.gameobjects:
            gameobj.draw(display, camera)

        self.draw_crosshair()

    def draw_crosshair(self):
        ''''Draws the crosshair to the center of the screen'''
        # TODO: Make this more efficient, and clean
        crosshair_radius = 30
        crosshair_alpha = 80
        crosshair_size = Vector2(crosshair_radius, crosshair_radius)
        crosshair_surface = pygame.Surface(crosshair_size, pygame.SRCALPHA)
        crosshair_surface.set_alpha(crosshair_alpha)
        pygame.draw.circle(crosshair_surface, (255,255,0), crosshair_size/2, crosshair_size.x / 2)
        self.display.blit(crosshair_surface, self.get_display_size()/2 - crosshair_size/2)
    
    def draw_debug(self):
        # TODO: Optimize this!
        self.debug_surface.fill((0,0,0))
        self.space.debug_draw(self.pymunk_draw_options)
        pos = self.get_display_size()/2 - self.camera.components[components.Physics].body.position
        self.display.blit(self.debug_surface, pos)

    def play(self):
        while self.is_running:
            # dt is the amount of seconds since the last frame
            dt = self.clock.tick(self.FPS) / 1000

            self.handle_events()
            self.update(dt)
            self.draw(self.display, self.camera)

        pygame.quit()
