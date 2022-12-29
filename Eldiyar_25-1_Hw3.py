all_glass = 'eyuioaAYUIOEуеыаоэяиюУЕЫАОЭЯИЮ'
while True:
    glas = 0
    sogl = 0
    kol = 0
    word = input('Cлово: ')
    if word == 'Exit':
        print('Программа остановлена.')
        break
    else:
        for i in word:
            if i.isalpha():
                kol += 1
                if i in all_glass:
                    glas += 1
                else:
                    sogl += 1
    print('Количество букв', kol)
    print('Согласных букв', sogl)
    print('Гласных букв', glas)
    print(f'Гласные/Согласные: {round((glas * 100) / kol, 2)}% / {round((sogl * 100) / kol, 2)}%')


