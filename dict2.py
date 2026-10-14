names = ["Анна", "Иван", "Анна", "Олег", "Иван", "Анна"]
dictt = dict()
for i in names:
    if dictt.get(i) == None:
        dictt[i] = 1
    else:
        dictt[i] = dictt[i] + 1
print(dictt)
