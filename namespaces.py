import random
from random import choice

print(f"методы в модуле random;\n{dir(random)})")

my_list = [1, 2, 3]

print(choice(my_list), "\n")
print(choice(my_list), "\n")
print(choice(my_list), "\n")

for key, value in list(globals().items()):
    print(f"{key}: | {value} |")
