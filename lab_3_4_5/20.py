a, b = map(int, input().split())
numbers1 = [a, b, 0]
numbers2 = [a, b, 0]
minNum, maxNum = min(numbers1[:2]), max(numbers1[:2])

while numbers1[1] != numbers1[0]:
    numbers1[0] = minNum
    numbers1[1] = maxNum - minNum
    numbers1[2] += 1

    minNum = min(numbers1[:2])
    maxNum = max(numbers1[:2])

minNum, maxNum = min(numbers2[:2]), max(numbers2[:2])
print()
while numbers2[1] != 0:
    numbers2[0] = minNum
    numbers2[1] = maxNum % minNum
    numbers2[2] += 1

    minNum = min(numbers2[:2])
    maxNum = max(numbers2[:2])

print('НОД({0},{1}) = {2}\nпервый алгоритм: {3}\nвторой алгоритм: {4}'.format(
    a, b, numbers1[0], numbers1[2], numbers2[2]))
