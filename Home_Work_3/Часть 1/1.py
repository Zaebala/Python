
x = int(input("Вклад в банке: "))
y = int(input("Скока будет: "))
p = int(input("Проценты: "))
z = 0

while x < y:
	x += int((x / 100) * p)
	z += 1
if x >= y:
	print("Через", z, "лет")