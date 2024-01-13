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
  The equation for a sphere of radius *r* centered at the origin is: $x^2 + y^2 + z^2 = r^2$
  So if any given point $(x,y,z)$ is on the sphere, then $x^2 + y^2 + z^2 = r^2$, if the point is inside the sphere, then $x^2 + y^2 + z^2 < r^2$ and if it is outside the sphere, then $x^2 + y^2 + z^2 > r^2$
  Suppose we want to allow the sphere center to be at an arbitrary point with coordinates $(C_x, C_y, C_z)$, then the equation becomes: $(x-C_x)^2 + (y-C_y)^2 + (z-C_z)^2 = r^2$.
  Generally speaking, we would like the formulas to be in terms of vectors so that all the coordinates can be expressed using a Vector class.
  This implies that the vector that goes from the center $C = (C_x, C_y, C_z)$ to a point $P = (x,y,z)$ is $(P - C)$
  Utilizing the definition of dot product between two vectors we get that the distance between center and point is equals to the definition of the sphere given a center of coordinates  $(C_x, C_y, C_z)$. Therefore, we can rewrite the equation as follows: $(P - C) \cdot (P - C) = r^2$
  We want to know wether our ray $P(t)$ ever hits the sphere anywhere.
  Given that $P$ is our Point, $P(t)$ is the function that casts the ray from that given point then 
  $P(t) = O + t b$, where O is the origin of the ray, b is the direction of the ray and t is the distance from the origin to the sphere. This means that if the equation solved for t does not give any value, the ray is not intersecting the sphere at any point, it follows that if the equation has one solution the ray is tangent to the sphere, if it has two the ray is hitting the sphere twice, hence it's secant.
  We can rewrite the equation as follows: $(P(t) - C) \cdot (P(t) - C) = r^2$, or rather
  $((O + tb) - C) \cdot ((O + tb) - C) = r^2$
  Solving for t, and using the quadratic formula we get that 
  $ a = b \cdot b, \newline
  b = 2b \cdot (O -C) \newline
  c = (A - C) \cdot (A - C) - r^2
  $
  Note that all the steps are not worked out in this paper since they are quite long
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
