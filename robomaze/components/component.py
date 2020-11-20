import abc

# hmm... maybe it doesn't need to be an abstract class
class Component(abc.ABC):

    def __init__(self):
        # Ensure that Component has attr. gameobject, even if not set
        self.gameobject = None

    def setup(self):
        '''For init logic requiring self.gameobject'''

    def update(self, dt):
        pass

    def draw(self, display, camera):
        pass