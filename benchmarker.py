from functools import wraps
from time import time
import tracemalloc
import sys
import os

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
        print(tracemalloc.get_traced_memory())

        tracemalloc.stop()
        return result
    return wrapper

@benchmark_decorator
def benchmark(function, **kargs):
    function(**kargs)

def main():
    settings = [{
        "samples": 1,
        "width": 100,
        "depth": 10,
        "number": 4,
        "output": "output.ppm",
        "numpy": False,
        "ratio": 16.0 / 9.0
    }, {
        "samples": 1,
        "width": 100,
        "depth": 10,
        "number": 4,
        "output": "output.ppm",
        "numpy": False,
        "ratio": 16.0 / 9.0
    
    }] * 2
    for idx,setting in enumerate(settings):
        setting['output'] = f"{setting['samples']}_{setting['depth']}_{setting['width']}_{setting['number']}_{'np' if setting['numpy'] else 'python'}_{idx}.ppm"
        renderer = PythonRenderer()
        benchmark(renderer.render, **setting)

if __name__ == "__main__":
    main()