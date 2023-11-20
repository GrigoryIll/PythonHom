
"""Основной код"""


class Calculate:
    """Класс, который будет проводить расчеты"""

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Необходимо передать список в аргументы")
        for elem in list1:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "В список list1 необходимо передать int или float")
        for elem in list2:
            if not isinstance(elem, (int, float)):
                raise TypeError(
                    "В список list2 необходимо передать int или float")

    def average(self):
        """Будет находить среднее значений списков, сравнивать и выводить результат"""

        if len(self.list1) < 1:
            average1 = 0
        else:
            average1 = (sum(self.list1))/len(self.list1)
        if len(self.list2) < 1:
            average2 = 0
        else:
            average2 = (sum(self.list2))/len(self.list2)
        if average1 > average2:
            return "Первый список имеет большее среднее значение"
        if average2 > average1:
            return "Второй список имеет большее среднее значение"
        return "Средние значения равны"
