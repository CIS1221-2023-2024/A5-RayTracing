from Vec3 import Vec3, Color, Point3
import math
from Ray import Ray
from hittable import HitRecord, Hittable, HittableList
from sphere import Sphere
from utilities import infinity, lerp

FILENAME="./python/output.ppm"

# Image
aspect_ratio = 16.0 / 9.0
image_width = 400

# Image dimensions
image_height = int(image_width / aspect_ratio)
image_height = 1 if image_height < 1 else image_height

# World
world = HittableList()
world.add(Sphere(Point3(0,0,-1), 0.5))
world.add(Sphere(Point3(0,-100.5,-1), 100))

# Camera
focal_length = 1.0
viewport_height = 2.0
viewport_width = viewport_height * (image_width / image_height)
camera_center = Point3(0, 0, 0)

# Viewport vectors
viewport_u = Vec3(viewport_width, 0, 0)
viewport_v = Vec3(0, -viewport_height, 0)

# Pixel vectors
pixel_delta_u = viewport_u / image_width
pixel_delta_v = viewport_v / image_height

# Pixel location
viewport_upper_left = camera_center - Vec3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2
pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

def main():
    with open(FILENAME,"w") as f:
        f.write(f"P3\n{image_width} {image_height}\n")
        f.write("255\n")
        for i in range(image_height):
            for j in range(image_width):
                pixel_center = pixel00_loc + (j * pixel_delta_u) + (i * pixel_delta_v)
                ray_direction = pixel_center - camera_center
                r = Ray(camera_center, ray_direction)
                pixel_color = ray_color(r, world)
                write_color(f, pixel_color)

    print("\rDone.")

def write_color(out, pixel_color):
    out.write(f"{int(255.999 * pixel_color.x)} ")
    out.write(f"{int(255.999 * pixel_color.y)} ")
    out.write(f"{int(255.999 * pixel_color.z)}\n")

def ray_color(r, world : Hittable):
    rec = HitRecord()
    if (world.hit(r,0,infinity, rec)):
        return 0.5 * (rec.normal + Color(1,1,1))

    unit_direction = r.direction.unit_vector()
    a = 0.5*(unit_direction.y + 1.0)
    start = Color(1.0,1.0,1.0)
    end = Color(0.5,0.7,1.0)
    return lerp(start,end,a)

if __name__ =='__main__':
    main()