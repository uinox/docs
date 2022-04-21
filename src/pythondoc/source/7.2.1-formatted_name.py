# 简单返回值
def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

# 参数变可选
print("-------------")
def get_formatted_name(first_name,middle_name,last_name):
    """不可选参数"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

def get_formatted_name(first_name,last_name,middle_name=''):
    """可选参数"""
    full_name = first_name + ' '+ middle_name + ' '+ last_name
    return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)