from python_numpy_rayt.materials.Material import IMaterial
from python_numpy_rayt.rendering.Ray import Ray
from python_numpy_rayt.geometries.Vec3 import Color, Vec3


class Lambertian(IMaterial):
    def __init__(self, albedo : Color):
        self.albedo = albedo

    def scatter(self, r_in, rec, attenuation, scattered):
        scatter_direction = rec.normal + Vec3.random_unit_vector()

        #Catch degenerate scatter direction
        scatter_direction = rec.normal if scatter_direction.near_zero() else scatter_direction
        r = Ray(rec.p,scatter_direction)
        scattered.copy(r)
        attenuation.copy(self.albedo)
        return True