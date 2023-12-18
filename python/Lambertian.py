from Material import IMaterial
from Ray import Ray
from Vec3 import Color, Vec3


class Lambertian(IMaterial):
    def __init__(self, albedo : Color):
        self.albedo = albedo

    def scatter(self, r_in, rec, attenuation, scattered):
        scatter_direction = rec.normal + Vec3.random_unit_vector()

        #Catch degenerate scatter direction
        if (scatter_direction.near_zero()):
            scatter_direction = rec.normal
        r = Ray(rec.p,scatter_direction)
        scattered.copy(r)
        attenuation.copy(self.albedo)
        return True