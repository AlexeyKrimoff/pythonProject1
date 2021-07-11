from functools import reduce

list_unk = []
for i in range(100, 1001, 2):
    list_unk.append(i)
print(list_unk)

sum_all = reduce(lambda x,y: x + y, list_unk)
print(f'Summ of all elements of the list  -  ', sum_all)