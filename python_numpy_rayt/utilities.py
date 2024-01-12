import numpy as np

infinity = np.inf

def lerp(start, end, value):
    return (1 - value) * start + value * end

def random_double():
    return np.random.uniform(0, 1)

def random_double_range(min, max):
    return np.random.uniform(min, max)

def linear_to_gamma(linear):
    return np.sqrt(linear)

def degrees_to_radians(degrees):
    return degrees * np.pi / 180.0
