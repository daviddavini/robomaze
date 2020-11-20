import random
import math
from pygame import Vector2

import os

### Some useful functions ###

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) 

def try_normalize(v):
    if v == Vector2(0,0):
        return v
    return v.normalized()

def random_vector():
    theta = random.uniform(0, 2*math.pi)
    return Vector2(math.cos(theta), math.sin(theta))