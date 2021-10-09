import math

a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))
d = int(input("Введите 4 число: "))
e = int(input("Введите 5 число: "))
f = int(input("Введите 6 число: "))
g = int(input("Введите 7 число: "))
h = int(input("Введите 8 число: "))
j = int(input("Введите 9 число: "))
k = int(input("Введите 10 число: "))

list = [a, b, c, d, e, f, g, h, j, k]

print('Сумма: ', sum(list))
print('Произведение: ', math.prod(list))
