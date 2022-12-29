class Figure:
    izmer = 'cm'
    def __init__(self, perimeter = 0):
        self.__perimeter = perimeter


    def get_perimeter(self):
        return self.__perimeter

    def set_perimeter(self, value):
        self.__perimeter = value

    def calculate_area(self, value):
        pass

    def calculate_perimeter(self,value):
        pass

    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length, perimeter = 0):
        Figure.__init__(self, perimeter)
        self.__side_length = side_length

        def calculate_perimeter(self, side_length):
            self.__perimeter = side_length*4

    def calculate_area(self, value):
        return value**2

    def calculate_perimeter(self, side_length):
        self.__perimeter = side_length * 4

    def info(self):
        return f'Square side length: {self.__side_length}{self.izmer}' \
               f', perimeter: {self.__side_length.calculate_perimeter}{self.izmer}, area: {self.__side_length.calculate_area}{self.izmer}'


class Rectangle(Figure):
    def __init__(self, length, width, perimeter = 0):
        Figure.__init__(self, perimeter)
        self.__length = length
        self.__width = width

        def calculate_perimeter(self, length, width):
            self.__perimeter = (length + width) * 2

    def calculate_area(self, length, width):
        return length * width

    def calculate_perimeter(self, length, width):
        self.__perimeter = (length + width) * 2

    def info(self):
        return f'Rectangle length: {self.__length}{self.izmer}, wenth: {self.__width}{self.izmer},' \
               f' perimeter: {self.__perimeter}{self.izmer}, area: {self.calculate_area}{self.izmer}'

some_figure = Square(2)
print(some_figure.info())


