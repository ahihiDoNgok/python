user_str = input("Write a word: ")


for char in user_str: #will print out each letter
    print(char)

print()

for idx in range(0,len(user_str)): #len() since we dont know the length
    print(user_str[idx])

print()

idx = 0

while idx < len(user_str):
    print(user_str[idx])
    idx += 1
