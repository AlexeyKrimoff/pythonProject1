
list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
for i in range(1, len(list_1)):
    a, b = list_1[i - 1], list_1[i]

    if a < b:
     new_list.append(b)
print(new_list)
