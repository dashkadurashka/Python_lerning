# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random

N = int(input("Введите желаемое количество элементов массива: "))
X = int(input("Ближайшее к какому числу ищем? "))

list_user = []
for i in range(N):
    list_user.append(random.randint(1, 10))
print(list_user)

dev = abs(X - list_user[0])

number = list_user[0]
for i in range(1, len(list_user)):
    if dev > abs(list_user[i] - X):
        dev = abs(list_user[i] - X)
        number = list_user[i]
print(number)