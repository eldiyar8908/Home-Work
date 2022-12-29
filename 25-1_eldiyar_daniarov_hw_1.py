class Person:
    def __init__(self, fullname, age: int, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f"fullname - {self.fullname}, age - {self.age}, is_married - {self.is_married}"


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        Person.__init__(self, fullname, age, is_married)
        self.marks = marks

    def arif(self):
        return f'{round(sum(self.marks.values()) / len(self.marks), 1)}'


class Teacher(Person):
    salary = 10000
    def __init__(self, fullname, age, is_married, experience):
        Person.__init__(self, fullname, age, is_married)
        self.experiance = experience


    def zar(self):
        if self.experiance>3:
            a = round((self.experiance-3) * self.salary / 100 * 5, 1)
            return self.salary + a

nik = Teacher('nikolay', 34, 'yes', 4)
print(nik.introduce_myself())
print(nik.zar())
def create_students():
    student1 = Student('daniyar', 14, 'no', {'kyrg':5, 'phy':3, 'alg': 2})
    student2 = Student('emir', 14, 'no', {'kyrg': 3, 'phy': 5, 'alg': 5})
    student3 = Student('alex', 14, 'no', {'kyrg': 4, 'phy': 2, 'alg': 5})
    n = [student1, student2, student3]
    return n
for i in create_students():
    print(i.introduce_myself())
    print(i.marks)
    print(i.arif())
    sdf = 2