import csv
filename='sitka_weather_07_2014.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    # enumerate() -->获取每个元素的索引及其值
    for index,column_header in enumerate(header_row):
        print(index,column_header)
