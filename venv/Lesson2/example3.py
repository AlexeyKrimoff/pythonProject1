#methods

text = 'Hello Python'
print(text.lower()) # Все заглавные
print(text.upper()) #Все строчные
print(text.isdigit()) # Проверяет число или нет
print(text.replace('l','uu')) # заменяет одно на другое
print(text.count('l')) # считает количество
print(text.find('l')) #находит первый объект

num = input('Введите число - ')
if num.isdigit():
    num = int(num)
else:
    print("Это не число")