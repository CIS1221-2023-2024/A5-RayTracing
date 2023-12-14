from hittable import Hittable
from math import sqrt

class Sphere(Hittable):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
    def hit(self, r, ray_tmin, ray_tmax, rec):
        oc = r.origin - self.center
        a = r.direction.length_squared()
        half_b = r.direction.dot(oc)
        c = oc.length_squared() - self.radius**2

        discriminant = half_b*half_b - a*c
        if (discriminant < 0):
            return False
            
        sqrtd = sqrt(discriminant)

        root = (-half_b - sqrtd) / a
        if (root <= ray_tmin or ray_tmax <= root):
            root = (-half_b + sqrtd) / a
            if (root <= ray_tmin or ray_tmax <= root):
                return False
        rec.t = root
        rec.p = r.at(rec.t)
        normal = (rec.p - self.center) / self.radius
        rec.set_face_normal(r, normal)

        return True
