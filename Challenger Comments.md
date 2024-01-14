Utilities.py

I do not see any improvements which can be done to this class.

Ray.py

In the at function a tuple can be used since it improves code readability. To make use of it replace the following line (line 8): return self.origin + t * self.direction by the below line: 		                   return tuple(a + t * b for a, b in zip(self.origin, self.direction))					           The zip function is basically equating a as self.origin and b as self.direction.

In the copy function to store a copy of the attributes of ray 2 the copy function can be used. This is recommended because when it is being referred to directly any changes made to the original data in ray 2 will also effect the data stored inside the copy when that is not the intention as what you really want to do is to store a copy of the data at that moment and this data cannot be changed. To make use of this function you first need to import the copy function using the line: import copy in the first line. Then you need to replace the line (line 11): self.origin = ray2.origin and the line (line 12): self.direction = ray2.direction with the lines self.origin = copy.copy(ray2.origin) and self.direction = copy.copy(ray2.direction) respectively. In this way the attributes self.origin and self.direction are independent are not dependent on the attributes inside ray2 but the attributes of the Ray instance are independent. This means that if anything inside ray2 is changed, those changes will not take effect on ray.

Interval.py

In the clamp function (lines 14-19) it is being checked if the value of x is greater than self._t_min and smaller than self._t_max. If it falls in that range it returns x but if it is smaller than self.t_min it returns self.t_min and if it is larger than self.t_max it returns self._t_max. This is done using a lot of if statements which does not make the code concise and makes code repetitive. Rather than using a lot of if statements the min and max functions can be used. These simplify the function and reduces the code inside the function to just 1 line rather than 5. 						 This is the way the function currently looks like:

![image](https://github.com/CIS1221-2023-2024/A5-RayTracing/assets/150594221/e3824e1b-17b4-4ecf-8c81-3d605bed70b5)

This is how it will look like after the min and max functions are used:

![image](https://github.com/CIS1221-2023-2024/A5-RayTracing/assets/150594221/6d756c8e-b7a5-4965-b591-15a434b28dfd)

In this way it first measures the smallest value between x and self.t_max and it then measures the largest value between self.t_min and the result from the previous operation. This will always work because if x is smaller than self.t_max the result will be self.t_max from the first operation and also from the second since self.t_max will always be larger than self.t_max and vice versa if x is smaller than self.t_min. While if it falls in the range, you will get x from the first operation and x from the second operation.

Vec3.py

Just like in the Ray.py class we can make use of the copy function to make a copy of v2 rather than manually referring to it. To do this we replace the lines:

self.e[0] = v2.e[0] (line 114)

self.e[1] = v2.e[1] (line 115)

self.e[2] = v2.e[2] (line 116)

with the lines:

self.e[0] = copy.copy(v2.e[0])

self.e[1] =copy.copy(v2.e[1])

self.e[2] = copy.copy(v2.e[2])

Apart from this I see nothing wrong with the code apart from the fact that NumPy can be used for various mathematical operations but since this version is without using NumPy it cannot be implemented.

Hittable.py

Rather than creating a new hit object every time the loop iterates, we can simply make use of the same rec object which was previously passed as a parameter of the function hit. This can be done by changing the line: temp_rec = HitRecord() (line 42) to temp_rec = rec. We can also remove the lines self.hit_anything = False (line 43) and self.closest_so_far = ray_t.t_max (line 44) since they were already initialized in the constructor __init__. If they are not removed, they will be initialized again every time the function is called. 

When making use of the copy function inside the hit function there is no need to specify that rec2=temp_rec inside the for loop (line 50) but you can simply write temp_rec only. In other words: rec.copy(rec2=temp_rec) becomes rec.copy(temp_rec).

Material.py

The decorator @abstractclassmethod in line 9 should be changed to @abstractmethod since that is the correct decorator to be used.

Just like the parameters r_in and rec were annotated with Ray and HitRecord respectively even the parameter scattered can be annotated with Ray since when saying scattered you are referring to a ray hence it is most probably referring to a ray.

Metal.py

Rather than using an if statement to check if fuzz should be returned or 1 should be returned in the __init__ function in line 8 the min function can be used. To do so replace: 		                

self.fuzz = fuzz if fuzz < 1 else 1 with self.fuzz = min(fuzz, 1)

Lambertian.py

You can make the code shorter by implementing the if statement from lines 14-15 in 1 line by replacing the below part:

![image](https://github.com/CIS1221-2023-2024/A5-RayTracing/assets/150594221/e57aab29-c64b-4fb3-8171-aff18625e800)

with just this 1 line: 

scatter_direction = rec.normal if scatter_direction.near_zero() else scatter_direction

Sphere.py

An optimization to this class which can be done is that of calculating the square of the radius beforehand inside the __init__ function and storing it inside a variable. For this to work you need to add this line inside the __init__ function self.radius_squared = radius**2 so this function will not look like this:

![image](https://github.com/CIS1221-2023-2024/A5-RayTracing/assets/150594221/19c71322-3c3d-4616-87c3-f5682bc59b28)

After this is done the line: c = oc.length_squared() - self.radius**2 (line 14) needs to be edited. We can remove the self.radius**2 part and replace it with self.radius_squared so the new line will now be this: c = oc.length_squared() - self.radius_squared.

A benefit of doing so is that in this way the square of the radius will only be calculated once and saved as opposed to having to calculate it every time it is used.

Dielectric.py

When calculating the value of r0 (lines 14-15) 2 lines of code are used which can be easily fitted into 1 lines of code making the code shorter by removing the below lines of code:

r0 = (1 - ref_idx) / (1 + ref_idx) (line 14)

r0 = r0 * r0 (line 15)

and combining them into 1 line of code like this: r0 = ((1 - ref_idx) / (1 + ref_idx))**2.

Camera.py

I do not see any improvements which can be done to this class.

main.Py

Rather than adding spheres one by one (lines 17-21), list comprehension can be used to add them all at once. The below code is removed:

world.add(Sphere(Point3(0.0, -100.5, -1.0), 100.0, material_ground)) (line 17)

world.add(Sphere(Point3(0.0, 0.0, -1.0), 0.5, material_center)) (line 18)

world.add(Sphere(Point3(-1.0, 0.0, -1.0), 0.5, material_left)) (line 19)

world.add(Sphere(Point3(-1.0, 0.0, -1.0), -0.4, material_left)) (line 20)

world.add(Sphere(Point3(1.0, 0.0, -1.0), 0.5, material_right)) (line 21)

and it is replaced by the following code:

spheres = [Sphere(Point3(0.0, 0.0, -1.0), 0.5, material_center), Sphere(Point3(-1.0, 0.0, -1.0), 0.5, material_left), Sphere(Point3(-1.0, 0.0, -1.0), -0.4, material_left), Sphere(Point3(1.0, 0.0, -1.0), 0.5, material_right)]

world.add(*spheres)

The star in the final line basically unpacks the list and adds every element one by one.
