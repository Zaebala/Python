
from random import randint

n = 5
m = [[randint(0,100) for i in range(n)] for j in range (n)]
max1 = []
print(m)
for i in m:
	max1.append(max(i))
print(max(max1))