# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married
#     def introduce_myself(self):
#         print(f'fullname: {self.fullname}, age: {self.fullname}, married: {self.is_married}')
#
#
#
# class Student(Person):
#     def __init__(self, fullname, age, is_married, marks):
#         self.marks = marks
#         def arif():
#             print(f'{round(sum(self.marks.value)/len(marks))}')

from decouple import config
print(config('hello'))



