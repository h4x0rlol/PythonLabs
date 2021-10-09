from random import randint

# 1
a = int(input('a: '))
b = int(input('b: '))

while b <= a:
    b = int(input('b must be greater than a, b: '))

print("First")
for i in range(0, 5):
    print(randint(a, b))

# 2
threeDigit = randint(100, 999)
print("Second")
print(threeDigit)
print(sum([int(k) for k in str(threeDigit)]))

# 3
print("Third")
num = str(randint(10, 99))
print(int(num+'0'))

# 4
print("Fourth")
n = randint(0, 100)
t = 10
while t > 0:
    k = int(input("Number: "))
    if k > n:
        print('k > n')
        t -= 1
    elif k < n:
        print('k < n')
        t -= 1
    elif k == n:
        print('you win')
        break
if t <= 0:
    print('random number is %i' % n)
