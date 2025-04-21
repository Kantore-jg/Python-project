with open("file1.txt") as data1:
    data_1 = data1.readlines()

with open("file2.txt") as data2:
    data_2 = data2.readlines()


result = [int(n) for n in data_1 if n in data_2 ]

print(result)