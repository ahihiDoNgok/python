#have user choice destruct and construct
#destruct - prompt for alternade and output the two words (pie and and)
#construct - prompt them for 2 words and the output the alternade that would produced those words (pained)
#must be a real words

count = 0

choice = input("Would you like to destruct 'd' or construct 'c' an alternade: ")

while count == 0:
    if choice == 'd': #if user chooses destruct
        d_word = input("Enter in alternade: ")
        test = d_word.isalpha() #checks if string is alphabets
        if test == False:
            count = 0
        else:
            first_word = d_word[0::2]
            second_word = d_word[1::2]
            print("The words are",first_word,"and",second_word)
            break


    if choice == 'c': #if user selects construct
        first_c_word = input("Enter first word: ")
        second_c_word = input("Enter second word: ")

        first_test = first_c_word.isalpha() #checks if string is alphabets
        if first_test == False:
            count = 0
        second_test = second_c_word.isalpha() #checks if string is alphabets
        if second_test == False:
            count = 0
        else:
            count = 1

        if count == 1:
            index_count = 0 #count for second word
            word = ''
            for char in first_c_word:
                char
                word += char + second_c_word.upper()[index_count]
                index_count += 1
                if len(second_c_word) == index_count:
                    print("The word is",word) #print for user
                    break
