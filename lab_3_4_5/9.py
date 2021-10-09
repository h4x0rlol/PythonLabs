n = int(input())

l = [number for number in range(n) if all((c != 0) and (
    number % c == 0) for c in map(int, str(number)))]
print(l)
