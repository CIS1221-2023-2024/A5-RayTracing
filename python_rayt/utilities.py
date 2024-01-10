import math
import random

infinity = float('inf')

def lerp(start,end,value):
    return (1-value) * start + value * end

def random_double():
    return random.uniform(0,1)

def random_double_range(min, max):
    return random.uniform(min, max)

def linear_to_gamma(linear):
    return math.sqrt(linear)