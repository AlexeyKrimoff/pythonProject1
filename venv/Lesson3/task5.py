
def sum_num():
    summa = 0
    while True:
        in_list = input('Enter digits thrue  spaces or "A" - ').split()
        for num in in_list:
           if num == 'a':
               return summa
           else:
               try:
                   summa += int(num)
               except ValueError:
                   print('Чтобы выйти из программы нажмите a - ')
        print(f'Сумма чисел = {summa}')


