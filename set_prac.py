def uni_char(str):
    my_str = str.lower()
    my_set = set(my_str)
    my_list = list(my_set)
    return my_list


print(uni_char('there'))
