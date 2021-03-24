d = {'Hello' : 'Hi', 'Bye' : 'Goodbye', 'List' : 'Array'}
k = input("введите значение для поиска ключа: ")
for name, znach in d.items():
    if znach == k:
        print(name)
