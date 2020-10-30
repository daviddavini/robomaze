import pygame
from pygame import Vector2
import pymunk
import pymunk.pygame_util

import maze
import gameobject
import constants

class Game:

    def handle_input(self):
        '''Process input and events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self, dt):
        '''Update the game objects'''
        self.space.step(dt)
        for gameobject in self.gameobjects:
            gameobject.update(dt)

    def draw(self, display):
        '''Draw the game objects to the screen'''
        self.display.fill(constants.BACKGROUND_COLOR)
        for gameobject in self.gameobjects:
            gameobject.draw(display)

        self.space.debug_draw(self.pymunk_draw_options)

        pygame.display.flip()

    def __init__(self):
        ### Start the game ###
        pygame.init()

        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))

        self.is_running = True

        self.space = pymunk.Space()
        self.space.gravity = 0,0  # No thank you, gravity
        self.pymunk_draw_options = pymunk.pygame_util.DrawOptions(self.display)
        pymunk.pygame_util.positive_y_is_up = False

        self.gameobjects = []

        player = gameobject.make_player(self)
        self.gameobjects.append(player)

        #self.gameobjects.append(gameobject.make_enemy(self, player))

        maze_set = maze.generate_maze_set(15,15)
        for (r,c) in maze_set:
            self.gameobjects.append(gameobject.make_wall(self, (100 + r*50, 100 + c*50)))

    def play(self):
        while self.is_running:
            dt = self.clock.tick(constants.FPS) / 1000
            self.handle_input()
            self.update(dt)
            self.draw(self.display)

        pygame.quit()

game = Game()
game.play()
