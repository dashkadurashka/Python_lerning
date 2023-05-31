# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = (input("Введите число: "))
summa = 0
if len(num) == 3:
    number = int(num)
    for i in range(3):
        summa = summa + number % 10
        number = number // 10
    print(summa)
else:
    print("Это не трехзначное число!")

