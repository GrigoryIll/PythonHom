import pytest
from calculator import *


@pytest.mark.parametrize('purchase_amount, discount, expected_result', [(100, 10, 90), (100, 20, 80), (100, 10, 5)])
def test_calculate_result_int(purchase_amount, discount, expected_result):
    calculator = Calculator()
    assert calculator.calculateDiscount(
        purchase_amount, discount) == expected_result, "Неверный подсчет"


@pytest.mark.parametrize('purchase_amount, discount, expected_result', [(100.1, 10.1, 89.98989999999999), (100.2, 50.5, 49.599)])
def test_calculate_result_float(purchase_amount, discount, expected_result):
    calculator = Calculator()
    assert calculator.calculateDiscount(
        purchase_amount, discount) == expected_result, "Неверный подсчет"


def test_negative_amount_discount():
    calculator = Calculator()
    calculator.calculateDiscount(100, -10)


def test_string_in_amount_discount():
    calculator = Calculator()
    calculator.calculateDiscount(100, "y")


def test_amount_is_null():
    calculator = Calculator()
    calculator.calculateDiscount(0, 10)
