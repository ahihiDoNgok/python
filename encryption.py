#This program is an encryption scheme that shifts all the letters in the alphabet by a fixed distances d
#6 functions - read_file, write_file, encrypt, build_dictionary, find_shift, and decrypt
#The full program should read a text file, encrypt and write the contents to a file, read in, decrypt and write the decryption to another text file

def read_file(file):
	my_file = open(file ,'r') ##opening the text file entered by the user and reading into it
	my_str = ""
	lines = my_file.readlines() #reading the lines of the file in order to enter it into a loop
	for elem in lines:
		my_str += elem #added the elements of the lines to a string
	my_file.close() #closing the file
	return my_str #returning the string

def write_file(str, file):
	my_file = open(file,'w') #opens the new file and has permission to write
	my_file.write(str) #writes string into encrypted.txt file
	my_file.close()

def encrypt(str, num):
	final_list = []
	my_str = str.lower() #case will not matter with this method
	my_list = list(my_str)

	for elem in my_list:
		if elem in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
		't', 'u', 'v', 'w', 'x', 'y', 'z']: #checks all the characters that are lowercase letters
			new_num = ord(elem) + num #ord() shows the ACII value assosiated with the elem and adds the the shift number
			if new_num > ord('z'):
				new_num -= 26 #if the element is larger than 'z', subtracts 26 to have it wrap back to the start of the alphabet
			new_char = chr(new_num)
			final_list.append(new_char) #appends new letter to a list
		else:
			final_list.append(elem) #appends the characters that arent letters to the list

	new_str = "".join(final_list) #joins the list together to one string
	write_file(new_str, 'encrypted.txt') #writes string to a new file
	return new_str


def build_dictionary(str):
	cmp_dict = {}
	new_list = []
	my_list = list(str) #changes the string to a list

	for char in my_list:
		if char in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
		't', 'u', 'v', 'w', 'x', 'y', 'z']:
			new_list.append(char)
		else:
			continue

	new_str = "".join(new_list)

	for elem in new_str:
		if elem in cmp_dict:
			cmp_dict[elem] += 1 #makes the key the letter and the value changes to have the count of occurances
		else:
			cmp_dict[elem] = 1

	return cmp_dict #returns the dictionary

def find_shift(dict):
	e_num = ord('e') #defining that e is the letter that occurs the most and storing 101 under the variable e

	value_list = dict.values()
	value_list = list(value_list) #makes a full list of values

	key_list = dict.keys()
	key_list = list(key_list) #makes a full list of keys

	max_value = max(value_list) #finding the max value of the value_list
	max_index = value_list.index(max_value) #indicting the index of the largest value

	largest_letter = ord(key_list[max_index]) #using the index of the largest value to find the index of the key

	shift = largest_letter - e_num #finding the shift number by subtracted the largest letter by e
	return shift


def decrypt(str):
	my_dict = build_dictionary(str) #building the dictionary
	my_shift = find_shift(my_dict) #finding the shift

	final_list = []
	my_list = list(str)

	for elem in my_list:
		if elem in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
		't', 'u', 'v', 'w', 'x', 'y', 'z']:
			new_num = ord(elem) - my_shift
			if new_num < ord('a'):
				new_num += 26 #if the element is smaller than 'a', adds 26 to have it wrap back to the end of the alphabet
			new_char = chr(new_num)
			final_list.append(new_char)
		else:
			final_list.append(elem)
			continue

	new_str = "".join(final_list)
	myfile = write_file(new_str, 'decrypted.txt')
	return new_str

print()
text_input = input("Enter the text file you'd like to encrypt: ")
shift_input = int(input("Enter the number you'd like to shift the number by: "))

text_file = read_file(text_input)
encrypt(text_file, shift_input)
find_shift(build_dictionary(read_file('encrypted.txt')))
decrypt(read_file('encrypted.txt')) #reading into the encrypted file
