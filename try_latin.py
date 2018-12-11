#two functions - wordToPig- 1 parameter and nameToPig- 2 parameters
#step 1: wordToPig will convert word by moving the first cons to the end and add ay to the end or yay if the first letter is a vowel
    #for bonus, move all the constants to the end and add ay
#step 2: the nameToPig uses the wordToPig and has a first and last name
#step 3: just print the two names for the user

#defining the wordToPig function
def wordToPig(pig_word):
    first_letter = pig_word[0] #assigning the first letter of the word to a variable

    #if statment for if the word begins with a vowel
    if first_letter in ['A', 'E', 'I', 'O', 'U']:
        vowel_word = pig_word + 'yay' #keeps the word as is and adds the yay at the end
        return vowel_word #returns the pig latin word

    #statement if the word does not start vowel
    else:
        word = pig_word.lower() #lowercases all characters in the word
        c_word = word[1:] + word[0] #automatically places the first letter at the end

        #for loop for finding where the first vowel of the word is
        for letter in c_word:
            if letter not in ['a', 'e', 'i', 'o', 'u']:
                c_word = c_word[1:] + c_word[0]
            else:
                break

        #adds 'ay' to the word that has the vowel as the first letter
        c_word += 'ay'
        cons_word = c_word.capitalize() #capitalizes the first letter of new word
        return cons_word #returns the pig latin word

#defining the nameToPig fuction
def nameToPig(first_name, last_name):
    first_word = wordToPig(first_name)
    second_word = wordToPig(last_name)
    full_name = first_word + " " + second_word #adds the first word, space, and second word to print both the first and last name together
    return full_name #returns the pig latin word with first and last name together

print()
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")

try:
    f1 = nameToPig(first_name.strip(), last_name.strip()) #we discussed .strip method in class - removes trailing/leading whitespace
    print()
    print("The name in pig latin is",f1)
    print()
except FileNotFoundError:
    print("Invalid file name")
