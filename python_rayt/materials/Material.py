from python_rayt.rendering.Hittable import HitRecord
from python_rayt.rendering.Ray import Ray
from abc import ABC, abstractclassmethod


class IMaterial(ABC):
    material = None

    @abstractclassmethod
    def scatter(r_in : Ray, rec : HitRecord, attenuation, scattered):
        pass