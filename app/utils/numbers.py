from .number import Number


class Numbers:
    def sum(self, numbers: list[int]) -> int:
        final_sum = 0
        number_class = Number()
        for number in numbers:
            final_sum = number_class.sum(final_sum, number)

        return final_sum

    def average(self, numbers: list[int]) -> float:
        final_sum = 0
        number_class = Number()
        for number in numbers:
            final_sum = number_class.sum(final_sum, number)

        return number_class.divide(final_sum, len(numbers))
