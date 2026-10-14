#even_squares = []
#for i in range(18):
#    if i % 2 == 0:
#        even_squares.append(i ** 2)

even_squares = [x ** 2 for x in range(18) if x % 2 == 0]

print(even_squares)
