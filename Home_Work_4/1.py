from random import randint

a = []
for i in range(10):
	a.append(randint(1,99))
a.sort()
print(a)

value = int(input("Введите искомое число: "))

low = 0
high = len(a) - 1
mid = (low + high) // 2

while value != a[mid] and low <= high:
	if value < a[mid]:
		high = mid - 1

	else:
		low = mid + 1

	mid = (low + high) // 2
	
if value == a[mid]:
	id = mid + 1
	print('ID: ', id)
else:
	print("Такого значения нет")