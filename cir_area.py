# calculate the  area and circumference of a circle from its radius
# Step 1: radius from user
# Step 2: apply the formulas - calculations
# Step 3: print out the results

import math # math is a module that Python provides to solve problems -this whole program is a module as well

#getting input from the user
radius_str = input("Enter the radius of your circle: ") # input means the code asks the user for x to solve
radius_int = int(radius_str) # radius_int function takes value from radius_str and changes it to remain an int, not a character

#adding formulas to use
circumference = 2 * math.pi * radius_int # ordering important, right side is evaluated and associated with left of =
area = math.pi * (radius_int ** 2) # (radius_int ** 2) = radius_int^2 and () = evaluate first then times with pi

print ("The circumference is:",circumference,  \
        ", and the area is:",area) # \ means that it continues to next line - it prints on the same line
