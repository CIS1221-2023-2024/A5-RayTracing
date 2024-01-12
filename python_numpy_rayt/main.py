from python_numpy_rayt.Renderer import Renderer

def main():
    samples = 3
    width = 200
    depth = 3
    number = 11
    output = "output.ppm"
    numpy = False
    ratio = 16/9

    Renderer.render(samples, width, depth, number, output, numpy, ratio)

if __name__=="__main__":
    main()