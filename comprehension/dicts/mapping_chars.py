#  Before

# char_to_ascii = {}
# for char in "Hello world":
#     char_to_ascii[char] = ord(char)
# print(char_to_ascii)

# After
char_to_ascii = {char: ord(char) for char in "hello world!"}
print(char_to_ascii)

