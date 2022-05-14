# 列表
list = ['trek','cannondale','redline','soecuakuzed',{'aa':'dd'}]
print(list)
print(list[1],list[3])
print(list[-1], list[-2])
message = "My first list was a " + list[0].title() + "."
print(message)

# 增删改 append insert del pop remove sort
print("*********************")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles1 = ['honda','yamaha','suzuki']
motorcycles1.append('ducati')
print('motorcycles1', motorcycles1)

motorcycles2 = ['honda','yamaha','suzuki']
motorcycles2.insert(0, 'ducati1')
print('motorcycles2', motorcycles2)

del motorcycles2[1]
print('motorcycles2', motorcycles2)

popList = ['honda','yamaha','suzuki','other']
popList.pop()
print('popList',popList)
popList.pop(0)
print('popList',popList)

removeList = ['list1','list2','list3','list4','list5']
removeList.remove('list1')
print('removeList',removeList)

sortList = ['list1','list2','list5','list3','list3','list10']
sortList.sort()
print("ssortList",sortList)
# sort倒序 reverse=True
sortList.sort(reverse=True)
print("sortList",sortList)
# sorted 对列表临时排序
sortedList = ['toyota','subaru','bmw','audi']
print('sortedList', sorted(sortedList))
print('sortedList', sortedList)

# 反转 reverse()
reverseList = ['bmw','audi','toyota','subaru']
reverseList.reverse()
print('reverseList',reverseList)
#len() 长度
print(len(reverseList))