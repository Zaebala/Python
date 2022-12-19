import json

data = {
	'testlog':'testpas'
}
with open ('log.json', 'w') as f:
	json.dump(data,f)

secret = 'GG не будет'
with open ('secret.json', 'w', encoding = 'utf-8') as f:
	json.dump(secret,f)

while True:	
	def reg():
		with open ('log.json', 'r') as f:
			data = json.load(f)
		login = input("Введите логин: ")
		password = input("Введите пароль: ")
		if login not in data.keys():
			data[login] = password
			with open ('log.json', 'w') as f:
				json.dump(data,f)
			print("Успешная регистрация!")
		else:
			print("Логин уже занят")
			
	def log():
		login = input("Введите логин: ")
		password = input("Введите пароль: ")
		with open ('log.json', 'r') as f:
			data = json.load(f)
		if data[login] == password:
			print ("Успешный вход")
			with open ('secret.json', 'r') as f:
				secret = json.load(f)
			print(secret)
		else:
			print('Неверный логин или пароль')

	q1 = input("Вход или регистрация?")
	if q1 == "вход":
		log()
	elif q1 == "регистрация":
		reg()
	elif q1 == "выход":
		break