# Файлы
# a - открытие для  добавления данных
# r - чтение
# w - открытие для записи данных
# r+ - создастся если нет
# w+ - ошибка если нет файла

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.close()

# with open("file.txt", "w") as data:
#     data.write('line2 /n')
#     data.write('line3 /n')

# # exit() # не выполнять дальше
# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# with open("file.txt", "w") as data:
#     data.write('line2 /n')
#     data.write()

    
# path = 'file.txt'

# def NewString(symbol, count):
#     return symbol * count

# print(NewString('!'))

# неограниченное число параметров
# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)

# list = []
# for e in range(1, 10):
#     list.append(fib(e))

# print(list)

# # Кортеж - неизменяемый список
# # пример
# a = (3, 4)
# a = (3,)
# print(a[0])
# print(a[1])
# # для кортежей не работает
# a[0] = 12

# a = (3,4,5)
# for item in a:
#     print(item)

# # Словари - неупорядоченные коллекции произвольных элементов с доступом по ключу
# dictionary = {}
# dictionary = \
#     {
#         'up': 'вверх',
#         'down': 'вниз'
#     }
# # print(dictionary)
# # print(dictionary['down'])

# for k in dictionary.keys():
#     print(k)

# Множества (тип данных - Set)
# colors = {'red', 'green', 'blue'}
# colors.add('red') # не добавит так как уже есть
# colors.remove('grey') # удалить, если элемента нет - еррор будет
# colors.discard('grey') # удалить без ошибки
# colors.clear() # очистить

# Списки (list)
# list1 = [1,2,3,4,5]
# list2 = list1 # связанные списки, поменяешь в одном, поменяется и в другом

# for e in list1:
#     print(e)

