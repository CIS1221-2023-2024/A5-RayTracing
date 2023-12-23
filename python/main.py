from Vec3 import Color, Point3
from Hittable import HittableList
from Sphere import Sphere
from Camera import Camera
from Lambertian import Lambertian
from Metal import Metal
from Dielectric import Dielectric

def main():
    world = HittableList()

    material_ground = Lambertian(Color(0.8, 0.8, 0.0))
    material_center = Lambertian(Color(0.1, 0.2, 0.5))
    material_left = Dielectric(1.5)
    material_right = Metal(Color(0.8, 0.6, 0.2), 0.0)

    world.add(Sphere(Point3(0.0, -100.5, -1.0), 100.0, material_ground))
    world.add(Sphere(Point3(0.0, 0.0, -1.0), 0.5, material_center))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), 0.5, material_left))
    world.add(Sphere(Point3(-1.0, 0.0, -1.0), -0.4, material_left))
    world.add(Sphere(Point3(1.0, 0.0, -1.0), 0.5, material_right))
    
    cam = Camera()
    cam.aspect_ratio = 16.0 / 9.0
    cam.image_width = 400
    cam.samples_per_pixel = 10

    cam.render(world)

if __name__ == '__main__':
    main()