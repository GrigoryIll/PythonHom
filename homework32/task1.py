"""
Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.

Написана в процедурной, структурной (есть циклы, ветвления) парадигме. Используется процедура, которую можно быстро и легко переиспользовать в коде, 
подав на вход необходимые параметры. 

"""


def bin_search(array, num):
    start = 0
    end = len(array)-1
    while start <= end:
        mid = (start + end) // 2
        if num == array[mid]:
            return mid
        if num < array[mid]:
            end = mid - 1
        if num > array[mid]:
            start = mid + 1
    return -1


print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100))