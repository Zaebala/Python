
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

max1 = (a > b) * a + (b > a) * b
print(int(max1))