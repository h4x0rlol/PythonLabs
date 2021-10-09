n = int(input('n: '))
sum = 0

# 1
while (n > 0):
    sum += n
    n -= 1

# 2

for i in range(0, n+1):
    sum += i
