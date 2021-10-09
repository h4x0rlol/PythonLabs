def isPerfect(n):
    s = 1
    k = 2

    while(k * k <= n):
        if n % k == 0:
            s += k
            m = n // k
            if m != k:
                s += m
        k += 1        
    return s == n

n = int(input("Enter number: "))

if isPerfect(n):
   print("perfect")
else:
   print("not perfect")