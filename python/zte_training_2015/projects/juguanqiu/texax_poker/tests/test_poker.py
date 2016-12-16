#!/usr/bin/env python
"""
Test for Texas Hold'em poker
"""
__author__ = '10183988'

import unittest
import sys
sys.path[0] = sys.path[0].replace('/texax_poker/tests', '')

from texax_poker.code.poker import Suit

suit_other = Suit(['a2', 'b3', 'c6', 'c12', 'd5'])
suit_one_pair = Suit(['a2', 'b2', 'c3', 'd11', 'a14'])
suit_two_pairs = Suit(['a2', 'b2', 'b6', 'd6', 'a12'])
suit_three_of_a_kind = Suit(['a13', 'a11', 'd13', 'b13', 'c14'])
suit_straight = Suit(['a5', 'b6', 'c7', 'd8', 'a9'])
suit_flush = Suit(['c3', 'c6', 'c8', 'c9', 'c12'])
suit_full_house = Suit(['a8', 'b3', 'd8', 'd3', 'a3'])
suit_four_of_a_kind = Suit(['a5', 'b5', 'c5', 'd5', 'c10'])
suit_straight_flush = Suit(['c4', 'c5', 'c6', 'c7', 'c8'])
suit_royal_flush = Suit(['a10', 'a11', 'a12', 'a13', 'a14'])


class DifferentStyleCompareTestCase(unittest.TestCase):
    """ Test for different poker style comparison """
    def test_other_and_one_pair(self):
        self.assertTrue(suit_other < suit_one_pair)

    def test_one_pair_and_two_pairs(self):
        self.assertTrue(suit_one_pair < suit_two_pairs)

    def test_two_pairs_and_three_of_a_kind(self):
        self.assertTrue(suit_two_pairs < suit_three_of_a_kind)

    def test_three_of_a_kind_and_straight(self):
        self.assertTrue(suit_three_of_a_kind < suit_straight)

    def test_straight_and_flush(self):
        self.assertTrue(suit_straight < suit_flush)

    def test_flush_and_full_house(self):
        self.assertTrue(suit_flush < suit_full_house)

    def test_full_house_and_four_of_a_kind(self):
        self.assertTrue(suit_full_house < suit_four_of_a_kind)

    def test_four_of_a_kind_and_straight_flush(self):
        self.assertTrue(suit_four_of_a_kind < suit_straight_flush)

    def test_straight_flush_and_royal_flush(self):
        self.assertTrue(suit_straight_flush < suit_royal_flush)


class SameStyleCompareTestCase(unittest.TestCase):
    """ Test for same poker style comparison """
    def test_cmp_suit_other(self):
        other_one = Suit(['a2', 'b3', 'c6', 'c12', 'd5'])
        other_two = Suit(['a4', 'c2', 'c7', 'd14', 'b9'])
        other_equal_to_one = Suit(['b2', 'b3', 'a6', 'c5', 'd12'])
        self.assertTrue(other_one < other_two)
        self.assertTrue(other_one == other_equal_to_one)

    def test_cmp_suit_one_pair(self):
        one_pair_one = Suit(['a2', 'b2', 'c3', 'd11', 'a14'])
        one_pair_two = Suit(['a5', 'b5', 'd2', 'd7', 'c14'])
        one_pair_equal_to_one = Suit(['c2', 'a2', 'c3', 'd11', 'a14'])
        self.assertTrue(one_pair_one < one_pair_two)
        self.assertTrue(one_pair_one == one_pair_equal_to_one)

    def test_cmp_suit_two_pairs(self):
        two_pairs_one = Suit(['a2', 'b2', 'b6', 'd6', 'a12'])
        two_pairs_two = Suit(['a4', 'b4', 'b6', 'd6', 'a12'])
        two_pairs_equal_to_one = Suit(['c2', 'd2', 'a6', 'd6', 'd12'])
        self.assertTrue(two_pairs_one < two_pairs_two)
        self.assertTrue(two_pairs_one == two_pairs_equal_to_one)

    def test_cmp_suit_three_of_a_kind(self):
        three_of_a_kind_one = Suit(['a13', 'a11', 'd13', 'b13', 'c14'])
        three_of_a_kind_two = Suit(['a10', 'a11', 'd14', 'b14', 'c14'])
        three_of_a_kind_equal_to_one = Suit(['a14', 'c11', 'd13', 'b13', 'c13'])
        self.assertTrue(three_of_a_kind_one < three_of_a_kind_two)
        self.assertTrue(three_of_a_kind_one == three_of_a_kind_equal_to_one)

    def test_cmp_suit_straight(self):
        straight_one = Suit(['a5', 'b6', 'c7', 'd8', 'a9'])
        straight_two = Suit(['a7', 'b8', 'c9', 'd10', 'a11'])
        straight_equal_to_one = Suit(['a7', 'b9', 'c5', 'd8', 'a6'])
        self.assertTrue(straight_one < straight_two)
        self.assertTrue(straight_one == straight_equal_to_one)

    def test_cmp_suit_flush(self):
        flush_one = Suit(['c3', 'c6', 'c8', 'c9', 'c12'])
        flush_two = Suit(['c4', 'c6', 'c7', 'c10', 'c12'])
        flush_equal_to_one = Suit(['d3', 'd6', 'd12', 'd9', 'd8'])
        self.assertTrue(flush_one < flush_two)
        self.assertTrue(flush_one == flush_equal_to_one)

    def test_cmp_suit_full_house(self):
        full_house_one = Suit(['a8', 'b3', 'd8', 'd3', 'a3'])
        full_house_two = Suit(['a5', 'b5', 'd5', 'd8', 'a8'])
        full_house_equal_to_one = Suit(['b8', 'c8', 'b3', 'd3', 'a3'])
        self.assertTrue(full_house_one < full_house_two)
        self.assertTrue(full_house_one == full_house_equal_to_one)

    def test_cmp_suit_four_of_a_kind(self):
        four_of_a_kind_one = Suit(['a5', 'b5', 'c5', 'd5', 'c10'])
        four_of_a_kind_two = Suit(['a5', 'b5', 'c5', 'd5', 'c11'])
        four_of_a_kind_equal_to_one = Suit(['a5', 'b5', 'c5', 'd5', 'd10'])
        self.assertTrue(four_of_a_kind_one < four_of_a_kind_two)
        self.assertTrue(four_of_a_kind_one == four_of_a_kind_equal_to_one)

    def test_cmp_suit_straight_flush(self):
        straight_flush_one = Suit(['c4', 'c5', 'c6', 'c7', 'c8'])
        straight_flush_two = Suit(['c6', 'c7', 'c8', 'c9', 'c10'])
        straight_flush_equal_to_one = Suit(['a8', 'a7', 'a6', 'a5', 'a4'])
        self.assertTrue(straight_flush_one < straight_flush_two)
        self.assertTrue(straight_flush_one == straight_flush_equal_to_one)

    def test_cmp_suit_royal_flush(self):
        royal_flush_one = Suit(['a10', 'a11', 'a12', 'a13', 'a14'])
        royal_flush_two = Suit(['b14', 'b12', 'b11', 'b10', 'b13'])
        royal_flush_equal_to_one = Suit(['d10', 'd11', 'd12', 'd13', 'd14'])
        self.assertTrue(royal_flush_one == royal_flush_two)
        self.assertTrue(royal_flush_one == royal_flush_equal_to_one)


if __name__ == "__main__":
    unittest.main()
