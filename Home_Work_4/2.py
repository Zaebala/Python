from random import randint

a = []

for i in range(10):
	a.append(randint(-20,20))
print(a)

def sorting(a):
	N = len(a)
	for i in range(1, N):
		for j in range(i,0,-1):
			if a[j] < a[j-1]:
				a[j], a[j-1] = a[j-1], a[j]
			else:
				break
	return a
print(sorting(a))