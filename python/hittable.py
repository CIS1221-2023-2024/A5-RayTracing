from Vec3 import Vec3
from Interval import Interval

class Hittable:
    def hit(self, ray, ray_t, rec):
        pass

class HitRecord:
    def __init__(self):
        self.t = 0
        self.p = Vec3(0,0,0)
        self.normal = Vec3(0,0,0)

    
    def set_face_normal(self, ray, outward_normal):
        self.front_face = ray.direction.dot(outward_normal) < 0
        self.normal = outward_normal if self.front_face else -outward_normal

    def copy(self,rec2):
        self.t = rec2.t
        self.p = rec2.p
        self.normal = rec2.normal
        self.front_face = rec2.front_face

class HittableList():
    def __init__(self, objects = []):
        self.objects = objects
        self.hit_anything = False
        self.closest_so_far = float('inf')

    def add(self, object):
        self.objects.append(object)

    def clear(self):
        self.objects.clear()

    def hit(self, ray, ray_t, rec):
        temp_rec = HitRecord()
        self.hit_anything = False
        self.closest_so_far = ray_t.t_max

        for obj in self.objects:
            if obj.hit(ray, Interval(ray_t.t_min, self.closest_so_far), temp_rec):
                self.hit_anything = True
                self.closest_so_far = temp_rec.t
                rec.copy(rec2=temp_rec)
        return self.hit_anything
