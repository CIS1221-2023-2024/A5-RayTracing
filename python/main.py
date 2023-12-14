from Vec3 import Vec3, Color, Point3
from Ray import Ray

FILENAME="./python/output.ppm"
aspect_ratio = 16.0 / 9.0
image_width = 400

image_height = int(image_width / aspect_ratio)
image_height = 1 if image_height < 1 else image_height

focal_length = 1.0
viewport_height = 2.0
viewport_width = viewport_height * (image_width / image_height)
camera_center = Point3(0, 0, 0)

viewport_u = Vec3(viewport_width, 0, 0)
viewport_v = Vec3(0, -viewport_height, 0)

pixel_delta_u = viewport_u / image_width
pixel_delta_v = viewport_v / image_height

viewport_upper_left = camera_center - Vec3(0, 0, focal_length) - viewport_u / 2 - viewport_v / 2
pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

def main():

    with open(FILENAME,"w") as f:
        f.write(f"P3\n{image_width} {image_height}\n")
        f.write("255\n")
        for i in range(image_height):
            for j in range(image_width):
                pixel_center = pixel00_loc + (j * pixel_delta_u) + (i * pixel_delta_v)
                ray_direction = pixel_center - camera_center
                r = Ray(camera_center, ray_direction)
                pixel_color = ray_color(r)
                write_color(f, pixel_color)

    print("\rDone.                 ")


def write_color(out, pixel_color):
    out.write(f"{int(255.999 * pixel_color.x)} ")
    out.write(f"{int(255.999 * pixel_color.y)} ")
    out.write(f"{int(255.999 * pixel_color.z)}\n")

def hit_sphere(center, radius, r):
    oc = r.origin - center
    a = r.direction.dot(r.direction)
    b = 2.0 * oc.dot(r.direction)
    c = oc.dot(oc) - radius*radius
    discriminant = b*b - 4*a*c
    return (discriminant >= 0)

def ray_color(r):
    if hit_sphere(Point3(0,0,-1), 0.5, r):
        return Color(1, 0, 0)

    unit_direction = r.direction.unit_vector()
    a = 0.5*(unit_direction.y + 1.0)
    return (1.0-a)*Color(1.0, 1.0, 1.0) + a*Color(0.5, 0.7, 1.0)

if __name__ =='__main__':
    main()