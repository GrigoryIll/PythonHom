"""Написать скрипт для расчета корреляции Пирсона между
двумя случайными величинами (двумя массивами)."""

from math import *

mas1 = [2, 4, 6, 8]
mas2 = [1, 3, 7, 13]


def pirson():
    aver_mas1 = sum(mas1)/len(mas1)
    aver_mas2 = sum(mas2)/len(mas2)
    res1 = 0
    res2_1 = 0
    res2_2 = 0
    for i in range(len(mas1)):
        sum1 = (mas1[i] - aver_mas1) * (mas2[i] - aver_mas2)
        sum2_1 = (mas1[i]-aver_mas1) ** 2
        sum2_2 = (mas2[i]-aver_mas2) ** 2
        res1 += sum1
        res2_1 += sum2_1
        res2_2 += sum2_2
    sqrt1 = sqrt(res2_1 * res2_2)
    res = res1 / sqrt1
    return res


print(pirson())
