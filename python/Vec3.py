import math

from utilities import random_double, random_double_range

class Vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        self.e = [e0, e1, e2]

    @property 
    def x(self):
        return self.e[0]

    @property 
    def y(self):
        return self.e[1]
        
    @property 
    def z(self):
        return self.e[2]

    def __add__(self, other):
        return Vec3(self.e[0] + other.e[0], self.e[1] + other.e[1], self.e[2] + other.e[2])
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return Vec3(self.e[0] - other.e[0], self.e[1] - other.e[1], self.e[2] - other.e[2])

    def __mul__(self, other):
        if type(other) != Vec3:
            return Vec3(self.e[0] * other, self.e[1] * other, self.e[2] *other)
        return Vec3(self.e[0] * other.e[0], self.e[1] * other.e[1], self.e[2] * other.e[2])
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if(type(other) != Vec3):
            return self * (1/other)
        return Vec3(self.e[0] / other.e[0], self.e[1] / other.e[1], self.e[2] / other.e[2])

    def __rtruediv__(self, other):
        return self.__truediv__(other)

    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, item):
        return self.e[item]

    def __setitem__(self, key, value):
        self.e[key] = value

    def __str__(self):
        return f"Vec3({self.e[0]}, {self.e[1]}, {self.e[2]})"

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0]**2 + self.e[1]**2 + self.e[2] ** 2

    def dot(self,other):
        return self.e[0] * other.e[0] +  self.e[1] * other.e[1] + self.e[2] * other.e[2]

    def cross(self,v):
        return Vec3(self.e[1] * v.e[2] - self.e[2] * v.e[1],
            self.e[2] * v.e[0] - self.e[0] * v.e[2],
            self.e[0] * v.e[1] - self.e[1] * v.e[0])
    
    def unit_vector(self):
        return self / self.length()
    
    def ranodm():
        return Vec3(random_double(), random_double(), random_double())
    
    def random(min, max):
        return Vec3(random_double_range(min,max), random_double_range(min,max), random_double_range(min,max))
    
    @staticmethod
    def random_in_unit_sphere():
        while True:
            p = Vec3.random(-1,1)
            if p.length_squared() >= 1:
                return p

    @staticmethod       
    def random_unit_vector():
        return Vec3.random_in_unit_sphere().unit_vector()
    
    @staticmethod
    def random_on_hemisphere(normal):
        in_unit_sphere = Vec3.random_unit_vector()
        if in_unit_sphere.dot(normal) > 0.0:
            return in_unit_sphere
        else:
            return -in_unit_sphere
    
Color = Vec3
Point3 = Vec3