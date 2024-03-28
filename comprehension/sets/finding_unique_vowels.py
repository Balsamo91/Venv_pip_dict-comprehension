#  before
# sentence = "look at those flying geese!"

# vowels = set()
# for char in sentence:
#     if char in "aeiouAIEOU":
#         vowels.add(char)
# print(vowels)

# After

sentence = "look at those flying geese and COWs!"
vowels = {char for char in sentence if char in "aeiouAIEOU"}
print(vowels)
