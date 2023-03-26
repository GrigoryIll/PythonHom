# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом 
# заданной во входном файле грядки.

import random
n = int(input("Введите количество кустов\n"))
i1 = 0
max_sum = 0
list1 = []
for i in range(n):
    list1.append(random.randint(1, 30))
print(list1)

while i1 < len(list1) - 2:
    print(list1[i1] + list1[i1 + 1] + list1[i1 + 2])
    if list1[i1] + list1[i1 + 1] + list1[i1 + 2] > max_sum:
        max_sum = list1[i1] + list1[i1 + 1] + list1[i1 + 2]
    i1 += 1
print(max_sum)