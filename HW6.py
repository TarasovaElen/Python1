# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
# x = int(input('Введите первый элемент a[0] : '))
# d = int(input('Введите шаг d: ')) 
# n = int(input('введите общее колличество элементов  n: '))
# print(*range(x, x + d * n, d))




# Задача 32: Определить элемент s массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 1
# 19
# Вывод: [1, 9, 13, 14, 19]

# list1 = [int(input("введите элементы массива ")) for i in range(int(input('введите сколько элементов в массиве: ')))]
# maxVal = int(input('Введите максимальный эленент: '))
# minVal = int(input('Введите минимальный эленент: '))
# list2 = [i for i in list1 if minVal-1 <i < maxVal+1]
# print(list2)


