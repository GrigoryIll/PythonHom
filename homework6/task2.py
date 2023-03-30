# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

import random

start = int(input("Введите начало диапазона\n"))
end = int(input("Введите конец диапазона\n"))
list = []
for _ in range(10):
    list.append(random.randint(1, 5))

result = []
i = 0
while i < len(list):
    if list[i] in range(start, end + 1):
        result.append(i)
    i += 1

print(list)
print(result)

import random

start = int(input("Введите начало диапазона\n"))
end = int(input("Введите конец диапазона\n"))
list1 = []
for _ in range(10):
    list1.append(random.randint(1, 5))

result = []
i = 0
for _ in list1:
    if list1[i] in range(start, end + 1):
        result.append(i)
    i += 1

print(list1)
print(result)