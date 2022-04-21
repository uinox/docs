filename='pi_million_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()
pi_string=''
for line in lines:
    pi_string+=line.rstrip()
brithday=input("Enter you birthday,in the from mmddyy:")
if brithday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")