"""Таблица умножения всех чисел от 1 до n.
Написана в процедурной парадигме, для того чтобы процедуру можно было использовать много раз, с разными входными данными."""

n = int(input("Введите число\n"))


def multi(n):
    for i in range(1, n+1):
        for j in range(1, 10):
            print(i, "*", j, "=", i * j)
        print()


multi(n)