from python_rayt.geometries.Sphere import Sphere
from python_rayt.geometries.Vec3 import Color, Point3, Vec3
from python_rayt.materials.Dielectric import Dielectric
from python_rayt.materials.Lambertian import Lambertian
from python_rayt.materials.Metal import Metal
from python_rayt.rendering.Camera import Camera
from python_rayt.rendering.Hittable import HittableList
from python_rayt.utilities import random_double_range, random_double
import random


class Renderer:
    def render(self,samples, width, depth, number, output, numpy, ratio, workers, seed):
        random.seed(seed)
        world = HittableList()
        world.clear()

        ground_material = Lambertian(Color(0.5, 0.5, 0.5))
        world.add(Sphere(Point3(0,-1000,0), 1000, ground_material))

        for a in range(-number,number):
            for b in range(-number,number):
                choose_mat = random_double()
                center = Point3(a + 0.9*random_double(), 0.2, b + 0.9*random_double())
                radius = random_double_range(0.1, 0.3)

                if ((center - Point3(4, 0.2, 0)).length() > 0.9):
                    sphere_material = None

                    if (choose_mat < 0.8):
                        albedo = Color.random(0,1) * Color.random(0,1)
                        sphere_material = Lambertian(albedo)
                        world.add(Sphere(center, radius, sphere_material))
                    elif (choose_mat < 0.95):
                        albedo = Color.random(0.5, 1)
                        fuzz = random_double_range(0, 0.5)
                        sphere_material = Metal(albedo, fuzz)
                        world.add(Sphere(center, radius, sphere_material))
                    else:
                        sphere_material = Dielectric(1.5)
                        world.add(Sphere(center, radius, sphere_material))
                    

        material3 = Metal(Color(0.7, 0.6, 0.5), 0.0)
        world.add(Sphere(Point3(4, 1, 0), 1.0, material3))

        cam = Camera()
        cam.aspect_ratio = ratio
        cam.image_width = width
        cam.samples_per_pixel = samples
        cam.max_depth = depth
        cam.filename = output
        cam.vfov     = 20
        cam.lookfrom = Point3(13,2,3)
        cam.lookat   = Point3(0,0,0)
        cam.vup      = Vec3(0,1,0)
        cam.n_process = workers

        cam.render(world)