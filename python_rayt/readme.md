# Python Ray Tracing

## Table of Contents

### [1. Geometries](#geometries)
- 1.1 Vec3
- 1.2 Sphere

### [2. Rendering](#rendering)
- 2.1 Hittable
- 2.2 Camera
- 2.3 Ray
- 2.4 Interval

### [3. Materials](#materials)
- 3.1 Material
- 3.2 Metal
- 3.3 Dielectric
- 3.4 Lambertian

### [4. Utilities & more](#utilities-&-more)
- 4.1 Utilities
- 4.2 Renderer
- 4.3 Benchmarker

---

### Geometries

This section is to show how is the Vec3 class working and how to generate a Sphere in the Scene

<a name="vec3"></a>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Vec3</h4>


The `Vec3` class represents a three-dimensional vector. It is used to store and manipulate coordinates in three-dimensional space. It is implemented with a series of utility methods to perform basic mathematical operations (+,-,x,/) as well as linear algebra's ones (dot product, cross product, lenght calculations, vector normalization, ecc)
It also includes methods for generating random vectors, calculating reflections and refractions, and checking if a vector is near zero.
</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Sphere</h4>

<a name="sphere"></a>


The `Sphere` class is an implementation of the IHittable interface (explained further down), representing a spherical object in a ray tracing scene. It contains a center, radius, and material properties. The primary method, `hit`, is responsible for determining if a given ray intersects with the sphere.

The method computes the quadratic equation of the ray-sphere intersection and checks the discriminant to determine if there is a real root. If a valid root is found, it further verifies if the root is within the acceptable range defined by the `ray_t` parameter. If all conditions are met, the intersection details are recorded in the rec parameter, including the intersection point, normal vector, and material properties, so that the Camera class (explained further) can effectively show the pixels of the sphere in the final result.
</div>

---

### Rendering

This section is to show how generating a realistic image by simulating the behavior of light rays in a virtual scene is possible. It provides an overview of the key components involved in the rendering process, whose job is to perform calculations to get the intersections between rays and objects in the scene, determine the color of each pixel, and generate the final image.

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Hittable</h4>

It is composed by 3 main classes:

The `IHittable` abstract class serves as an interface for objects that can be hit by rays in the ray tracing simulation. This abstraction enables a unified approach to handling ray-object interactions across different geometric entities in the ray tracing project. (for this project only Spheres are used)

The `HitRecord` class encapsulates information about an intersection between a ray and a hittable object. It includes essential attributes regarding points, vectors and materials of the hittable object. The method `set_face_normal` ensures the determination of the front face of the hit, a crucial detail for subsequent shading calculations in the rendering process.

The `HittableList` class manages a list of hittable objects and provides methods for adding objects to the list (add), clearing the list (clear), and checking for intersections (hit). This class acts as a container for various hittable entities in a scene, which are stored in a 'world' variable. This list keeps track of all the objects that are to be rendered in the scene, as well as their properties
</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Camera</h4>

The `Camera` class is a fundamental component in the ray tracing project, responsible for simulating a virtual camera and capturing the scene. These are its main functionalities:

The class has essential image-related parameters such as `aspect_ratio`, `image_width`, `samples_per_pixel`, and `max_depth`, which determine the characteristics of the rendered image. The camera's orientation and position are specified by `vfov` (vertical field of view), `lookfrom` (position), `lookat` (target), and `vup` (up vector). Default values for image dimensions and other parameters are provided, but can be overwritten in the main function.

The `initialize` method sets up the camera by calculating viewport dimensions, orientation vectors (`u`, `v`, and `w`), and viewport and pixel vectors for subsequent ray casting. This is the step that defines the camera's perspective and ensures accurate rendering.

The `get_ray` method computes rays for each pixel in the image. It determines the ray direction based on the pixel's position and the camera's center, enabling the generation of rays for casting into the scene.

To enhance the visual quality, the `pixel_sample_square` method implements basic random sampling, introducing perturbations to pixel locations. This technique contributes to the anti-aliasing problem, reducing visual artifacts, known as the "staircase effect" or just "aliasing" in the final image.

The heart of the class lies in the `ray_color` method, where recursive ray tracing takes place. This method checks for intersections with hittable objects in the world and calculates the color based on material properties. In case of no intersection, a simple sky gradient is applied, providing a background color. The depth of the recursive function is set thanks to the `max_depth` attribute of the class

Finally, the `write_color` method handles the output by writing color information to a file in PPM format. Gamma correction and clamping are applied to ensure that the color values are within a valid range.
</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Ray</h4>

The `Ray` class represents a ray in 3D space, defined by its origin and direction. 

The `at` method computes a point along the ray's trajectory at a given parameter `t`. It's a convenient way to find the position of the ray at different distances and it's used to determine intersections.
</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Interval</h4>

The `Interval` class manages a numerical range defined by minimum (`t_min`) and maximum (`t_max`) values. It provides methods for checking containment, strict enclosure, and clamping values within the interval. Predefined instances include `empty` (an empty interval) and `universe` (covering the entire real number line) which proved quite helpful during the project. This is more of an utility class to compute intervals.
</div>

---

### Materials

Materials in the real worlds absorp, reflect and refract light in different manners. This section is to show how each material has different properties and how these can change the overall aspect of a surface, including shiny surfaces, transparent objects, and textured materials.

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Material</h4>

The `IMaterial` class serves as an abstract blueprint for materials in the ray tracing project. It declares an abstract method `scatter` that defines how rays interact with materials during scattering events. Subclasses will then implement this method to specify material-specific behaviours
</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Metal</h4>

The `Metal` class handles metal material properties. The `scatter` method calculates a realistic reflection on a metal surface. It combines a reflected ray with controlled fuzziness, introducing randomness.
</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Dielectric</h4>

The `Dielectric` class handles dielectric material properties. Dielectric objects are the non-metallic ones like plastic and glass

This `scatter` method first sets the attenuation to full white, indicating minimal light absorption and then calculates the refraction ratio based on whether the ray hit the front or back face of the material.

Next, it computes the angles and checks if refraction is possible thanks to the Snell's law. If not, the ray is reflected, otherwise it gets refracted 
</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Lambertian</h4>

The `Lambertian` class handles lambertian reflectance, also known as "matte". It is a type of surface that appears uniformly bright from all directions, and thus reflects the entire incident light. An example of lambertian material is wood

The `scatter` method generates a random scattering direction by adding the surface normal to a randomly generated unit vector. A check ensures that the scatter direction is not degenerate (zero or close to zero), and if so, it is set to the surface normal. The scattered ray is then updated, and the attenuation is set to the material's color.
</div>

---

### Utilities & more

This section is to show the last part of the project, the utilities functions utilized, how is the renderer handled and how is the benchmarker working

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Utilities</h4>

This file is used to handle functions that have been used inside many different modules of the proejct. They are placed here to have a common repository to get these functions easily when needed. It is included: the linear interpolation (`lerp`), random double generation (`random_double` and `random_double_range`), gamma correction (`linear_to_gamma`), and conversion between degrees and radians (`degrees_to_radians`).
</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Renderer</h4>

The `Renderer` class is the one whose responsibility is the rendering process. Its primary function, the `render` method, takes in parameters that will eventually overwrite the default `Camera`'s ones.

Within this method, a virtual scene is constructed using a `HittableList` named `world`. Here both material and position as well as the color of the sphere are set randomly for each sphere, while the number of spheres is set before the rendering. (When benchmarking the randomness seed will be the same so that we have a way to compare)

The rendering process is initiated with the `cam.render(world)` method, where rays are cast into the scene, intersections with objects are handled, and pixel colors are calculated based on material interactions. 

</div>

<div style="margin-left: 20px">
    <h4 style="margin-left: -10px">Benchmarker</h4>

The benchmarker.py script file is where all the benchmarks happens.
It is using a decorator to measure times (using time module) and memory (using tracemalloc module).
It basically takes three array and generate all the possible combinations of parameters to pass to the renderer and then it runs the renderer with those parameters and prints the results.
To have a deeper inside of the benchmarking process, please refer to the [Comparisons](../docs/comparisons.md) file.

</div>
