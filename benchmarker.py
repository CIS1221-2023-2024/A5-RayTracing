from functools import wraps
from time import time
import tracemalloc
import sys
import os
from itertools import product

sys.path.insert(1, os.path.realpath(os.path.pardir))
from python_rayt.Renderer import Renderer as PythonRenderer

def benchmark_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        time_start = time()
        tracemalloc.start()
        func(*args, **kwargs)
        time_end = time()
        time_duration = time_end - time_start
        current,peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        return [time_duration, current, peak]
    return wrapper

@benchmark_decorator
def benchmark(function, **kargs):
    return function(**kargs)

def generate_setting(samples = 10, width = 400, depth=5, number=6, output="output.png", numpy=False, ratio = 16/9, n_process = 4):
    return {
        "samples": samples,
        "width": width,
        "depth": depth,
        "number": number,
        "output": output,
        "numpy": numpy,
        "ratio": ratio,
        "n_process" : n_process
    }

def main():
    samples =  [1,50,100]
    depths = [5,10,20]
    widths = [100,1360]

    # Generate all possible combinations
    combinations = list(product(samples, depths, widths))

    totals = [list(combination) for combination in combinations]
    settings = [generate_setting(samples=total[0],depth=total[1],width=total[2]) for total in totals]

    for idx,setting in enumerate(settings):
        setting['output'] = f"./benchmarks/{setting['samples']}_{setting['depth']}_{setting['width']}_{setting['number']}_{'np' if setting['numpy'] else 'python'}_{idx}.ppm"
        renderer = PythonRenderer()

        heigth = int(setting['width'] / setting['ratio'])

        time_delta, current, peak = benchmark(renderer.render, **setting)
        pixel_per_minute = setting['width'] * heigth / time_delta * 60

        print(f"Total pixels: {setting['width'] * heigth}")
        print(f"Total time: {time_delta}")
        print(f"Pixels per minute: {pixel_per_minute}")
        print(f"Memory usage: {current / 10**6}MB")
        print(f"Peak memory usage: {peak / 10**6}MB")
        print(f"Samples: {setting['samples']}")
        print(f"Depth: {setting['depth']}")
        print(f"Width: {setting['width']}")

if __name__ == "__main__":
    main()