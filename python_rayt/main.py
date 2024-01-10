from python_rayt.geometries.Vec3 import Color, Point3
from python_rayt.rendering.Hittable import HittableList
from python_rayt.utilities import random_double, random_double_range
from python_rayt.rendering.Camera import Camera
from python_rayt.geometries.Sphere import Sphere
from python_rayt.materials.Lambertian import Lambertian
from python_rayt.materials.Metal import Metal
from python_rayt.materials.Dielectric import Dielectric
from python_rayt.Renderer import Renderer

def main():
    samples = 100
    width = 200
    depth = 50
    number = 11
    output = "output.ppm"
    numpy = False
    ratio = 16/9

    Renderer.render(samples, width, depth, number, output, numpy, ratio)

if __name__=="__main__":
    main()