#calculate quadratic formula
#step 1: ask user for a, b, c
#step 2: formula of square root and quadratic formulas
#step 3: print for user

import math

#input coefficient a, b, c from user
a_str = input("Enter coefficient a: ")
a_int = float(a_str)
b_str = input ("Enter coefficient b: ")
b_int = int(b_str)
c_str = input("Enter coefficient c: ")
c_int= int(c_str)

#formulas to print x=
discriminant = math.sqrt(b_int ** 2 - (4 * a_int * c_int)) #discriminant_int stands for the square root of the function
if discriminant < 0:
    print("The discriminant is negative")
else:
    quadratic_plus = float((-b_int + discriminant) / (2 * a_int)) #+ and - are split into two different modules to find x
    quadratic_minus = float((-b_int - discriminant) / (2 * a_int))
print("x=",quadratic_plus,"and x=",quadratic_minus)
