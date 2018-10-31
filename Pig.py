#step 1: print statement of directions to user_roll
#step 2: conditon for 'r'
#step 3: condition for 'h'
#step 4: print if counts >= 100, then user or computer wins

#importing random module
import random

print()
print("This game is a of version Pig, it is a dice game against a computer in which the first player to reach 100 points wins.")
print("If you roll a number between 2-6, you can roll again for more points in that round, or hold your current points to the next round.")
print("When you hold, the computer rolls until it reaches 20 points, but if it rolls a 1 on it's round, it'll earn 0 points for that round.")
print("Same goes for you! If you roll a 1, all your points for that round will be lost and it'll be the Computer's turn!")
print("Good luck!")

#defining count
count = 0

#defining loop control variables
user_count = 0 #total points for user for one round
user_sum = 0 #total points for user when user chooses to keep rolling and doesn't hold
user_total = 0 #the total value of points for user
comp_sum = 0  #total points for comp during one round
comp_total = 0 #the total point value for comp


while user_total < 100 and comp_total < 100:
    print()
    choice = input("Would you like to roll 'r' or hold 'h': ")
    print()

    #condition of choice 'r'
    if choice == 'r':
        user_roll = random.randint(1,6)  #assigning the dice roll to variable
        print("Your dice roll is:",user_roll) #printing dice roll to user
        print()
        if user_roll != 1:
            user_total = user_sum + user_roll + user_count #assigning user_total to its value
            print("You have",user_total,"points and the computer has",comp_total)
        #while loop
        if user_roll == 1:
            print("You rolled a one! Computer's turn")
            user_sum = 0 #sum of current round equals zero
        if user_roll != 1:
            user_sum += user_roll #total points for one round
    else:
        user_count += user_sum
        count = 1

    #condition of choice 'h'
    if choice == 'h' or user_roll == 1:
        user_sum = 0 #user_sum is equals 0 for its next round
        #user_count = user_count
        comp_roll = random.randint(1,6) #assigning the dice roll to variable

        if comp_roll == 1:
            comp_sum = 0 #sum of the round is 0 if 1 is dice roll
            comp_total += comp_sum #the comp total remains the same
        elif comp_roll > 1:
            while comp_sum <= 20 and comp_roll != 0: #rolls till it reaches 20 points
                comp_sum += comp_roll #total points for one round
                comp_roll = random.randint(1,6) #the dice keeps rolling
            comp_total = comp_sum + comp_total #total point value
        print("You have",user_count,"points and the computer has",comp_total,"points.")
        count = 1

    #condition at the end of each condition - checks if total ever equal to or greater than 100
    if count == 1:
        if user_total >= 100: #if the user reaches 100 or more points first
            print()
            print("You win! Your score is",user_total,"and the Computer Score is",comp_total)
            print("Congrats!")
            print()
            break #exit out of while loop
        if comp_total >= 100: #if the computer reaches 100 or more points first
            print()
            print("Computer wins! Your score is",user_count,"and the Computer Score is",comp_total)
            print("Better luck next time!")
            print()
            break #exit out of while loop
