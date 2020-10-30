import pygame

from gameobject import GameObject, Movement, WASDControlled, Follow, Wiggle
import constants

class Game:

    def handle_input(self):
        '''Process input and events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self, dt):
        '''Update the game objects'''
        for gameobject in self.gameobjects:
            gameobject.update(dt)

    def draw(self, display):
        '''Draw the game objects to the screen'''
        self.display.fill(constants.BACKGROUND_COLOR)
        for gameobject in self.gameobjects:
            gameobject.draw(display)
        pygame.display.flip()

    def __init__(self):
        ### Start the game ###
        pygame.init()

        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((constants.DISPLAY_WIDTH, constants.DISPLAY_HEIGHT))

        self.is_running = True

        self.gameobjects = []

        player = GameObject(components = [Movement(300), WASDControlled()], color = constants.CYAN, size = (40, 40))
        self.gameobjects.append(player)

        enemy = GameObject(components = [Movement(50), Follow(player), Wiggle(1)], color = constants.RED, size = (20, 20))
        self.gameobjects.append(enemy)

    def play(self):
        while self.is_running:
            dt = self.clock.tick(constants.FPS) / 1000
            self.handle_input()
            self.update(dt)
            self.draw(self.display)
            
        pygame.quit()

game = Game()
game.play()