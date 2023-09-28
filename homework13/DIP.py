from abc import ABC, abstractmethod


class Multiplier:
    @abstractmethod
    def get_result(self):
        pass


class Number5(Multiplier):
    def get_result(self):
        return 5


def my_function(num: Multiplier):
    return num.get_result() * 2


print(my_function(Number5()))
