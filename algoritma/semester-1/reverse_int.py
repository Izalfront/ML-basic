data = [2,1,4,5,3,0]

reversed_data = data[::-1]
print(reversed_data)

data2 = [2,1,4,5,3,0,1,0]
data2 = [x for x in data2 if x != 0]
data2.reverse()
print(data2)   