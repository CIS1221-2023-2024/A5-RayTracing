from python_rayt.rendering.Hittable import HitRecord
from python_rayt.rendering.Ray import Ray
from abc import ABC, abstractmethod


class IMaterial(ABC):
    material = None

    @abstractmethod
    def scatter(r_in, rec, attenuation, scattered):
        pass