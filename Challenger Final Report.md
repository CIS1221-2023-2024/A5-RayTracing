Ray Tracing Program Report

General:

In this project two programs were created where ray tracing was implemented using python. However one of the implementations made use of NumPy while the other implementation did not make any use of NumPy. The results of the outcome of the program were shown by the team and as can be seen from the results it was a job well done. The suggestions which I as a challenger suggested reduced the execution time, improved code readability, and made it more concise.

Utilities.py:

No suggestions were given as code could not be improved any further.

Ray.py:

I had suggested to make use of the copy function to store a copy of the contents of the origin and direction respectively so that you store a copy of the data at the moment the program is executing and if the original data is updated the copy is not updated.

Inerval.py:

A suggestion which consisted of removing the various if statements which made the code very long and replacing the if statements and making use of the min and max functions. This enhances code readability and makes it easier to understand. 

Vec3.py:

No suggestions were given as code could not be improved any further.

Hittable.py:

In the original version of this class inside the HittableList() class a new object was being  created with every iteration of the loop. I then provided a suggestion where rather than creating a new object with every iteration you can simply make use of the same rec object which was passed as a parameter inside the hit function.

Material.py:

The suggestion which I provided for this class consisted of changing the decorator for the abstract method as incorrect syntax was used for the decorator.

Metal.py:

The only enhancement which could be done to this class consisted of making use of the min function rather than making use of an if statement. This suggestion was correctly implemented and it improved code readability.

Lambertian.py:

No suggestions were given as code could not be improved any further.

Sphere.py:

An optimization which was suggested for this class was that rather than having to calculate the radius every time it is used, it is calculated beforehand and stored inside a variable and then only use that specific variable. This reduces the number of calculations done by the program and in turn makes the program more efficient. This suggestion was correctly implemented by the team.

Dielectric.py:

A very simple improvement which was suggested for this class was to combine 2 lines into 1 by rather than calculating its value and storing it in r0 and then using another line to overwrite r0 with its square you store its square in r0 immediately.

Camera.py:

No suggestions were given as code could not be improved any further.

Conclusion:

Overall, there was good cooperation between myself the challenger and the team members as I received feedback by the team members about my suggestions and most of my suggestions were implemented as suggested.
