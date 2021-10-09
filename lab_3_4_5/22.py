s = 0
c = 1

while True:
    a = int (input ("Enter number: "))
    s += a
    if (a != 0): c *= a
    if a == 0:
        print ("summ: ", s)
        print ("composition: ", c)
        break