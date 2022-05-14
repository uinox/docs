#切片
players = ['charles','martina','michael','floerence','eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])
print("***********")
# 遍历切片

players1 = ['charless','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players1[:3]:
    print(player.title())

# 复制切片
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("******************")

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)



# 直接赋值
my_foods1 = ['pizza','falafel','carrot','carrot cake']
friend_foods1 = my_foods1
my_foods1.append("cannoli")
friend_foods1.append("ice cream")

print("My favorite foods are:")
print(my_foods1)
print("\nMy friend's favorite foods are:")
print(friend_foods1)