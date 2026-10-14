def average(numbers: list) -> float:
    return sum(numbers) / len(numbers)

num = []

try:
    print(average(numbers=[1, 2, 3, 4, 5]))
    print(average(numbers=num))

except ZeroDivisionError:
    print("list is empty")
