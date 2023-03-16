# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных 
# числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

import random
import math

randomX = random.randint(1, 10)
print(f"Первое загаданное число Петей: {randomX}")
randomY = random.randint(1, 10)
print(f"Второе загаданное число Петей: {randomY}")

sum = randomX + randomY
mult = randomX * randomY
D = math.sqrt(sum * sum - 4 * mult)
number1 = (-sum + D) / -2
number2 = (-sum - D) / -2


print(f"Катя назвала одно загаданное число: {round(number1)}")
print(f"Катя назвала второе загаданное число: {round(number2)}")
