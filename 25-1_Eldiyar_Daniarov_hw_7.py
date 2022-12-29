def binary_search(value, list1 : list):
    first = 0
    last = len(list1) - 1
    mid = (first + last) // 2
    list2 = sorted(list1)
    while True:
        if value > list2[mid]:
            first = mid + 1
        elif value < list2[mid]:
            last = mid - 1
        elif value == list2[mid]:
            print('Элемент найден!')
            print(f'Индекс: {mid}')
            break
        else:
            print('Элемент не найден!')
            break
        mid = (first + last) // 2

binary_search(12, [33, 44, 12, 55, 1])


def bubble_sort(list1 : list):
    first = 0
    second = 1
    a = len(list1)
    for i in range(a - 1):
        while True:
            if list1[first] > list1[second]:
                list1[first], list1[second] = list1[second], list1[first]
            first += 1
            second += 1
            if second == len(list1):
                break
        second = 1
        first = 0
        a -=1
    return list1

print(bubble_sort([33, 44, 12, 55, 35, 1]))