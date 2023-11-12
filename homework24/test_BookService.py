from BookRepository import *
from BookService import *
from pytest_mock import *


def test_get_book_by_id(mocker):
    mock_get_book_by_id = mocker.Mock(
        side_effect=lambda id: ["Book1", "Book2"], return_value=["Book1", "Book2"])
    mocker.patch.object(BookRepository, "get_book_by_id", mock_get_book_by_id)
    result = mock_get_book_by_id(5)
    mock_get_book_by_id.assert_called_once_with(5)
    assert result == [
        "Book1", "Book2"], "Книга по id выдана неверно"


def test_get_book_by_title(mocker):
    mock_get_book_by_title = mocker.Mock(
        side_effect=lambda title: 13, return_value=13)
    mocker.patch.object(BookRepository, "get_book_by_title",
                        mock_get_book_by_title)
    result = mock_get_book_by_title("Book3")
    mock_get_book_by_title.assert_called_once_with("Book3")
    assert result == 13, "Книга по title выдана неверно"
