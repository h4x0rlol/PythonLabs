a = int(input('1: '))
b = int(input('2: '))

res = 0
z = 0

while z != (abs(b)):
    res = res+(abs(a))
    z = z+1

if (a or b) < 0:
    res = -res

print(res)
