# What is ray tracing and how it works

Ray tracing is a technique for rendering high-fidelity 3D images, there are various implementation of ray tracing such as ray casting, recursive ray tracing, distribution ray tracing, photon mapping and path tracing.
In this project, we will focus on **path tracing**
With ray tracing, we can simulate various optical effects such as reflection, refraction, soft-shadows and many more
There are two main problems that a renderer should solve to output an image:

- Visibility problem (what is the first object that intersects the camera?)
- Shading problem (computing the visibility between two surfaces)

## Ray tracing approach

Ray tracing, in particular, to compute photo-realistic images of 3D objects needs to achieve three steps:

- **Casting Rays:** cast a ray for each pixel in the image
- **Ray-Geometry Intersection:** test if a ray intersects any of the objects in the scene
- **Shading:** find out what the object "looks like" at the intersection point between the ray and the object

Let's see each of them in more details

### Casting Rays

This phase involves casting a ray in the center of each pixel in the image.
These rays solve the visibility problem and are called primary rays (or camera rays). Additionally, this phase can also be called **ray-casting**

### Testing For Intersections

To actually display something, we need to check if our ray intersects any of the objects that are in our scene. 
For mathematically described shapes (AKA spheres, triangles, etc), we can do this using a geometrical approach to solve an equation.
- **SPHERE EQUATION**
  - /equation/
- **TRIANGLE EQUATION**
  - /equation/

For shapes of more complex objects like polygon meshes, subdivision surfaces or NURBS (Non-Uniform-Rational-B-Splines) the approach used for the geometrically described shapes becomes a bit more difficult, therefore, the easiest solution programmers have come up with is to abstract the object, converting each geometry type using the same, identical form of representation: a triangle. So even the most complex geometries can be fragmented (the exact term is "tessellated") into multiple more simple shapes.
Triangles, rather than other polygons, have been chosen to be the most atomic way of representing a complex object because of their mathamtical properties: they have a simple geometry with only 3 vertexes, many algorithms such as intersection tests, barycentric coordinates calculator and interpolation are simpler and more efficient computationally speaking. <br>

In ray tracing, whenever an intersection is found, the distance *t* from the camera to the intersection gets compared with the previous nearest distance *t*. At the end, when all the triangles have been tested, it is known which triangle is the closest, and which triangles got hit

### Shading

Once the object intersected with the ray is found, then we need to find out what the color of the object is at the intersection point. This requires the knowledge of:
- How much light is the point assorbing
- Which direction has the light 
- The property of the surface (its color, its refraction, its reflection, ecc)
- The observer position, since most surfaces do not reflect light equally in all directions, hence the amount of reflected light is likely to change depending on the camera and the observer position.

Some of the rays might also hit multiple surfaces and be reflected again.
While in the real world is the light that travels from the light source to the eye, in ray tracing this process is usually done differently, taking into consideration which rays is the viewpoint seeing first. This gets called *backward* tracing




## Bibliography

- [Ray Tracing Overview Scratchpixel](https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-overview/ray-tracing-rendering-technique-overview.html)