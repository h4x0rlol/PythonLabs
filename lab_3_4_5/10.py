for i in range(100, 1000):
    sum = 0
    for s in range(0, 3):
        i = str(i)
        sum = sum + int(i[s]) ** 3
        i = int(i)
    if sum == i:
        print(i)

for i in range(1000, 10000):
    sum = 0
    for s in range(0, 4):
        i = str(i)
        sum = sum + int(i[s]) ** 4
        i = int(i)
    if sum == i:
        print(i)
