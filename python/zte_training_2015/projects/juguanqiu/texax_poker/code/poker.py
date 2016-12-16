#!/usr/bin/env python
"""
Texas Hold'em poker
"""
from collections import Counter
POKER_TYPE_OTHER = 1
POKER_TYPE_ONE_PAIR = 2
POKER_TYPE_TWO_PAIRS = 3
POKER_TYPE_THREE_OF_A_KIND = 4
POKER_TYPE_STRAIGHT = 5
POKER_TYPE_FLUSH = 6
POKER_TYPE_FULL_HOUSE = 7
POKER_TYPE_FOUR_OF_A_KIND = 8
POKER_TYPE_STRAIGHT_FLUSH = 9
POKER_TYPE_ROYAL_FLUSH = 10


class Poker(object):
    """ class of basic poker """
    def __init__(self, poker):
        self.color = poker[0].upper()
        self.num = int(poker[1:])

    def __cmp__(self, other):
        return cmp(self.num, other.num)


class Suit(object):
    def __init__(self, suit):
        self.poker_group = [Poker(suit[0]), Poker(suit[1]), Poker(suit[2]),
                            Poker(suit[3]), Poker(suit[4])]

    def get_style(self):
        same_number_flag = self._get_same_number_flag()
        style_dict = {
            0: self._get_style_for_different_numbers(), 1: POKER_TYPE_ONE_PAIR,
            2: POKER_TYPE_TWO_PAIRS, 3: POKER_TYPE_THREE_OF_A_KIND,
            4: POKER_TYPE_FULL_HOUSE, 6: POKER_TYPE_FOUR_OF_A_KIND
        }
        return style_dict[same_number_flag]

    def _get_same_number_flag(self):
        """ return flag, refer to times of repetition in poker group """
        flag = 0
        for i in range(5):
            for j in range(i+1, 5):
                if self.poker_group[i].num == self.poker_group[j].num:
                    flag += 1
        return flag

    def _get_style_for_different_numbers(self):
        if self.is_flush():
            style = self._get_style_for_flush()
        elif self.is_straight():
            style = POKER_TYPE_STRAIGHT
        else:
            style = POKER_TYPE_OTHER
        return style

    def _get_style_for_flush(self):
        if not self.is_straight():
            return POKER_TYPE_FLUSH
        ordered_poker_group = sorted(self.poker_group)
        if ordered_poker_group[4].num == 14:
            return POKER_TYPE_ROYAL_FLUSH
        else:
            return POKER_TYPE_STRAIGHT_FLUSH

    def is_flush(self):
        color_set = set([poker.color for poker in self.poker_group])
        return True if len(color_set) == 1 else False

    def is_straight(self):
        ordered_poker_group = sorted(self.poker_group)
        return True if ordered_poker_group[4].num - \
                       ordered_poker_group[0].num == 4 else False

    def __cmp__(self, other):
        if self.get_style() != other.get_style():
            return cmp(self.get_style(), other.get_style())
        else:
            return cmp(self.get_weighed_list(), other.get_weighed_list())

    def get_weighed_list(self):
        weighed_dict = Counter([poker.num for poker in self.poker_group])
        weighed_list = weighed_dict.items()
        weighed_list = sorted(weighed_list, key=lambda d: d[0], reverse=True)
        weighed_list = sorted(weighed_list, key=lambda d: d[1], reverse=True)
        return [poker[0] for poker in weighed_list]
