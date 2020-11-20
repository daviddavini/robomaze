import enum

import components
import utilities

class FollowType(enum.Enum):
    LOCKED_ON_TARGET = 1
    CONSTANT_SPEED = 2
    EXPONENTIAL_DECAY = 3

class Follow(components.Component):
    def __init__(self, target, speed = 40, decay_rate = 0.95, follow_type=FollowType.CONSTANT_SPEED):
        '''
        target - GameObject to follow
        speed - Used for FollowType.CONSTANT_SPEED. It's... just the speed.
        decay_rate - Used for FollowType.EXPONENTIAL_DECAY. The percent of distance to cover in one move
        '''
        super().__init__()
        self.speed = speed
        self.decay_rate = decay_rate
        self.target = target
        self.follow_type = follow_type

    def update(self, dt):
        if self.follow_type == FollowType.LOCKED_ON_TARGET:
            self.gameobject.components[components.Physics].body.position = (
                self.target.components[components.Physics].body.position)
        else:
            displacement = (self.target.components[components.Physics].body.position - 
                    self.gameobject.components[components.Physics].body.position)
            
            velocity = None
            if self.follow_type == FollowType.CONSTANT_SPEED:
                velocity = self.speed * utilities.try_normalize(displacement)
            elif self.follow_type == FollowType.EXPONENTIAL_DECAY:
                velocity = self.decay_rate * displacement
            self.gameobject.components[components.Physics].body.velocity = velocity