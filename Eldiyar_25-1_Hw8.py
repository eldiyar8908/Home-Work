min = 0
max = 100
attempts = 0
chislo = []
print('Загадайте число от 1 до 100')
while True:
    a = (max + min)//2
    print(f'ваше число: {a}')
    chislo.append(a)
    attempts += 1
    user = input('правильно?: ')
    if user == 'да':
        with open('results.txt', 'w', encoding='utf-8') as file:
            file.write(f'количество попыток: {attempts}\n'
                        f'список попыток: {chislo}\n'
                        f'загаданное число: {a}'
                        )
        break
    elif user == 'меньше':
        max = max - (max - a)
    elif user == 'больше':
        min = a
    else:
        print('введите коректно: да/больше/меньше')

