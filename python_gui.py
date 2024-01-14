import tkinter as tk
from tkinter import messagebox
from python_rayt.Renderer import Renderer as PythonRenderer

import tkinter.messagebox as messagebox

import cv2
import matplotlib.pyplot as plt

window = tk.Tk()

def render_image(render_info):
    window.destroy()

    renderer = PythonRenderer()
    renderer.render(*render_info.values())

    img = cv2.imread("./results/" + render_info["output"])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis('off') 
    plt.show()
    
def createTKinter():
    window.title("Raytracing Parameters")
    window.geometry("500x450")

    # Add space at the top
    top_space = tk.Label(window, text="", font=("Arial", 12))
    top_space.grid(row=0, column=0, columnspan=2, pady=10)

    parameters = {
        "samples": {"label": "Samples per Pixel:", "default": 10},
        "width": {"label": "Image Width:", "default": 400},
        "depth": {"label": "Shadow Recursion Depth:", "default": 5},
        "number": {"label": "Number of Spheres:", "default": 4},
        "output": {"label": "Output File Name:", "default": "output"},
        "aspectRatioW": {"label": "Aspect Ratio Width:", "default": 16},
        "aspectRatioH": {"label": "Aspect Ratio Height:", "default": 9},
        "n_process": {"label": "Number of workers (processes):", "default": 8},
        "seed": {"label": "Random seed:", "default": 0}
    }

    row = 1  # Start from row 1 after the top space
    for param, info in parameters.items():
        label = tk.Label(window, text=info["label"], font=("Arial", 12))
        label.grid(row=row, column=0, pady=5)
        entry = tk.Entry(window, font=("Arial", 12), width=15)
        entry.grid(row=row, column=1, pady=5)
        entry.insert(0, str(info["default"]))
        parameters[param]["entry"] = entry
        row += 1

    render_button = tk.Button(window, text="Render Image", command=lambda: check_param_types(parameters), font=("Arial", 12), width=15)
    render_button.grid(row=row, column=0, columnspan=2, pady=10)

    message_label = tk.Label(window, text="Your file will be saved in the 'results' folder.", font=("Arial", 10))
    message_label.grid(row=row+1, column=0, columnspan=2, pady=5)

    # Center the content horizontally
    window.grid_columnconfigure(0, weight=1)
    window.grid_columnconfigure(1, weight=1)

    window.mainloop()

def check_param_types(parameters):
    try:

        width_entry = int(parameters["width"]["entry"].get())
        if width_entry < 100:
            messagebox.showerror("Invalid Input", "Width must be at least 100")
            return

        render_info = {
            "samples": int(parameters["samples"]["entry"].get()),
            "width": width_entry,
            "depth": int(parameters["depth"]["entry"].get()),
            "number": int(parameters["number"]["entry"].get()),
            "output": parameters["output"]["entry"].get() + '.ppm',
            "numpy": False, # numpy implementation has been done, but it won't be supported in the GUI due to low performances
            "ratio": float(parameters["aspectRatioW"]["entry"].get()) / float(parameters["aspectRatioH"]["entry"].get()),
            "n_process": int(parameters["n_process"]["entry"].get()),
            "seed": int(parameters["seed"]["entry"].get())
        }

        render_image(render_info)
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Input", "All the parameters (except 'output') must be integers!")

def main():
    createTKinter()

if __name__ == "__main__":
    main()