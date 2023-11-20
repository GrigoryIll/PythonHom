"""
Тесты для основного кода.

В основном выбрал сценарии на проверку работы выбрасывания ошибок в случае передачи 
некорректных аргументов(не списков, списков с str значениями и др.) 
в функцию, которые могли сломать ее работу или выдать некорректный результат.
Корректность подсчета при передаче корректных аргументов также проверяется, 
в том числе пустых списков.
"""
import pytest
from main import Calculate


def test_correct_result_int():
    """Тест на корректность подсчета для значений int"""

    result = Calculate([1, 9], [1, 7])
    error = "Первый список имеет большее среднее значение"
    assert result.average() == error,  "Неверный подсчет"


def test_correct_result_float():
    """Тест на корректность подсчета для значений float"""

    result = Calculate([1, 9.0], [1, 7.0])
    error = "Первый список имеет большее среднее значение"
    assert result.average() == error, "Неверный подсчет"


def test_error_args_not_list():
    """Тест на выбрасывания ошибки в случае передачи в аргументы не list"""

    with pytest.raises(TypeError) as error_info:
        Calculate(9, [1, 7])
    error = "Необходимо передать список в аргументы"
    assert str(
        error_info.value) == error, "Не выбрасывает ошибку TypeError"


def test_error_not_number_in_list1():
    """Тест на выбрасывание ошики в случае передачу в list1 не числа"""

    with pytest.raises(TypeError) as error_info:
        Calculate(["5", 1], [1, 7])
    error = "В список list1 необходимо передать int или float"
    assert str(
        error_info.value) == error, "Не выбрасывает ошибку TypeError"


def test_error_not_number_in_list2():
    """Тест на выбрасывание ошики в случае передачу в list2 не числа"""

    with pytest.raises(TypeError) as error_info:
        Calculate([5, 1], [1, "7"])
    error = "В список list2 необходимо передать int или float"
    assert str(
        error_info.value) == error, "Не выбрасывает ошибку TypeError"


def test_correct_result_empy_list1():
    """Тест на корректность работы в случае передачи в list1 пустого списка"""

    result = Calculate([], [1, 7.0])
    error = "Второй список имеет большее среднее значение"
    assert result.average() == error, "Неверный подсчет"


def test_correct_result_empy_list2():
    """Тест на корректность работы в случае передачи в list2 пустого списка"""

    result = Calculate([1, 7.0], [])
    error = "Первый список имеет большее среднее значение"
    assert result.average() == error, "Неверный подсчет"
