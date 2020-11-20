from pygame import Vector2

from components import Sprite, Physics, WASDControlled, Wiggle, Follow, FollowType

class GameObject:
    def __init__(self, game, components):
        '''
        components -- list of Components objects
        '''
        self.game = game
        # self.components is a Dict mapping Component classes (the keys) to Component objects (the values)
        self.components = {type(comp) : comp for comp in components}
        for component in components:
            component.gameobject = self
            component.setup()

    def update(self, dt):
        for component in self.components.values():
            component.update(dt)

    def draw(self, display, camera):
        # The physics debug drawing is done outside GameObject.draw
        # Later, we might want to change this so other components can draw too
        if Sprite in self.components:
            self.components[Sprite].draw(display, camera)
    #     pygame.draw.rect(display, constants.CYAN, self.get_rect())
    #     print(self.get_rect())

    # def get_rect(self):
    #     return pygame.Rect(self.components[Physics].body.position - self.components[Physics].size/2, self.components[Physics].size)

### The GameObjects ###

def make_player(game):
    return GameObject(game, components = [
        Sprite('tank_0.png', size = Vector2(32, 32)), 
        WASDControlled(200), 
        Physics(debug_color = (0,255,0,50))
    ])

def make_enemy(game):
    return GameObject(game, components = [
        Sprite('brick.png', size = Vector2(32, 32)), 
        Follow(target=game.player), 
        Wiggle(1), 
        Physics(debug_color = (255,0,0,50))
    ])

def make_wall(game, pos):
    return GameObject(game, components = [
        Sprite('block.png'), 
        Physics(pos = pos, debug_color = (150,150,255,50), is_dynamic=False)
    ])

def make_camera(game):
    return GameObject(game, components = [
        Physics(debug_color = (255, 0, 255, 50), size = Vector2(10,10), is_collidable=False), 
        Follow(target=game.player, follow_type=FollowType.EXPONENTIAL_DECAY),
    ])