op = input("+ or * or **: ")
for i in range(1, 10):
    for ii in range(1, 10):
        if op == '+':
            iii = i + ii
        elif op == '*':
            iii = i * ii
        elif op == '**':
            iii = i ** ii
        else:
            print("Invalid input")
        print(f"{i} {op} {ii} = {iii}")
