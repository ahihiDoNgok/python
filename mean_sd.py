#step 1: prompts user for positive integers - stops storing when a negative number is entered
#step 2: stores values in a list
#step 3: print the integers in a sorted list
#step 4: compute the mean and standard deviation and print answers to user

print()
print("This program will find the mean and standard deviation of the positive integers you enter.")
print("When you would like to stop entering integers, enter in a negative number and you'll see the mean and standard deviation.")
print()

#importing math module for the square root of variance (standard deviation)
import math

#control variables
count = 0
sum = 0 #mean control variable
integer_squared = 0 #variance control variable
int_list = [] #defining the list variable

#while loop for entering integers
while count == 0:
    integers = float(input("Enter in positive integers: "))

    #if loop for entering values to the list
    if integers >= 0:
        int_list.append(integers) #appending the values added by the users to the list
    else:
        values = len(int_list) #assigning the length of the list to a variable
        count = 1


#if loop for putting the list in order and computing mean and standard deviation
if count == 1:
    int_list.sort()
    print()
    print("The integers you entered were:",int_list)

    #mean loop
    for i in int_list:
        sum += i
    mean = sum / values #formula for the mean - leaving the answer as a float for an accurate answer
    print("The mean of the integers is:", mean)

    #standard deviation loop
    for i in int_list:
        integer_squared += i **2 #taking the square of each value in int_list

    mean_squared = sum **2 / values #taking the sum of the values in int_list and squaring the sum and dividing by the amount of values

    var = (integer_squared - mean_squared) / values #the formula for the variance
    sd = math.sqrt(var) #the formula to find the standard deviation
    print("The standard deviation of the integers is:", sd)
    print()
