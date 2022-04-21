# 我们需要将这两个程序合并到一个程序（remember_me.py）中。这个程序运行时，我们将尝试从文件username.json中获取用户名，因此我们首先编写一个尝试恢复用户名的try 代 码块。如果这个文件不存在，我们就在except 代码块中提示用户输入用户名，并将其存储在username.json中，以便程序再次运行时能够获取它：
import json
# 如果以前存在了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename='username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f_obj:
        json.dump(username,f_obj)
        print("We'll remember you when you come back, "+username+"!")
else:
    print("welcome back, "+username+"!")