from python_rayt.geometries.Sphere import Sphere
from python_rayt.geometries.Vec3 import Color, Point3
from python_rayt.materials.Dielectric import Dielectric
from python_rayt.materials.Lambertian import Lambertian
from python_rayt.materials.Metal import Metal
from python_rayt.rendering.Camera import Camera
from python_rayt.rendering.Hittable import HittableList
from python_rayt.utilities import random_double_range, random_double


class Renderer:
    def render(samples, width, depth, number, output, numpy, ratio):
        world = HittableList()

        ground_material = Lambertian(Color(0.5, 0.5, 0.5))
        world.add(Sphere(Point3(0,-1000,0), 1000, ground_material))

        for a in range(-number,number):
            for b in range(-number,number):
                choose_mat = random_double()
                center = Point3(a + 0.9*random_double(), 0.2, b + 0.9*random_double())

                if ((center - Point3(4, 0.2, 0)).length() > 0.9):
                    sphere_material = None

                    if (choose_mat < 0.8):
                        albedo = Color.random(0,1) * Color.random(0,1)
                        sphere_material = Lambertian(albedo)
                        world.add(Sphere(center, 0.2, sphere_material))
                    elif (choose_mat < 0.95):
                        albedo = Color.random(0.5, 1)
                        fuzz = random_double_range(0, 0.5)
                        sphere_material = Metal(albedo, fuzz)
                        world.add(Sphere(center, 0.2, sphere_material))
                    else:
                        sphere_material = Dielectric(1.5)
                        world.add(Sphere(center, 0.2, sphere_material))
                    


        material1 = Dielectric(1.5)
        world.add(Sphere(Point3(0, 1, 0), 1.0, material1))

        material2 = Lambertian(Color(0.4, 0.2, 0.1))
        world.add(Sphere(Point3(-4, 1, 0), 1.0, material2))

        material3 = Metal(Color(0.7, 0.6, 0.5), 0.0)
        world.add(Sphere(Point3(4, 1, 0), 1.0, material3))

        cam = Camera()
        cam.aspect_ratio = ratio
        cam.image_width = width
        cam.samples_per_pixel = samples
        cam.max_depth = depth
        cam.filename = output
        

        cam.render(world)