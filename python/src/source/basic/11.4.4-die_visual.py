from die import Die
die=Die()
results=[]
for roll_num in range(1000):
    result=die.roll()
    results.append(result)
# 分析结果
frequencies=[]
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)