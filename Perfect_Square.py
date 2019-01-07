#calculate a perfect square root
#step 1: prompt user to enter a number
#step 2: determine if it is a perfect square
#step 3: print it's not perfect square if it is not and let user add another number
#step 4: print answer if it is a perfect square

import math

#assign conditional value (perfect_square)
perfect_square = 0 #setting the condition to false

#determine if it is perfect_square is the same as x
while perfect_square == 0:
    x = int(input("Enter a number: "))
    square_root = math.sqrt(x)
    square_root_int = int(square_root)

    if square_root == int(square_root):
        print("The perfect square of the number is",int(square_root))

        perfect_square = 1 #assign the conditional value to true

    else:
        print("The number is not a perfect square, please enter another number") #the condition is false, so it will loop back to while
