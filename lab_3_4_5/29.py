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

a = int(input("a: "))
b = int(input("b: "))

for i in range(a,b):
    if isPerfect(i):
        print(i)
