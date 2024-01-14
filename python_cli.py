import argparse

from python_rayt.Renderer import Renderer as PythonRenderer
 
def main():
    parser = argparse.ArgumentParser(
        prog="RaytracingCLI",
        description="A simple CLI for rendering images using our raytracer.",
        epilog="This is the epilog. It is a multiline string"
    )

    parser.add_argument("-s", "--samples", type=int, default=10, help="Number of samples per pixel")
    parser.add_argument("-w", "--width", type=int, default=100, help="Width of the output image")
    parser.add_argument("-d", "--depth", type=int, default=10, help="Depth of the shadow recursion")
    parser.add_argument("-n", "--number", type=int, default=4, help="Number of spheres (total_spheres =  (2 * N )**2)")
    parser.add_argument("-o", "--output", type=str, default="output.ppm", help="Output file name")
    parser.add_argument("-np", "--numpy", type=bool, default=False, help="Use numpy for calculations")
    parser.add_argument("-r", '--ratio', type=float, default=16.0 / 9.0, help="Aspect ratio of the image")
    parser.add_argument("-wr","--workers", type=int, default=4, help="Number of workers")
    parser.add_argument("-seed","--seed", type=int, default=None, help="Random seed")
 
    args = parser.parse_args().__dict__
    
    if args['width'] < 100:
        raise ValueError("Width must be at least 100.")
    
    renderer = PythonRenderer()
    renderer.render(**args)


if __name__ == '__main__':
    main()