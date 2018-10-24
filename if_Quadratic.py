#calculate quadratic formula
#step 1: ask user for a, b, c
#step 2: define the discriminant without the square root
#step 3: if discriminant < 0, print to user that discriminant is negative and cannot continue
#step 4: if discriminant > 0, add else function and square root the discriminant
#step 5: add quadratic function formula
#step 6: print answer for user

import math

#input coefficient a, b, c from user
a_str = input("Enter coefficient a: ")
a_int = int(a_str)
b_str = input ("Enter coefficient b: ")
b_int = int(b_str)
c_str = input("Enter coefficient c: ")
c_int= int(c_str)

#define discriminant
discriminant = (b_int ** 2 - (4 * a_int * c_int)) #discriminant stands for the square root of the function

#if discriminant < 0, print to user that discriminant is negative
if discriminant < 0:
    print("The discriminant is a negative number, cannot continue with problem.")

#if discriminant > 0, square root the discriminant and put into quadratic formula
else:
    discriminant = math.sqrt (discriminant)
    quadratic_plus = int((-b_int + discriminant) / (2 * a_int)) #+ and - are split into two different modules to find x
    quadratic_minus = int((-b_int - discriminant) / (2 * a_int))

    #print x= to user
    print("x=",quadratic_plus,"and x=",quadratic_minus)
