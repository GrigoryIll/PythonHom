from numberInInterval import *


def test_numberInInterval_in_range():
    assert numberInInterval(30) == True, "число не в заданном интервале"


def test_numberInInterval_not_in_range():
    assert numberInInterval(300) == False, "число в заданном интервале"


def test_numberInInterval_float():
    assert numberInInterval(400.0) == False, "число в заданном интервале"
