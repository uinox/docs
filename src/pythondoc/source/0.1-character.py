# 转义字符 \n 换行 \t 一个制表符(4位) \r 覆盖 \b 退一个格
print('hello\nworld')
print('hello\tworld')
print('helloooo\tworld')
print('hello\rworld')
print('hello\bworld')

print('http:\\\\www.baidu.com')
print('\'hello\'')
print('\"helloworld\"')

# 原字符 不希望字符串中转义字符起作用，或使用原自负，就是在字符串前加上r或R
# 注意事项，最后一个字符不能是反斜杠 \
print(r'hello\nworld')