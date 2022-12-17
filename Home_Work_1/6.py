
condition = True

i = 0

while condition:
    pas = input('Введите пароль: ')
    if len(pas) >= 8:
        
        for letter in pas:
          
          if letter == letter.capitalize():
            i += 1
    else:
        print("Простой пароль")
        
    if i > 0:
        condition = False
        print('Пароль подтвержден!')