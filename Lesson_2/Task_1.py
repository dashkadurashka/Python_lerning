# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

from random import randint


coins = []
n = int(input("Введите число: "))
for i in range(n):
    coins.append(randint(0, 1))

print(coins)

zero = 0
one = 0

for el in coins:
    if el == 0:
        zero += 1
    else:
        one += 1

if zero > one:
    print(one)
else:
    print(zero)

