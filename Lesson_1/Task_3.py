# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и
# получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

number_of_ticket = input("Ваш билетик, пожалуйста: ")
sum_1 = 0
sum_2 = 0
if len(number_of_ticket) == 6:
    number_of_ticket = int(number_of_ticket)
    num_1 = number_of_ticket // 1000
    num_2 = number_of_ticket % 1000
    for i in range(3):
        sum_1 = sum_1 + num_1 % 10
        num_1 = num_1 // 10
    for i in range(3):
        sum_2 = sum_2 + num_2 % 10
        num_2 = num_2 // 10
    if sum_1 == sum_2:
        print("Ураа, вас ожидает удача")
    else:
        print("Повезет в любви")
else:
    print("Неверный номер билетика")