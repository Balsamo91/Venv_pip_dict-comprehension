#  Before
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = []
# print(numbers)
# for x in numbers:
#     squares.append(x**2)

# print(squares)

#  After

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers]
print(squares)