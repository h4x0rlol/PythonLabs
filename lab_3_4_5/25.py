a = int(input('Enter number: '))
n = int(input('Enter degree: '))

a1 = a

for k in range (n - 1):
   a *= a1

print (a)