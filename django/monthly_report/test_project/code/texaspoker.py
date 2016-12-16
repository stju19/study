__author__ = '10191230'
from operator import itemgetter


class TexasPoker(object):

    def __init__(self, input_string):
        self.colors = [x[0] for x in input_string.split(' ')]
        self.numbers = [int(x[1:]) for x in input_string.split(' ')]
        self.weight = 0
        self._execute_weight_and_sort()

    def _is_flush(self):
        return self.colors.count(self.colors[0]) == 5

    def _is_straight(self):
        self.numbers.sort()
        for i in range(0, 4):
            if self.numbers[i + 1] - self.numbers[i] != 1:
                return False
        return True

    def _execute_weight_and_sort(self):
        """Counted_numbers is a list of number and the same numbers count in numbers,
        weight is sum of the same numbers' count,there are mapping of poker's type and weight:
        RAGGED = 5
        ONE_PAIR = 7
        TWO_PAIR = 9
        TRIPLE = 11
        STRAIGHT = 11.5
        FLUSH = 12
        CALABASH = 13
        QUADRUPLE = 17
        FLUSH_STRAIGHT = 18.5

        example_numbers = [2, 8, 9, 2, 5]
        example_counted_numbers = [(2, 2), (8, 1), (9, 1), (2, 2), (5, 1)]
        example_weight = 7
        """
        counted_numbers = [(number, self.numbers.count(number)) for number in self.numbers]
        counted_numbers.sort(key=itemgetter(1, 0), reverse=True)
        self.numbers = [number for number, count in counted_numbers]
        self.weight = sum([count for number, count in counted_numbers])
        if self.weight == 5:
            self.weight = 5 + self._is_straight() * 6.5 + self._is_flush() * 7

    def __lt__(self, other):
        result = cmp(self.weight , other.weight)
        return True if result < 0 else result == 0 and cmp(self.numbers, other.numbers) < 0

    def __eq__(self, other):
        return cmp(self.weight , other.weight) == 0 and cmp(self.numbers, other.numbers) == 0