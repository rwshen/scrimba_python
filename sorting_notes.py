# sort() doesn't create a new list
# sorted() creates a new list

my_list = [1,5,3,7,2]
my_dict = {'car':4,'dog':2,'add':3,'bee':1}
my_tuple = ('d','c','e','a','b')
my_string = 'python'
print(my_list,'original')
my_list_1 = sorted(my_list)
my_sorted_tuple = sorted(my_tuple)
print(my_list_1,'new')
print(my_sorted_tuple)
print(my_dict,'original')
print(sorted(my_dict.values(), reverse=True))
print(my_dict,'new')
# reverses
print(my_list_1[::-1])

# list of lists
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
# sort on the second index
print(sorted(my_llist, key = lambda item :item[1]))
print(sorted(my_llist, key = lambda item :item[2]))

