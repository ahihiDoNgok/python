#prints every other libe of one file to another file

def other_line(input_file, output_file):
    line_num = 1
    for line in input_file:
        line = line.strip()
        if line_num % 2 ==1:
            print(line, file = output_file)
        line_num += 1
    #no return statement since output is going to a file

input_file = input("What file would you like to read: ")

try:
    f1 = open('file1.txt', 'r')
    f2 = open('file3.txt', 'w')
    other_line(f1, f2)
    f1.close()
    f2.close()
except FileNotFoundError:
    print("Invalid file name")
