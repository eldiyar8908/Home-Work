day = int(input('Введите число: '))
month = int(input('Введите номер месяца: '))
if (day >= 21 and 3 == month) or (day <= 20 and month == 4):
    print('Овен')
elif (day >= 21 and 4 == month) or (day <= 21 and month == 5):
    print('Телец')
elif (day >= 22 and 5 == month) or (day <= 21 and month == 6):
    print('Близнецы')
elif (day >= 22 and 6 == month) or (day <= 22 and month == 7):
    print('Рак')
elif (day >= 23 and 7 == month) or (day <= 21 and month == 8):
    print('Лев')
elif (day >= 22 and 8 == month) or (day <= 23 and month == 9):
    print('Дева')
elif (day >= 24 and 9 == month) or (day <= 23 and month == 10):
    print('Весы')
elif (day >= 24 and 10 == month) or (day <= 22 and month == 11):
    print('Скорпион')
elif (day >= 23 and 11 == month) or (day <= 22 and month == 12):
    print('Стрелец')
elif (day >= 23 and 12 == month) or (day <= 20 and month == 1):
    print('Козерог')
elif (day >= 21 and 1 == month) or (day <= 19 and month == 2):
    print('Водолей')
elif (day >= 20 and 2 == month) or (day <= 20 and month == 3):
    print('Рыбы')
else:
    print('Ошибка!')