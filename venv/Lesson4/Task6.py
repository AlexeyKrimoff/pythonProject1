from itertools import count, cycle

#list_1 = []
#for i in range(2, 11,1):
#    list_1.append(i)
#print(list_1)

s = 0
for el in cycle('Fedor'):
    if s > 10:
        break
    print(el)
    s += 1