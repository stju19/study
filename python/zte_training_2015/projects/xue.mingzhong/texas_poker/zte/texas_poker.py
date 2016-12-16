__author__ = 'xue.mingzhong'
from collections import Counter

class PokerCard(object):
    def __init__(self, card):
        self._color = card[0]
        self._kind = int(card[1:])

    @property
    def kind(self):
        return self._kind

    @property
    def color(self):
        return self._color

    def __str__(self):
        return "{0}{1}".format(self._color, self._kind)


class TexasPoker(object):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8
    ROYAL_FLUSH = 9

    def __init__(self, cards):
        self._cards = [PokerCard(card.strip()) for card in cards.split(',')]

    def __str__(self):
        return ', '.join([str(card) for card in self._cards])

    def _is_straight(self):
        return len(self._cards) == self._cards[0].kind - self._cards[-1].kind + 1

    def _is_flush(self):
        return len(set([card.color for card in self._cards])) == 1

    def _level_for_none_same_kind(self):
        if self._is_straight() and self._is_flush():
            return self.STRAIGHT_FLUSH
        elif self._is_straight():
            return self.STRAIGHT
        elif self._is_flush():
            return self.FLUSH
        else:
            return self.HIGH_CARD

    def _level_for_any_same_kind(self, count_for_kinds):
        count_for_kind_to_level = {
            (2, 1, 1, 1): self.ONE_PAIR,
            (2, 2, 1): self.TWO_PAIR,  (3, 1, 1): self.THREE_OF_A_KIND,
            (3, 2): self.FULL_HOUSE,
            (4, 1): self.FOUR_OF_A_KIND
        }
        return count_for_kind_to_level[tuple(count_for_kinds)]

    def level(self):
        if  len(self._cards) != 5:
            raise Exception("Invalid texas poker for {0}".format(self))

        count_for_kinds = [count for count, kind in self.counter_of_kind_with_sorted()]
        if count_for_kinds[0] == 1:
            return self._level_for_none_same_kind()
        else:
            return self._level_for_any_same_kind(count_for_kinds)

    def counter_of_kind_with_sorted(self):
        counter_of_kinds = Counter([card.kind for card in self._cards])
        return sorted([(count, kind) for kind, count in counter_of_kinds.items()], reverse=True)

    def __cmp__(self, other):
        if self.level() == other.level():
            return cmp(self.counter_of_kind_with_sorted(), other.counter_of_kind_with_sorted())
        else:
            return cmp(self.level(), other.level())