from math import tan
from python_rayt.rendering.Hittable import HitRecord
from python_rayt.rendering.Interval import Interval
from python_rayt.rendering.Ray import Ray
from python_rayt.utilities import degrees_to_radians, infinity, lerp, linear_to_gamma, random_double
from python_rayt.geometries.Vec3 import *
import copy
import multiprocessing


class Camera:
    #Image dimensions (these get passed from main)
    aspect_ratio = 1.0
    image_width = 100
    samples_per_pixel = 10
    max_depth = 10

    vfov = 90
    lookfrom = Point3(0,0,-1)
    lookat = Point3(0,0,0)  
    vup = Vec3(0,1,0);   
    u, v, w = Vec3(0,0,0), Vec3(0,0,0), Vec3(0,0,0)

    filename="output.ppm"
    pixels = []
    n_threads = 6

    image_height = 100
    camera_center = Point3(0,0,0)
    pixel00_loc = Point3(0,0,0)
    pixel_delta_u = Vec3(0,0,0)
    pixel_delta_v = Vec3(0,0,0)

    def render(self, world):
        self.initialize()
        threads = []
        manager = multiprocessing.Manager()
        pixels = manager.dict()
        idx = 0
        step = self.image_height // self.n_threads 
        remainder = self.image_height % self.n_threads
        for i in range(0, self.image_height, step):
            world_new = copy.deepcopy(world)

            if(i + step + remainder == self.image_height):
                step += remainder

            t = multiprocessing.Process(target=self.render_width, args=(idx,pixels,i,i + step,world_new))
            idx += 1
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

        self.write_file(pixels)

    def render_width(self,idx,pixels,h_start,h_end,world):
        results = []
        for i in range(h_start,h_end):
            for j in range(self.image_width):
                pixel_color = Color(0,0,0)
                for sample in range(self.samples_per_pixel):
                    r = self.get_ray(j,i)
                    pixel_color += self.ray_color(r, self.max_depth, world)
                results.append(pixel_color)

        pixels[idx] = results
        print("\rDone.")

    def initialize(self):

        self.image_height = int(self.image_width / self.aspect_ratio)
        self.image_height = 1 if self.image_height < 1 else self.image_height

        self.camera_center = self.lookfrom 

        focal_length = (self.lookfrom - self.lookat).length()

        focal_length = 1.0
        theta = degrees_to_radians(self.vfov)
        h = tan(theta/2)
        viewport_height = 2 * h * focal_length
        viewport_width = viewport_height * (self.image_width / self.image_height)

        w = (self.lookfrom - self.lookat).unit_vector()
        u = (self.vup.cross(w)).unit_vector()
        v = w.cross(u)

        # Viewport vectors
        viewport_u = viewport_width * u
        viewport_v = viewport_height * -v

        # Pixel vectors
        self.pixel_delta_u = viewport_u / self.image_width
        self.pixel_delta_v = viewport_v / self.image_height

        # Pixel00 location
        viewport_upper_left = self.camera_center - (focal_length * w) - viewport_u/2 - viewport_v/2
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

    def ray_color(self, r, max_depth ,world):
        rec = HitRecord()

        if(max_depth <= 0):
            return Color(0,0,0)
        if (world.hit(r,Interval(0.001, infinity), rec)):
            scattered = Ray(Vec3(1,1,1),Vec3(1,1,1))
            attenuation = Color()
            if(rec.mat.scatter(r,rec,attenuation,scattered)):
                return attenuation * self.ray_color(scattered,max_depth - 1,world)
            return Color(0,0,0)

        unit_direction = r.direction.unit_vector()
        a = 0.5*(unit_direction.y + 1.0)
        start = Color(1.0,1.0,1.0)
        end = Color(0.5,0.7,1.0)
        return lerp(start,end,a)
    
    def write_file(self, pixels):
        with open(self.filename,"w") as f:
            f.write(f"P3\n{self.image_width} {self.image_height}\n")
            f.write("255\n")
            for i in range(self.n_threads):
                for pixel in pixels[i]:
                    self.write_color(f,pixel)
        

    def write_color(self, out, pixel_color):

        r = pixel_color.x
        g = pixel_color.y
        b = pixel_color.z

        scale = 1.0 / self.samples_per_pixel

        r *= scale
        g *= scale
        b *= scale

        r = linear_to_gamma(r)
        g = linear_to_gamma(g)
        b = linear_to_gamma(b)

        intensity = Interval(0.000, 0.999)

        out.write(f"{int(255.999 * intensity.clamp(r))} ")
        out.write(f"{int(255.999 * intensity.clamp(g))} ")
        out.write(f"{int(255.999 * intensity.clamp(b))}\n")