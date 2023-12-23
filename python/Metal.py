from Material import IMaterial
from Ray import Ray
from Vec3 import Color, Vec3


class Metal(IMaterial):
    def __init__(self, albedo : Color, fuzz : float):
        self.fuzz = fuzz if fuzz < 1 else 1
        self.albedo = albedo

    def scatter(self, r_in, rec, attenuation, scattered):
        reflected = Vec3.reflect(Vec3.unit_vector(r_in.direction), rec.normal)
        scattered.copy(Ray(rec.p, reflected + self.fuzz * Vec3.random_unit_vector()))
        attenuation.copy(self.albedo)
        return scattered.direction.dot(rec.normal) > 0