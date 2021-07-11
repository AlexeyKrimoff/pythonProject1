#from sys import argv

#first = int(input('Enter work hours  - '))
#second = int(input('Salary per hour  - '))
#third = int(input('Extra salary  - '))
#first, second, third = argv
#argv = 'Enter work hours, salary per hour, extra salary '
#print("Этот скрипт называется: ", script)
#print("Work hours: ", first)
#print("sal_hours: ", second)
#print("extra_sal: ", third)

#sal = (first * second) + third
#print(f' Your salary is ', sal, 'per month')

from sys import argv
first_param = int(input('Enter work hours  - '))
second_param = int(input('Salary per hour  - '))
third_param = int(input('Extra salary  - '))

#first_param, second_param, third_param = argv
def salary(first_param, second_param, third_param):
    sal = first_param * second_param + third_param
    print(sal)

print('Param_1', first_param)
print('Param_2', second_param)
print('Param_3', third_param)
#def salary(first_param, second_param, third_param):
#    sal = first_param * second_param + third_param
#print(salary())
