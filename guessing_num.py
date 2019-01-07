#using while-else loop w/ a break
#simple guessing game which provides hints to user

import random
num = random.randint (1,100)

guess_int = int(input("Guess a number: "))

while 0 <= guess_int <= 100:
    if guess_int > num:
        print("Guessed too high")
    elif guess_int < num:
        print("Guessed to low")
    else:
        print("You guessed it! The number was:",num)
        break #early exit - do not want to ask the user for the number again
    guess_int = int(input("Guess a number: ")) #if and elif will jump down here and it'll go over again; else is stopped b/c break
else:
    print("You quit early. The number was:",num) #if user adds a negative number, it'll quit playing

print("Something else") #shows that after the while-else loop, the code continues on
