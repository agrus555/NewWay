set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
numbers = [1, 2, 2, 2, 2, 3, 3, 3, 6, 4, 5, 6, 5, 5, 7, 8, 12, 543, 7, 9, 10, 1]
unique_numbers = set(numbers)

un_set = set1.union(set2)  # совмещение
print(un_set)
un_set = set1.difference(set2)  # показывает каких элементов нету в set2
print(un_set)
un_set = set1.intersection(set2)  # проверка на одинаковые числв
print(un_set)
