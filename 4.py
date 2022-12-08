num1 = input("Число 1: ")
num2 = input("Число 2: ")
num3 = input("Число 3: ")

value = (num1 == num2) + (num1 == num3) + (num2 == num3)

if value == 3:
	print("3")
elif value == 1:
	print("2")
else:
	print("0")