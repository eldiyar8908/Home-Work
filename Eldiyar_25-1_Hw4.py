data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
data_list = list[data_tuple]
letters = []
numbers = []
for i in data_tuple:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)
letters.append(numbers.pop(1))
numbers.pop(0)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = 'G'
letters[-2] = 'c'
for i in range(len(numbers)):
    numbers[i] **= 2
letters_kor = tuple(letters)
numbers_kor = tuple(numbers)
print(letters_kor)
print(numbers_kor)