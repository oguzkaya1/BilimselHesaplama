a1, b1, c1 = 1, 2, 1
a2, b2, c2 = 3, 4, -2

A = [[a1, b1, c1], [a2, b2, c2]]

y, s = 0, 0
for x in range(1, -1, -1):
  if (s>=3):
    y = 1
  for i in range (2, -1, -1):
      A[x][i] = -A[x][y]*A[y][i]/A[y][y]+A[x][i]
      s += 1
    
print(A[0][2]/A[0][0], A[1][2]/A[1][1])
