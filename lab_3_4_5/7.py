from random import random

n = int(input())

first = second = third = foruth = 0

for i in range(0, n):
    k = random()
    if (k >= 0 and k < 0.25):
        first += 1
    elif (k >= 0.25 and k < 0.5):
        second += 1
    elif (k >= 0.5 and k < 0.75):
        third += 1
    elif(k >= 0.75 and k < 1):
        foruth += 1

print(first, second, third, foruth)
