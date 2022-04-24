magicians = ['alice','david','carolina']
for magician in magicians:
    # print(magician)
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

for magician in magicians:
    print(magician)

# range生成数据
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print('numbers', numbers)

even_numbers = list(range(2,11,2))
print('even_numbers', even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares1 = [value**2 for value in range(1,11)]
print(squares1)

squares2 = [value**3 for value in range(1,11)]
print(squares2)