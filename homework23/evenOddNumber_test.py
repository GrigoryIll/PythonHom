from evenOddNumber import *


def test_evenOddNumber_even():
    assert evenOddNumber(4) == True, "тест на четность. число нечетное"


def test_evenOddNumber_not_even():
    assert evenOddNumber(3) == False, "тест на нечетность, число четное"


def test_evenOddNumber_null():
    assert evenOddNumber(0) == True, "тест на четность. число нечетное"


def test_evenOddNumber_float():
    assert evenOddNumber(8.0) == True, "тест на четность. число нечетное"
