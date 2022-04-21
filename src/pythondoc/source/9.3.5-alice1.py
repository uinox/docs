filename='alice.txt'

try:
    with open(filename) as f_obj:
        contens=f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exits"
    print(msg)