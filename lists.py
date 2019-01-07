#list examples

s_list = [['Name', 'Age', 'GPA'], ['Bill', 25, 3.55], ['Rich', 26, 4.00]]

b_info = s_list[1] #row
print(b_info)

b_gpa = b_info[2] #column
print(b_gpa)

b_gpa1 = s_list[1][2] #going into index 1 and from there going into that list's index 2 
print(b_gpa1)
