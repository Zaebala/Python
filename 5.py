
x1 = int(input("X1: "))
y1 = int(input("Y1: "))
x2 = int(input("X2: "))
y2 = int(input("Y2: "))

if x1 > 8 or x1 < 1 or y1 > 8 or y1 < 1 or x2 > 8 or x2 < 1 or y2 > 8 or y2 < 1:
	print("Неверные координаты!\nКоординаты могут быть только от 1 до 8!")
else:
	if x1 == x2 or y1 == y2:
		print("Yes")
	else:
		print("No")