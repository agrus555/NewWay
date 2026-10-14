
fruits = ["apple", "banana", "cherry", "orange", "strawberry", "grapefruit", "dragonfruit"]
sort_fruits = sorted(fruits)
print("\nSort:")
print(sort_fruits)
rev_sort_fruits = sorted(fruits, reverse=True)
print("\nRevered sort:")
print(rev_sort_fruits)

def sort_by_len(element: str):  # сортировка по длине
    return len(element)

print("\nSort by length:")
len_sort_fruits = sorted(fruits, key=sort_by_len)  # сортировка по ключу
print(len_sort_fruits)


def sort_by_letters(element: str) -> bool:
    return "a" in element  # первыми будут идти слова что имеют букву а

print("\nSort by letters:")
letter_sort_fruits = sorted(fruits, key=sort_by_letters, reverse=True)
print(letter_sort_fruits)


def rev_sort_by_letters(element: str) -> bool:
    return "a" not in element  # первыми будут идти слова что не имеют букву а

print("\nRev sort by letters:")
rev_letter_sort_fruits = sorted(fruits, key=rev_sort_by_letters, reverse=True)
print(rev_letter_sort_fruits)