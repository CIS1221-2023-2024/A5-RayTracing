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
        result = func(*args, **kwargs)
        time_end = time()
        time_duration = time_end - time_start


        print(f'Took {time_duration:.3f} seconds')
        current,peak = tracemalloc.get_traced_memory()
        print(f'Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB')

        tracemalloc.stop()
        return result
    return wrapper

@benchmark_decorator
def benchmark(function, **kargs):
    function(**kargs)

def generate_setting(samples = 10, width = 400, depth=5, number=4, output="output.png", numpy=False, ratio = 16/9):
    return {
        "samples": samples,
        "width": width,
        "depth": depth,
        "number": number,
        "output": output,
        "numpy": numpy,
        "ratio": ratio
    }

def main():
    samples =  [5,50,100]
    depths = [5,10,20]
    widths = [480,1360,1920]

    # Generate all possible combinations
    combinations = list(product(samples, depths, widths))

    # Display the result
    totals = [list(combination) for combination in combinations]
    settings = [generate_setting(samples=total[0],depth=total[1],width=total[2]) for total in totals]
    for idx,setting in enumerate(settings):
        setting['output'] = f"./benchmarks/{setting['samples']}_{setting['depth']}_{setting['width']}_{setting['number']}_{'np' if setting['numpy'] else 'python'}_{idx}.ppm"
        renderer = PythonRenderer()
        benchmark(renderer.render, **setting)

if __name__ == "__main__":
    main()