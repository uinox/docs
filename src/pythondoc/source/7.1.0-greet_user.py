def greet_user():
    """注释"""
    print("Hello!")
greet_user()

def greet_user(username):
    print("Hello，"+username+"!")
greet_user('jesse')

def describe_pet(animal_type, pet_name):
    """位置实参"""
    print("\nI have a " + animal_type + ".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet('hamster','harry')

def describe_pet(animal_type, pet_name):
    """关键字实参"""
    print("\nI have a " + animal_type + ".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(animal_type='hamster',pet_name='harry')

def describe_pet(pet_name,animal_type='dog'):
    """默认值"""
    print("\nI have a "+ animal_type +".")
    print("My "+animal_type+"'s name is "+pet_name.title()+".")
describe_pet(pet_name='willie')

def describe_pet(pet_name,animal_type='dog'):
    """显示宠物信息"""
    print("\nI have a "+animal_type+".")
    print("My "+animal_type+"'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

# 等效调用
print("-----------------")
describe_pet('willie')
describe_pet(pet_name='willie')
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')