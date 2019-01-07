#funcitions with area of circle, circumfernce, volume of sphere, volume of cyclinder
import math

def area_of_cir(radius_int):
    area_cir = int(radius_int ** 2) * math.pi
    return area_cir

def cir_of_circle(radius_int):
    cir_circle = 2 * radius_int * math.pi
    return cir_cirle

def vol_of_sphere(radius_int):
    vol_sphere = (4/3) * math.pi * (radius_int ** 3)
    return vol_sphere

def vol_of_cylin(radius_int, height_int):
    vol_cylin = math.pi * (radius_int **2) * height_int
    return vol_cylin

radius_int = int(input("Enter radius: "))
height_int = int(input("Enter height for volume of a cylinder: "))

f1 = area_of_cir(radius_int)
f2 = cir_of_circle(radius_int)
f3 = vol_of_sphere(radius_int)
f4 = vol_of_cylin(radius_int, height_int)

print(f1)
print(f2)
print(f3)
print(f4)
