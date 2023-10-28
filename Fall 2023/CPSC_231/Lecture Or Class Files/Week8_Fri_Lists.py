#List 1:
my_list = [1,2,3,4,5,6]
sliced_list = my_list[3:]

print(sliced_list)
#Dump: [4, 5, 6]

#List 2: 
my_list = [10,20,30,40]
sliced_list = [i*2 for i in my_list]

print(sliced_list)
#Dump: [20, 40, 60, 80]

#List 3: 

list1 = [10,20,30,40]
print(list1)
#Dump: [10, 20, 30, 40]

list2 = [i + 1 for i in list1]
print(list2)
#Dump: [11, 21, 31, 41]

#List 4: 

list1 = [10,20,30,40]
list2 = [i / 2 for i in list1 if i > 10]
print(list2)
#Dump: [10.0, 15.0, 20.0]

