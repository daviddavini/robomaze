import pymunk
from pygame import Vector2

import components

class Physics(components.Component):
    def __init__( self, 
                pos = None, 
                size = None, 
                debug_color = (255,255,255,100), 
                is_dynamic = True,
                is_collidable = True
            ):
        '''
        size -- (width, height) of the hitbox. 
                If not specified, uses the Sprite Component's size
        is_collidable -- If False, doesn't create a box for object
        '''
        # Well, this stuff shouldn't really be used except for setup
        super().__init__()
        self.pos = pos
        self.size = size
        self.debug_color = debug_color
        self.is_dynamic = is_dynamic
        self.is_collidable = is_collidable

        # Defined in setup
        self.body = None
        self.poly = None

    def setup(self):
        # If pos is None, set pos to center of screen
        self.pos = self.pos or self.gameobject.game.get_display_size() / 2
        # If size is None, set size to size of sprite
        self.size = self.size or self.gameobject.components[components.Sprite].size

        body_type = pymunk.Body.DYNAMIC if self.is_dynamic else pymunk.Body.STATIC
        self.body = pymunk.Body(1, pymunk.inf, body_type)
        self.body.position = self.pos

        if self.is_collidable:
            corner_radius = 0
            self.poly = pymunk.Poly.create_box(self.body, self.size, corner_radius) #roundedness
            self.poly.color = self.debug_color

            self.gameobject.game.space.add(self.body, self.poly)
        
        else:
            self.gameobject.game.space.add(self.body)

    def update(self, dt):
        self.gameobject.pos = Vector2(self.body.position)