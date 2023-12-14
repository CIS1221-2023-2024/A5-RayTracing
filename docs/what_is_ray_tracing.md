# What is ray tracing and how it works

Ray tracing is a technique for rendering high-fidelity 3D images, there are various implementation of ray tracing such as ray casting, recursive ray tracing, distribution ray tracing, photon mapping and path tracing.
In this project, we will focus on **path tracing**
With ray tracing, we can simulate various optical effects such as reflection, refraction, soft-shadows and many more
There are two main problems that a renderer should solve to output us an image:

- Visibility problem ( what is the first object that intersects the camera?)
- Shading problem ( computing the visibility between two surfaces )

## Ray tracing approach

Ray tracing, in particular, to compute photo-realistic images of 3D objects needs to achieve three steps:

- **Casting Rays:** cast a ray for each pixel in the image
- **Ray-Geometry Intersection:** test if a ray intersects any of the objects in the scene
- **Shading:** find out what the object "looks like" at the intersection point between the ray and the object

Let's see each of them in more details!

### Casting Rays

These phase involves casting a ray in the center of each pixel in the image.
These rays solve the visibility problem and are called primary rays (or camera ray). Additionally, this phase can also be called **ray-casting**

### Testing For Intersections

To actually display something, we need to check if our ray intersect any of the objects that are in our scene. For mathematically described shapes (AKA spheres, triangles, etc ), we can do this using a geometrical approach solving an equation.
- **SPHERE EQUATION**
  - /equation/
- **TRIANGLE EQUATION**
  - /equation/



## Bibliography

- [Ray Tracing Overview Scratchpixel](https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-overview/ray-tracing-rendering-technique-overview.html)