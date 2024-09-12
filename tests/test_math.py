import pytest

from app.utils.number import Number
from app.utils.numbers import Numbers


def test_sum():
    # Test case 1 - sum of two positive numbers
    number = Number()
    assert number.sum(2, 3) == 5

    # Test case 2 - sum of two negative numbers
    number = Number()
    assert number.sum(-2, -3) == -5

    # Test case 3 - sum of a positive and a negative number
    number = Number()
    assert number.sum(2, -3) == -1

    # Test case 4 - sum of two zeros
    number = Number()
    assert number.sum(0, 0) == 0


def test_divide():
    # Test case 1 - divide two positive numbers
    number = Number()
    assert number.divide(10, 2) == 5.0

    # Test case 2 - divide two negative numbers
    number = Number()
    assert number.divide(-10, -2) == 5.0

    # Test case 3 - divide a positive and a negative number
    number = Number()
    assert number.divide(10, -2) == -5.0

    # Test case 4 - divide by zero
    number = Number()
    with pytest.raises(ZeroDivisionError):
        number.divide(10, 0)


def test_sum_numbers():
    # Test case 1 - sum of positive numbers
    numbers = Numbers()
    assert numbers.sum([1, 2, 3, 4, 5]) == 15

    # Test case 2 - sum of negative numbers
    numbers = Numbers()
    assert numbers.sum([-1, -2, -3, -4, -5]) == -15

    # Test case 3 - sum of positive and negative numbers
    numbers = Numbers()
    assert numbers.sum([1, -2, 3, -4, 5]) == 3

    # Test case 4 - sum of zeros
    numbers = Numbers()
    assert numbers.sum([0, 0, 0, 0, 0]) == 0


def test_average():
    # Test case 1 - average of positive numbers
    numbers = Numbers()
    assert numbers.average([1, 2, 3, 4, 5]) == 3.0

    # Test case 2 - average of negative numbers
    numbers = Numbers()
    assert numbers.average([-1, -2, -3, -4, -5]) == -3.0

    # Test case 3 - average of positive and negative numbers
    numbers = Numbers()
    assert numbers.average([1, -2, 3, -4, 5]) == 0.6

    # Test case 4 - average of zeros
    numbers = Numbers()
    assert numbers.average([0, 0, 0, 0, 0]) == 0.0
