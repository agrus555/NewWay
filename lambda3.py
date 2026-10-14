t_list = range(1, 21)

filtered_list = filter(lambda x: x % 3 == 0, t_list)
print(list(filtered_list))