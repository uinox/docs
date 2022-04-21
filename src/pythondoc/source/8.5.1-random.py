import random

for i in range(5):
    print('%4.3f' % random.random(),end='\n')

print('---')

list=[]

for i in range(10):
    list.append('%4.3f' % random.random())

print(list)