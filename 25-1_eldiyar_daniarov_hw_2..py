class Figure:
    izmer = 'cm'
    def __init__(self):
        pass


    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        Figure.__init__(self)
        self.__radius = radius
        self.__area = self.calculate_area()

    def calculate_area(self):
        return round(3.14 * self.__radius**2)

    def info(self):
        return f'Circle radius: {self.__radius}{self.izmer}, area: {self.__area}{self.izmer}'


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b
        self.__area = self.calculate_area()


    def calculate_area(self):
        return round(self.__side_a * self.__side_b//2)


    def info(self):
        return f'RightTriangle side a: {self.__side_a}{self.izmer}, side_b: {self.__side_b}{self.izmer},' \
               f' area: {self.__area}{self.izmer}'

some_figure = [Circle(3), Circle(10), RightTriangle(2,5), RightTriangle(4,1), RightTriangle(5,9)]
for i in some_figure:
    print(i.info())