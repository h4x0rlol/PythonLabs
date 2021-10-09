count = 0
for i in range(13):
  for j in range(11):
    for k in range(9):
      if 185 == i*15 + j*17 + k*21:
        count += 1
        print(i,j,k)
print("total ways -", count)