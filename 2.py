
v = int(input("Введите скорость: "))
t = float(input("Введите время: "))

s = v * t
if s >= 109:
	rounds = int(s / 109)
	value = s - rounds * 109
	print ("Вася остановился на:", value, "километре")
else:
	print("Вася остановился на:", s, "километре")