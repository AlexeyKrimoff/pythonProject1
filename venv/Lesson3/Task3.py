
#def my_func():
 #   arg_1 = int(input('Enter arg_1 -  '))
#    arg_2 = int(input('Enter arg_2 -  '))
 #   arg_3 = int(input('Enter arg_3 -  '))

#   summa = max(arg1, arg2, arg_3) + max(min(arg_1, arg_2), min(arg_1, arg_3), min(arg_3, arg_2))
 #   return summa

#print(summa)

def summa(a,b,c):

    return a + b + c -(min(a,b,c))

print(f'Summ of two biggest numbers -  ', summa(10, 20, 30))