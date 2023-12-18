from Material import IMaterial
from Ray import Ray
from Vec3 import Color, Vec3


class Metal(IMaterial):
    def __init__(self, albedo : Color):
        self.albedo = albedo

    def scatter(self, r_in, rec, attenuation, scattered):
        reflected = Vec3.reflect(Vec3.unit_vector(r_in.direction), rec.normal)
        r = Ray(rec.p,reflected)
        scattered.copy(r)
        attenuation.copy(self.albedo)
        return True