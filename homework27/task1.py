"""
Задача №1
Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
"""


def sort_list_imperative(list1):
    for i in range(len(list1) - 1):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j+1]:
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1


print(sort_list_imperative([5, 9, 7, 8, 1]))

"""
Задача №2
Написать точно такую же процедуру, но в декларативном стиле
"""


def sort_list_declarative(list1):
    list1.sort()
    return list1


print(sort_list_declarative([5, 9, 7, 8, 1]))
