# Python Ray Tracing

## Table of Contents

### [1. Geometries](#geometries)
- Vec3
- Sphere

### 2. Rendering
- 2.1 Hittable
- 2.2 Camera
- 2.3 Ray
- 2.4 Interval

### 3. Materials
- 3.1 Material
- 3.2 Metal
- 3.3 Dielectric
- 3.4 Lambertian

---

<a name="geometries"></a>

### Geometries

This section is to show how is the Vec3 class working and how to generate a Sphere in the Scene

#### Vec3
The Vec3 class represents a three-dimensional vector. It is used to store and manipulate coordinates in three-dimensional space. 
It is implemented with a series of utility methods to perform basic mathematical operations (+,-,x,/) as well as linear algebra's ones (dot product, cross product, lenght calculations, vector normalization, ecc)
It also includes methods for generating random vectors, calculating reflections and refractions, and checking if a vector is near zero.
The class is versatile and utilized extensively in the project also thanks to the 2 aliases that it has: the class Color is used to store rgb values while the class Point is used to store (x,y,z) coordinated of a point

#### Sphere

The Sphere class is an implementation of the IHittable interface (explained further down), representing a spherical object in a ray tracing scene. It contains a center, radius, and material properties. The primary method, hit, is responsible for determining if a given ray intersects with the sphere.

The method computes the quadratic equation of the ray-sphere intersection and checks the discriminant to determine if there is a real root. If a valid root is found, it further verifies if the root is within the acceptable range defined by the ray_t parameter. If all conditions are met, the intersection details are recorded in the rec parameter, including the intersection point, normal vector, and material properties, so that the Camera class (explained further) can effectively show the pixels of the sphere in the final result.

