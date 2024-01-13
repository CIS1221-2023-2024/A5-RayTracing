from python_numpy_rayt.rendering.Hittable import IHittable
from math import sqrt

class Sphere(IHittable):
    def __init__(self, center, radius, mat):
        self.center = center
        self.radius = radius
        self.mat = mat
    
    def hit(self, r, ray_t, rec):
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = r.direction.dot(oc)
        c = oc.length_squared() - self.radius**2

        discriminant = half_b*half_b - a*c
        if (discriminant < 0):
            return False
            
        sqrtd = sqrt(discriminant)

        root = (-half_b - sqrtd) / a
        if not ray_t.surrounds(root):
            root = (-half_b + sqrtd) / a
            if not ray_t.surrounds(root):
                return False
        rec.t = root
        rec.p = r.at(rec.t)
        normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, normal)
        rec.mat = self.mat

        return True
