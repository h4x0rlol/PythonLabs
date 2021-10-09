min = None
max = None

while True:
   m = int(input('Enter number: '))

   if m == 0:
       break

   if min is None or m < min:
       min = m

   if max is None or m > max:
       max = m

print(min, max)