day = int(input('Введите число: '))
month = int(input('Введите номер месяца: '))
if (31 >= day >= 21  and 3 == month) or (1 <= day <= 20 and month == 4):
    print('Овен')
elif (30 >= day >= 21 and 4 == month) or (1 <= day <= 21 and month == 5):
    print('Телец')
elif (31 >= day >= 22 and 5 == month) or (1 <= day <= 21 and month == 6):
    print('Близнецы')
elif (30 >= day >= 22 and 6 == month) or (1 <= day <= 22 and month == 7):
    print('Рак')
elif (31 >= day >= 23 and 7 == month) or (1 <= day <= 21 and month == 8):
    print('Лев')
elif (31 >= day >= 22 and 8 == month) or (1 <= day <= 23 and month == 9):
    print('Дева')
elif (30 >= day >= 24 and 9 == month) or (1 <= day <= 23 and month == 10):
    print('Весы')
elif (31 >= day >= 24 and 10 == month) or (1 <= day <= 22 and month == 11):
    print('Скорпион')
elif (30 >= day >= 23 and 11 == month) or (1 <= day <= 22 and month == 12):
    print('Стрелец')
elif (31 >= day >= 23 and 12 == month) or (1 <= day <= 20 and month == 1):
    print('Козерог')
elif (31 >= day >= 21 and 1 == month) or (1 <= day <= 19 and month == 2):
    print('Водолей')
elif (28 >= day >= 20 and 2 == month) or (1 <= day <= 20 and month == 3):
    print('Рыбы')
else:
    print('Ошибка!')