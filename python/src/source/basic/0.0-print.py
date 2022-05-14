# print
print(2022)
print(98.5)
print('hello world!')
print(3+1)

# print to file
# a+ 如果文件不存在就创建，存在就在文件内容后面追加
fp=open('/Users/zsy/Desktop/data/python/learn/base/text.txt','a+')
print('helloworld',file=fp)
fp.close()

# 不进行换行输出
print('hello','world','python')
