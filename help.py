# работа с файлами
# w - write (перезапись)
# a - add (добавить)
# x - satefy (безопасный режим)
# r - read (чтение)

# new = open('file.txt','w', encoding='UTF-8')
# new.write('Бишкек,Кыргызстан')
# new.close()

# with open('new.txt', 'w') as file:
#     file.write('new file')

# with open('file.txt', 'x') as file:
#     file.write('\nadded info')

# with open('file.txt', 'r') as file:
#     print(file.)
    # print(file.readline())
    # print(file.readline())
    # file.seek(0)
    # print(file.readlines()[-1])
    # print(file.read().split('\n')[-0])


class Car:
    def __init__(self, model, year):
        self.__model = model
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__year = value

car = Car('m5', 1990)
car.model('m4')
print(car.model())