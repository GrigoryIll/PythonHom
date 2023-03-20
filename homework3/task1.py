# # Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# # *Пример:*
# # 5
# #     1 2 3 4 5
# #     3
# #     -> 1

import random
count = 0
n = int(input("Введите количество элементов списка\n"))
list1 = []
for i in range(n):
    list1.append(random.randint(1, 5))
    
random_num = random.randint(1, 5)
for j in list1:
    if random_num == j:
        count += 1

print(list1)
print(random_num)
print(count)