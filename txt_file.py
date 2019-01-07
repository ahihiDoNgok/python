'''#reading to file
temp_file = open("practice.txt", "r")
for line in temp_file:
    print(line)
temp_file.close()'''

'''#writing to a file - will have no output here, but it creates it for me in my folder on my desktop
file1 = open("file2.txt", "w")
print("I'm writing to a file", file = file1)
print("yay, files are cool ig", file = file1)
file1.close()'''

#read form one file and write to another one
input_file = open("practice.txt", "r")
output_file = open("file2.txt", "w")

for line in input_file:
    new_str = ""
    line = line.strip()
    for char in line:
        new_str = char + new_str
    print(new_str, file = output_file)

input_file.close()
output_file.close()
