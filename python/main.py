from Vec3 import Point3
from Hittable import HittableList
from Sphere import Sphere
from Camera import Camera

# World
def main():
    world = HittableList()
    world.add(Sphere(Point3(0,0,-1), 0.5))
    world.add(Sphere(Point3(0,-100.5,-1), 100))

    cam = Camera()

    cam.aspect_ratio = 16.0 / 9.0
    cam.image_width = 400
    cam.samples_per_pixel = 10

    cam.render(world)

if __name__ =='__main__':
    main()