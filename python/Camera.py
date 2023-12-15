from Hittable import HitRecord
from Interval import Interval
from Ray import Ray
from utilities import infinity, lerp, random_double
from Vec3 import Color, Point3, Vec3

FILENAME="./python/output.ppm"

class Camera:

    #Image dimensions (these get passed from main)
    aspect_ratio = 1.0
    image_width = 100
    samples_per_pixel = 10

    image_height = 100
    camera_center = Point3(0,0,0)
    pixel00_loc = Point3(0,0,0)
    pixel_delta_u = Vec3(0,0,0)
    pixel_delta_v = Vec3(0,0,0)

    def render(self, world):
        self.initialize()

        with open(FILENAME,"w") as f:
            f.write(f"P3\n{self.image_width} {self.image_height}\n")
            f.write("255\n")
            for i in range(self.image_height):
                for j in range(self.image_width):
                    pixel_color = Color(0,0,0)
                    for sample in range(self.samples_per_pixel):
                        r = self.get_ray(j,i)
                        pixel_color += self.ray_color(r, world)
                    # pixel_center = self.pixel00_loc + (j * self.pixel_delta_u) + (i * self.pixel_delta_v)
                    # ray_direction = pixel_center - self.camera_center
                    # r = Ray(self.camera_center, ray_direction)
                    # pixel_color = self.ray_color(r, world)
                    self.write_color(f, pixel_color)

        print("\rDone.")

    def initialize(self):

        self.image_height = int(self.image_width / self.aspect_ratio)
        self.image_height = 1 if self.image_height < 1 else self.image_height

        focal_length = 1.0
        viewport_height = 2.0
        viewport_width = viewport_height * (self.image_width / self.image_height)

        # Viewport vectors
        viewport_u = Vec3(viewport_width, 0, 0)
        viewport_v = Vec3(0, -viewport_height, 0)

        # Pixel vectors
        self.pixel_delta_u = viewport_u / self.image_width
        self.pixel_delta_v = viewport_v / self.image_height

        # Pixel00 location
        viewport_upper_left = self.camera_center - Vec3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2
        self.pixel00_loc = viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)

    def get_ray(self, i, j):
        pixel_center = self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
        pixel_sample = pixel_center + self.pixel_sample_square()
        ray_direction = pixel_center - self.camera_center
        ray_origin = self.camera_center
        ray_direction = pixel_sample - ray_origin
        return Ray(ray_origin, ray_direction)
    
    def pixel_sample_square(self):
        px = -0.5 + random_double()
        py = -0.5 + random_double()
        return (px * self.pixel_delta_u) + (py * self.pixel_delta_v)

    def ray_color(self, r, world):
        rec = HitRecord()
        if (world.hit(r,Interval(0, infinity), rec)):
            return 0.5 * (rec.normal + Color(1,1,1))

        unit_direction = r.direction.unit_vector()
        a = 0.5*(unit_direction.y + 1.0)
        start = Color(1.0,1.0,1.0)
        end = Color(0.5,0.7,1.0)
        return lerp(start,end,a)
    

    def write_color(self, out, pixel_color):

        r = pixel_color.x
        g = pixel_color.y
        b = pixel_color.z

        scale = 1.0 / self.samples_per_pixel

        r *= scale
        g *= scale
        b *= scale

        intensity = Interval(0.000, 0.999)

        out.write(f"{int(255.999 * intensity.clamp(r))} ")
        out.write(f"{int(255.999 * intensity.clamp(g))} ")
        out.write(f"{int(255.999 * intensity.clamp(b))}\n")