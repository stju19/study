__author__ = 'xue.mingzhong'

from unittest import TestCase
from zte.texas_poker import TexasPoker


class TestHighCard(TestCase):
    def test_first_9_is_greater_than_8(self):
        self.assertGreater(TexasPoker("A9, A7, A4, A3, D2"),
                           TexasPoker("A8, A7, A4, A3, D2"))

    def test_only_3_greater_than_2(self):
        self.assertGreater(TexasPoker("A11, A10, A9, A8, D3"),
                           TexasPoker("A11, A10, A9, A8, D2"))

    def test_equal_all_with_different_order(self):
        self.assertEqual(TexasPoker("C2, B11, B10, B9, B8"),
                         TexasPoker("A11, A10, A9, A8, D2"))


class TestOnePairCard(TestCase):
    def test_pair_of_2_greater_than_high_card_of_8(self):
        self.assertGreater(TexasPoker("A2, A7, A4, A3, D2"),
                           TexasPoker("A8, A7, A4, A3, D2"))

    def test_all_equal(self):
        self.assertEqual(TexasPoker("A3, C3, A9, A8, D5"),
                         TexasPoker("A9, A8, D5, A3, C3"))

    def test_pair_of_8_greater_than_pair_of_5(self):
        self.assertGreater(TexasPoker("A3, A9, C8, A8, D5"),
                           TexasPoker("A3, A9, A8, C5, D5"))


class TestTwoPairCard(TestCase):
    def test_pair_of_3_and_2_greater_than_pair_of_14(self):
        self.assertGreater(TexasPoker("A3, C2, B3, A2, D5"),
                           TexasPoker("A14, C3, B14, A8, D5"))

    def test_first_pair_9_greater_8(self):
        self.assertGreater(TexasPoker("A9, C9, B3, A6, D6"),
                           TexasPoker("A7, C8, B8, A7, D9"))

    def test_second_pair_7_greater_6(self):
        self.assertGreater(TexasPoker("A7, C7, B3, A8, D8"),
                           TexasPoker("A6, C8, B8, A6, D9"))

    def test_third_card_3_greater_than_2(self):
        self.assertGreater(TexasPoker("A9, C9, B3, A6, D6"),
                           TexasPoker("A9, C9, B6, A6, D2"))

    def test_all_equal(self):
        self.assertEqual(TexasPoker("A9, C9, B3, A6, D6"),
                         TexasPoker("A9, C9, B6, A6, D3"))


class TestThreeCard(TestCase):
    def test_three_of_2_greater_than_two_pair_of_4_5(self):
        self.assertGreater(TexasPoker("A2, A7, A4, C2, D2"),
                           TexasPoker("A3, B3, A4, A8, D4"))

    def test_three_of_4_greater_than_two_of_3(self):
        self.assertGreater(TexasPoker("A13, A7, A4, C4, D4"),
                           TexasPoker("A3, B3, A7, A8, D13"))


class TestStraightCard(TestCase):
    def test_Straight_of_8_greater_than_Three_of_9(self):
        self.assertGreater(TexasPoker("A8, B7, D6, C5, D4"),
                           TexasPoker("A9, B9, A9, A8, D13"))

    def test_Straight_of_8_greater_7(self):
        self.assertGreater(TexasPoker("A8, B7, D6, C5, D4"),
                           TexasPoker("A7, B6, A5, A4, D3"))

    def test_Straight_of_8_equal_8(self):
        self.assertEqual(TexasPoker("A8, B7, D6, C5, D4"),
                         TexasPoker("C8, A7, B6, A5, A4"))

    def test_not_straight_of_9_7_7_6_5(self):
        self.assertNotEqual(TexasPoker("A9, B7, D7, C6, D5").level(),
                            TexasPoker.STRAIGHT)

class TestFlushCard(TestCase):
    def test_flush_of_8_greater_Straight_of_9(self):
        self.assertGreater(TexasPoker("A8, A7, A6, A2, A4"),
                           TexasPoker("A9, B8, B7, B6, B5"))

    def test_fLush_of_8_greater_than_flush_7_at_highest(self):
        self.assertGreater(TexasPoker("A8, A7, A6, A2, A4"),
                           TexasPoker("B5, B7, B6, B2, B4"))

    def test_fLush_of_8_greater_than_flush_7_at_last(self):
        self.assertGreater(TexasPoker("A13, A12, A11, A10, A8"),
                           TexasPoker("B13, B12, B11, B10, B7"))


class TestFullHouseCard(TestCase):
    def test_full_house_of_3_4_greater_than_flush_of_9(self):
        self.assertGreater(TexasPoker("A3, B3, C3, A4, B4"),
                           TexasPoker("B10, B8, B7, B6, B5"))

    def test_full_house_of_5_6_greater_than_full_house_of_4_3(self):
        self.assertGreater(TexasPoker("A5, B5, C5, A6, B6"),
                           TexasPoker("B4,C4,D4,B3,C3"))


class TestFourOfAKindCard(TestCase):
    def test_four_of_2_greater_than_full_house_of_3_4(self):
        self.assertGreater(TexasPoker("A2, B2, C2, D2, B7"),
                           TexasPoker("A3, B3, C3, A4, B4"))

    def test_four_of_6_greater_than_four_of_5(self):
        self.assertGreater(TexasPoker("A6, B6, C6, A6, B9"),
                           TexasPoker("A5, B5, C5, D5, C10"))


class TestStraightFlushCard(TestCase):
    def test_straight_flush_of_8_greater_than_four_of_9(self):
        self.assertGreater(TexasPoker("A8, A7, A6, A5, A4"),
                           TexasPoker("A9, B9, C9, D9, B10"))

    def test_straight_flush_of_8_greater_than_straight_flush_of_7(self):
        self.assertGreater(TexasPoker("A8, A7, A6, A5, A4"),
                           TexasPoker("B7, B6, B5, B4, B3"))

    def test_straight_flush_of_8_equal_straight_flush_of_8(self):
        self.assertEqual(TexasPoker("A8, A7, A6, A5, A4"),
                         TexasPoker("B8, B7, B6, B5, B4"))


class TestInvalidTexasPoker(TestCase):
    def test_invalid_cards(self):
        self.assertRaises(Exception, TexasPoker("A2, B2, C2").level)
        self.assertRaises(Exception,
                          TexasPoker("A1, A2, A3, B3, B4, B5").level)

