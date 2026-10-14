people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]

sorted_people = sorted(people, key=lambda x: x[1])  # СОРТИРОВКА ПО ЧИСЛУ
print(sorted_people)