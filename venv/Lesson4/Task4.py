from random import random

list_inp = [1, 1, 6, 32, 54, 0, 3, 3, 7, 7, 7, 9, 17, 6, 9, 9, 76, 0, 76, 5, 5, 5]

new_list = []
for i in list_inp:
    if list_inp.count(i) == 1:
        new_list.append(i)
print(new_list)

