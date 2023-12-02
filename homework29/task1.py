"""
Игра крестики-нолики.
Написана в императивной, процедурной, структурной парадигмах, т.к. код выполняется последовательно, используются циклы и ветвления, используются процедуры,
которые выполняют определенные задачи.
"""

mas = [[0] * 3 for _ in range(3)]


def check():
    if mas[0][0] == mas[0][1] == mas[0][2] == "X" or mas[0][0] == mas[0][1] == mas[0][2] == "O":
        return False
    if mas[1][0] == mas[1][1] == mas[1][2] == "X" or mas[0][0] == mas[0][1] == mas[0][2] == "O":
        return False
    if mas[2][0] == mas[2][1] == mas[2][2] == "X" or mas[0][0] == mas[0][1] == mas[0][2] == "O":
        return False
    if mas[0][0] == mas[1][0] == mas[2][0] == "X" or mas[0][0] == mas[0][1] == mas[0][2] == "O":
        return False
    if mas[0][1] == mas[1][1] == mas[2][1] == "X" or mas[0][0] == mas[0][1] == mas[0][2] == "O":
        return False
    if mas[0][2] == mas[1][2] == mas[2][2] == "X" or mas[0][0] == mas[0][1] == mas[0][2] == "O":
        return False
    if mas[0][0] == mas[1][1] == mas[2][2] == "X" or mas[0][0] == mas[0][1] == mas[0][2] == "O":
        return False
    if mas[0][2] == mas[1][1] == mas[2][0] == "X" or mas[0][0] == mas[0][1] == mas[0][2] == "O":
        return False
    return True


def print_mas():
    for _ in mas:
        print(_)


while True:
    x1 = int(input("Ход первого игрока, введите строку\n"))
    y1 = int(input("Ход первого игрока, введите столбец\n"))
    mas[x1][y1] = "X"

    x2 = int(input("Ход второго игрока, введите строку\n"))
    y2 = int(input("Ход второго игрока, введите столбец\n"))
    mas[x2][y2] = "O"

    x3 = int(input("Ход первого игрока, введите строку\n"))
    y3 = int(input("Ход первого игрока, введите столбец\n"))
    mas[x3][y3] = "X"

    x4 = int(input("Ход второго игрока, введите строку\n"))
    y4 = int(input("Ход второго игрока, введите столбец\n"))
    mas[x4][y4] = "O"

    x5 = int(input("Ход первого игрока, введите строку\n"))
    y5 = int(input("Ход первого игрока, введите столбец\n"))
    mas[x5][y5] = "X"
    if check() == False:
        print("Победил первый игрок")
        print_mas()
        break

    x6 = int(input("Ход второго игрока, введите строку\n"))
    y6 = int(input("Ход второго игрока, введите столбец\n"))
    mas[x6][y6] = "O"
    if check() == False:
        print("Победил второй игрок")
        print_mas()
        break

    x7 = int(input("Ход первого игрока, введите строку\n"))
    y7 = int(input("Ход первого игрока, введите столбец\n"))
    mas[x7][y7] = "X"
    if check() == False:
        print("Победил первый игрок")
        print_mas()
        break

    x8 = int(input("Ход второго игрока, введите строку\n"))
    y8 = int(input("Ход второго игрока, введите столбец\n"))
    mas[x8][y8] = "O"
    if check() == False:
        print("Победил второй игрок")
        print_mas()
        break

    x9 = int(input("Ход первого игрока, введите строку\n"))
    y9 = int(input("Ход первого игрока, введите столбец\n"))
    mas[x9][y9] = "X"
    if check() == False:
        print("Победил первый игрок")
        print_mas()
        break
    if check() == True:
        print("Ничья")
        print_mas()
        break
