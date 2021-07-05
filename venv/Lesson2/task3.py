
dict_month = {1 :'january', 2 : 'february', 3 : 'march', 4 : 'april',
5 : 'may', 6 : 'june', 7 : 'july', 8 : 'august', 9 : 'september', 10 : 'october', 11 : 'november', 12 : 'december'}


digit = int(input('Enter digit 1 - 12 >  '))
x = digit

if  dict_month.keys() == digit:
    print(dict_month.get(key))

else:
     print(dict_month.get(x))



