import math
from Material import IMaterial
from Vec3 import Color
from Ray import Ray
from utilities import random_double


class Dielectric(IMaterial):
    def __init__(self, index_of_refraction):
        self.ir = index_of_refraction

    @staticmethod
    def reflectance(cosine, ref_idx):
        r0 = (1 - ref_idx) / (1 + ref_idx)
        r0 = r0 * r0
        return r0 + (1 - r0) * pow((1 - cosine), 5)

    def scatter(self, r_in, rec, attenuation, scattered):
        attenuation.copy(Color(1.0, 1.0, 1.0))
        refraction_ratio = 1.0 / self.ir if rec.front_face else self.ir

        unit_direction = r_in.direction.unit_vector()

        cos_theta = min(-unit_direction.dot(rec.normal), 1.0)
        sin_theta = math.sqrt(1.0 - cos_theta * cos_theta)

        cannot_refract = refraction_ratio * sin_theta > 1.0

        if(cannot_refract or Dielectric.reflectance(cos_theta, refraction_ratio) > random_double()):
            direction = unit_direction.reflect(rec.normal)
        else:
            direction = unit_direction.refract(rec.normal, refraction_ratio)

        refracted = unit_direction.refract(rec.normal, refraction_ratio)

        scattered.copy(Ray(rec.p, refracted))

        return True