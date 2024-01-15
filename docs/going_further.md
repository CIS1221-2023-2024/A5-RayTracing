# Going Further

Our exploration has just scratched the surface of what a raytracer can achieve. For those looking to dive deeper, consider the following optimizations and feature additions:

- Other Shapes: Implementing shapes beyond spheres, (everything can be expressed as a sum of triangles).
- Lights
- Volumes: Exploring volumetric path tracing for added realism.
- Depth Of Field
- Monte Carlo Integration

These are all extremely computer-graphics related stuff, however, there are still some things that we can do to improve the performance of our python raytracer:

- Using GPU for calculation via the CUDA module
- Refactoring our multiprocessing architecture to render chunk of images vertically and not horizontally. 
- Refactoring our multiprocessing architecture to use a Process pool instead of assigning each process a task. This can improve the efficiency because, since image is not evenly distributed in objects to render, some process will by force finish earlier, lowering down the pixel rendered per minute. If a process can be reused after it completed the job, we could approach a solution that is, in our estimate, 10-20% faster.

We had a lot of fun uncovering the world of Ray Tracing, I hope you'll have fun too!

Our exploration has just scratched the surface of what a raytracer can achieve. For those looking to dive deeper, consider the following optimizations and feature additions:

1. **Other Shapes:** Implementing shapes beyond spheres, as everything can be expressed as a sum of triangles.

2. **Lights:** Introduce various light sources to enhance the realism and visual appeal of the scenes.

3. **Volumes:** Explore volumetric path tracing to add realism by simulating the interaction of light with participating media.

4. **Depth Of Field:** Enhance visual aesthetics by implementing depth of field effects to simulate realistic camera focus.

5. **Monte Carlo Integration:** Implement advanced rendering techniques such as Monte Carlo integration to achieve more accurate and visually pleasing results with less rendering time.

While these improvements are heavily focused on computer graphics, there are still ways to optimize the performance of our Python raytracer:

- **Using GPU for Calculation:** Using the CUDA module to offload computation to the GPU.
- **Refactoring Multiprocessing Architecture (Vertical Rendering):** Instead of rendering images horizontally, consider rendering chunks of images vertically. This can optimize work distribution among workers.

- **Refactoring Multiprocessing Architecture (Process Pool):** Instead of assigning each process a task, use a Process pool to efficiently manage the distribution of tasks among available processes. Reusing processes that finish early can lead to a 10-20% improvement in rendering speed, especially when the image distribution across objects is uneven.

We had a lot of fun uncovering the world of Ray Tracing, and we hope you'll enjoy exploring these optimizations and enhancements too!
