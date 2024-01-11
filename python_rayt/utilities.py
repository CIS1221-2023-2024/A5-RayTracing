import math
import random

infinity = float('inf')

def lerp(start,end,value):
    return (1-value) * start + value * end

def random_double():
    rand = random.uniform(0,1)
    return rand

def random_double_range(min, max):
    rand = random.uniform(min,max)
    return rand 

def linear_to_gamma(linear):
    return math.sqrt(linear)

def degrees_to_radians(degrees):
    return degrees * math.pi / 180.0