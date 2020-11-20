import random

import utilities
import components

class Wiggle(components.Component):
    def __init__(self, wiggle_amount):
        super().__init__()
        self.wiggle_amount = wiggle_amount

    def update(self, dt):
        self.gameobject.components[components.Physics].body.velocity += (
            random.uniform(0, self.wiggle_amount) * utilities.random_vector()
        )