fruits = ["apple", "banana", "cherry", "orange", "strawberry", "grapefruit", "dragonfruit"]

sorted_fruits = sorted(fruits, key=lambda x: "a" not in x)
print(sorted_fruits)