
def my_div():
    poz_1 = int(input('Enter first digit  -  '))
    poz_2 = int(input('Enter second digit  -  '))
    if  poz_2 == 0:
        print('Zero division alert!!!')
    else:
        rezult = poz_1 / poz_2
        return rezult
print(f'Rezult = ',(my_div()))

