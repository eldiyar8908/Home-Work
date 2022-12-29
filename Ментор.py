'''1'''
# def area(x1, y1, x2, y2, x3, y3):
#     area1 = abs((x2 - x1) * (y3 - y1)-(x3 - x1) * (y2 - y1))
#     S = round(area1 / 2)
#     with open('area.txt', 'a', encoding='utf-8') as file:
#         file.write(f'Площадь треугольника: {S}см \n')
#     ab = (x2 - x1)**2 + (y2 - y1)**2
#     bc = (x3 - x2) ** 2 + (y3 - y2) ** 2
#     ac = (x3 - x1) ** 2 + (y3 - y1) ** 2
#     if ab < bc and ac < bc:
#         if ab + ac == bc:
#             with open('TrueFalse.txt', 'a', encoding='utf-8') as file:
#                 file.write('True\n')
#         else:
#             with open('TrueFalse.txt', 'a', encoding='utf-8') as file:
#                 file.write('False\n')
#     elif bc < ab and ac < ab:
#         if bc + ac == ab:
#             with open('TrueFalse.txt', 'a', encoding='utf-8') as file:
#                 file.write('True\n')
#         else:
#             with open('TrueFalse.txt', 'a', encoding='utf-8') as file:
#                 file.write('False\n')
#     else:
#         if ab + bc == ac:
#             with open('TrueFalse.txt', 'a', encoding='utf-8') as file:
#                 file.write('True\n')
#         else:
#             with open('TrueFalse.txt', 'a', encoding='utf-8') as file:
#                 file.write('False\n')
# print(area(-3, -2, 0, -1, -2, 5))





'''2'''
# user = input().split()
# user_input = user
# b = 0
# try:
#     for i in user_input:
#         сount_words = user_input.count(i)
#         if сount_words > b:
#             b = сount_words
#             all_words = i
#     print(all_words)
# except NameError:
#     print('Введите хотя бы 1 слово')



# '''3'''
count = int(input('Введите кол-во моментов: '))
aaa = 0
time = []
while aaa != count:
    hour = input('Введите час момента: ').split()
    time.append(hour)
    aaa += 1

time1 = []
for i in time:
    a = int(i[0]) * 60 + int(i[1])
    b = a * 60 + int(i[2])
    time1.append(b)
time2 = sorted(time1)


time_finisf = []
a = []
for i in time2:
    seconds = i % 60
    minutes = i // 60
    hours = minutes // 60
    minutes1 = minutes % 60
    a.append(hours)
    a.append(minutes1)
    a.append(seconds)
    time_finisf.append(a)
    a = []
print(time_finisf)



