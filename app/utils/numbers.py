from .number import divide
from .number import sum as sum_number


def sum(numbers: list[int]) -> int:
    final_sum = 0
    for number in numbers:
        final_sum = sum_number(final_sum, number)

    return final_sum


def average(numbers: list[int]) -> float:
    final_sum = 0
    for number in numbers:
        final_sum = sum_number(final_sum, number)

    return divide(final_sum, len(numbers))
