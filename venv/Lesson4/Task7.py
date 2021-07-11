from math import factorial as fact

n = 5
facto = 1
if (n%1==0 and n>=0):
    #def generator(n):
    #    for el in fact(n):
    #         yield el
    #    if n > 10:
    #        break
    for i in range(1, n + 1):
        fact = i * fact
else:
    print('Невозможно вычислить факториал нецелого и/или отрицательного числа!')
g = generator(n)

for el in g:
    print(el)
    n += 1

