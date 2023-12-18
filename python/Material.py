from Hittable import HitRecord
from Ray import Ray
from abc import ABC,abstractclassmethod


class IMaterial(ABC):
    material = None

    @abstractclassmethod
    def scatter(r_in : Ray, rec : HitRecord, attenuation, scattered):
        pass