def get_formatted_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    f_name = input("First_name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name,l_name)
    print("\nHello, " + formatted_name + "!")