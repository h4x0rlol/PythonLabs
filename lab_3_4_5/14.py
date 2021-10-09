n = input()
k = False
for i in range(len(n) - 1):
    if n[i] == n[i+1]:
        k = True
print(k)
