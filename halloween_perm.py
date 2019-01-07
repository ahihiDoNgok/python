#tuple of 20 Halloween themed words and create permutations
#words have to be 5 letters or more
#the computer will randomly pick one word from the list and print a random permutation
#user has three guesses and has the option to quit
#should print whether the guess is correct or incorrect

#importing permuations/random module
from itertools import permutations
import random

print("In this game, you will be given a permuation of a Halloween themed word.")
print("You will have three tries to guess the word for one round and will be given the option to continue earning points or quit at the end of each round.")
print("Good luck!")

tuple_words = ('mummy', 'vampire', 'spooky', 'apple', 'candy', 'carve', 'costume', 'ghost', 'goblin', 'monster', 'orange', 'black', 'pumpkin', 'scary', 'spider', 'witch', 'zombie', 'haunted', 'broom', 'freaky')

#defining variables
count = 0
user_points = 0

while count == 0:
    random_words = [] #resets the list each time

    random_num = random.randint(0,19)
    random_pick = tuple_words[random_num] #using the random number and finding the index to pick a word from tuple

    #for loop for the list of permutations
    for char in permutations(random_pick):
        joined_words = "".join(char) #used the .join method to join the string together to display an element to user
        random_words.append(joined_words) #appending each loop to the list

    user_num = random.randint(0,len(random_words))
    perm_word = random_words[user_num] #finding the index of the random permutation to display to user

    print()
    print("Your permutation is:",perm_word)
    guess = input("What do you guess your word to be: ")
    count = 1

    #first guess loop
    if count == 1:
        if guess == random_pick:
            user_points += 1 #adds points to the user's total
            print()
            print("You guessed it! Your point total is now:",user_points)
            option = input("If you wish to play again to earn more points or quit, enter 'continue' or 'quit': ")

            if option == 'continue':
                count = 0 #loops back to the while statement above to play again
            else:
                break #exits the game
        else:
            print()
            print("Your guess was incorrect! You have two more tries!")
            guess = input("What do you guess your word to be: ")
            count = 2 #second guess loop

    #second guess loop
    if count == 2:
        if guess == random_pick:
            user_points += 1 #adds points to the user's total
            print()
            print("You guessed it! Your point total is now:",user_points)
            option = input("If you wish to play again to earn more points or quit, enter 'continue' or 'quit': ")

            if option == 'continue':
                count = 0 #loops back to the while statement above to play again
            else:
                break #exits the game
        else:
            print()
            print("Your guess was incorrect! You have one more try!")
            guess = input("What do you guess your word to be: ")
            count = 3 #third guess loop

    #third guess loop
    if count == 3:
        if guess == random_pick:
            user_points += 1 #adds points to the user's total
            print()
            print("You guessed it! Your point total is now:",user_points)
            option = input("If you wish to play again to earn more points or quit, enter 'continue' or 'quit': ")

            if option == 'continue':
                count = 0 #loops back to the while statement above to play again
            else:
                break #exits the game
        else:
            print()
            print("Your guess was incorrect! You have earned zero points for this round!")
            print("The word was:",random_pick)
            print("The total amount of points you have is:",user_points)
            print()
            option = input("If you wish to play again to earn more points or quit, enter 'continue' or 'quit': ")
            if option == 'continue':
                count = 0
            else:
                break #exits the game
