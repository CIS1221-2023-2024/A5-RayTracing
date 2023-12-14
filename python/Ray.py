class Ray:

    def __init__(self, origin, direction):
        self.orig = origin
        self.dir = direction

    @property
    def origin(self):
        return self.orig

    @property
    def direction(self):
        return self.dir

    def at(self, t):
        return self.orig + t * self.dir
