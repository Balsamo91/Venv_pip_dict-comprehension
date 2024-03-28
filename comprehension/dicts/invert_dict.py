# Before

# original_dict = {'a' : 1, 'b' : 2, 'c' : 3}
# inverted_dict = {}

# print(original_dict)
# for key, value in original_dict.items():
#     inverted_dict[value] = key
# print(inverted_dict)



# After

original_dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd': 4}
print(original_dict)
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)
