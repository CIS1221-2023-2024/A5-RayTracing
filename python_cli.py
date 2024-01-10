import argparse

from python_rayt.Renderer import Renderer as PythonRenderer
#from numpy_rayt.Renderer import Renderer as NumpyRenderer
 
parser = argparse.ArgumentParser(
    prog="RaytracingCLI",
    description="A simple CLI for rendering images using our raytracer.",
    epilog="This is the epilog. It is a multiline string"
)
 
parser.add_argument("-s", "--samples", type=int, default=10, help="Number of samples per pixel")
parser.add_argument("-w", "--width", type=int, default=100, help="Width of the output image")
parser.add_argument("-d", "--depth", type=int, default=10, help="Depth of the shadow recursion")
parser.add_argument("-n", "--number", type=int, default=4, help="Number of spheres")
parser.add_argument("-o", "--output", type=str, default="output.ppm", help="Output file name")
parser.add_argument("-np", "--numpy", type=bool, default=False, help="Use numpy for calculations")
parser.add_argument("-r", '--ratio', type=float, default=16.0 / 9.0, help="Aspect ratio of the image")
 
args = parser.parse_args().__dict__
PythonRenderer.render(**args)