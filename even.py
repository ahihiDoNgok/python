#prompt user for even numbers
#add the even numbers together
#if there is an odd number, we skip that w/ continue statement and move on
#use a . to exit

num_str = input("Enter in even numbers: ") #leaving in str because the . is a string to exit
the_sum = 0 #dont use just sum - if it says sum(), thats something else

while num_str != ".":
    num = int(num_str)
    if num % 2 ==1: #checking if number is odd
        print("Only even numbers, please try again")
        num_str = input("Enter in even numbers: ")
        continue
    the_sum += num #storing the numbers provided by user
    num_str = input("Enter in even numbers: ")

print("The sum is:",the_sum)
