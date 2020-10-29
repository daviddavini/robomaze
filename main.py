import pygame

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
        self.player.update(dt)

    def draw(self, display):
        '''Draw the game objects to the screen'''
        self.display.fill(constants.BACKGROUND_COLOR)
        self.player.draw(display)
        pygame.display.flip()

    def __init__(self):
        ### Start the game ###
        pygame.init()

        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))

        self.is_running = True

        self.player = gameobject.GameObject()

    def play(self):
        while self.is_running:
            dt = self.clock.tick(constants.FPS) / 1000
            print(dt)
            self.handle_input()
            self.update(dt)
            self.draw(self.display)
            
        pygame.quit()

game = Game()
game.play()