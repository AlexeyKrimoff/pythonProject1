list1 = input("Enter five words thru the _ ")

my_list = list1.split()

for ind, el in enumerate(my_list,1):
    print(ind,el)