#step 1: create two functions: complement and revComplement
#step 2: use complement in revComplement function
#step 3: only A, T, C, G are acceptable letters - tell user to try again if anything else is entered

#defining the complement function
def complement(dna_str):
    nucl_list = [] #control variable

    #for loop to go through the string one at a time
    for nucl in dna_str:
        if nucl == 'A':
            nucl_list.append('T') #if A then T is appended to the list

        elif nucl == 'T':
            nucl_list.append('A') #if T then A is appended to the list

        elif nucl == 'C':
            nucl_list.append('G') #if C then G is appended to the list

        elif nucl == 'G':
            nucl_list.append('C') #if G then C is appended to the list

    #joining the list to be one element
    join_nucl = "".join(nucl_list)

    return join_nucl #returns compliment to the user

#defing the reverse compliment function
def revComplement(dna_str):
    reverse_comp = complement(dna_str)[::-1] #calling the dna_to_comp function and indexing backwords to reserve the compliment
    return reverse_comp #returns value to user

dna_str = input("Enter a DNA Sequence: ")
count = 0

#while loop
while count == 0:

    #for loop for checking if the letters are A, T, C, and G
    for char in dna_str:

        if char not in ['A', 'T', 'G', 'C']:
            count = 1 ##when a letter is not A, T, C or G
        else:
            count = 2 #when a letter is A, T, C or G

    #loop for displaying on error to the user
    if count == 1:
        print()
        print("Error! Please enter a valid DNA sequence")
        print()
        break

#if statement to print answer to user
if count == 2:
    f1 = complement(dna_str)
    f2 = revComplement(dna_str)
    print()
    print("The complement of the DNA sequence is:",f1)
    print("The reverse complement of the DNA sequence is:",f2)
    print()
