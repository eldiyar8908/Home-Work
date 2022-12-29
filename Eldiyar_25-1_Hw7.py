ten = [i for i in range(1,11)]
evens = list(filter(lambda args: args%2==0, ten))
a = list(map(lambda args: args**2,evens))
print(a)


def ind(a=list(ten)):
    while True:
        user = input("введите индекс: ")
        if user == "exit":
            break
        else:
            try:
                print(a[int(user)])
            except IndexError:
                print('неверно')
            except:
                print('введите коректно!')
print(ind())