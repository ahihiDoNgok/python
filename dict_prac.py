def word_count(str):
    my_list =str.split()
    count_dict = {}
    for word in my_list:
        if word in count_dict:
            count_dict[word] = count_dict[word] + 1
        else:
            count_dict[word] = 1
    return count_dict

s = 'one fish two fish red fish blue fish'
word_dict = word_count(s)
print(word_dict)
