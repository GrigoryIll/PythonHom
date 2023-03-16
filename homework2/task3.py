# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Введите положительное число\n"))
degree = 0
while number > 2 ** degree:
    print(2 ** degree, end = " ")
    degree += 1

