#  Before

# even_square = []
# for x in range(10):
#     if x % 2 == 0:
#         even_square.append(x**2)
# print(even_square)

#  After

even_square = [x**2 for x in range(12) if x % 2 ==0]
print(even_square)

