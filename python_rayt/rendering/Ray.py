class Ray:

    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = direction

    def at(self, t):
        return self.origin + t * self.direction

    def copy(self, ray2):
        self.origin = ray2.origin
        self.direction = ray2.direction
