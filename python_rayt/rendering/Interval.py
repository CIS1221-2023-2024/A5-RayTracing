from python_rayt.utilities import infinity

class Interval:
    def __init__(self, _t_min=infinity, _t_max=-infinity):
        self.t_min = _t_min
        self.t_max = _t_max

    def contains(self, x):
        return self.t_min <= x <= self.t_max

    def surrounds(self, x):
        return self.t_min < x < self.t_max
    
    def clamp(self, x):
        return max(self.t_min, min(x, self.t_max))

empty = Interval(infinity, -infinity)
universe = Interval(-infinity, infinity)
