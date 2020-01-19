len('Moha') #4


numbers = [ 1 , 3 , 4 , 2 ]
numbers.sort()


list(map(lambda x: x**2, [2,3])) #[4,9]


list(filter(lambda x: x < 0, [-1,3,-5]))#[-1, -5]


my_list = ['geeks', 'for']
my_list.append('geeks')
my_list.insert(0, 'ssss')


my_dictionary ={'a':1}
my_dictionary['b']=2



find_index_list =['a','b','c']
find_index_list.index('b')


x = my_list.pop()


vec = [2, 4, 6]
[3*x for x in vec] #[6, 12, 18]


dic= {'a':1,'b':2}

for (index,item) in dic.items():
    print(index)
    print (item)