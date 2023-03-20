# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# # число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# # *Пример:*
# # 5
# #     1 2 3 4 5
# #     6
# #     -> 5

import random

max_dif = 100
i = 0
x = 0
n = int(input("Введите количество элементов в списке (до 5)\n"))
print()
list1 = []
for num in range(n):
    list1.append(random.randint(1, 100))

random_num = random.randint(1, 100)

for j in list1:
    if i < n:
        if abs(random_num - list1[i]) <= max_dif:
            
            max_dif = abs(random_num - list1[i])
            x = list1[i]
        i += 1
                    
print(list1)
print(random_num)
print(x)