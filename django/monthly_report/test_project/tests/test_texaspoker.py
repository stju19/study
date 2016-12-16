__author__ = '10191230'

import os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
import unittest
from code.texaspoker import *

RAGGED = ['A11 A9 B2 C3 D6', 'A10 A3 B8 C5 D2']
ONE_PAIR = ['A11 A9 B3 C3 D6', 'A10 A3 B8 C5 D3']
TWO_PAIR = ['A11 A8 B2 C2 D8', 'A10 A2 B8 C8 D2']
TRIPLE = ['A11 A9 B9 C9 D6', 'A10 A8 B8 C8 D2']
STRAIGHT = ['A11 A9 B7 C8 D10', 'A10 B9 B8 C6 D7']
FLUSH = ['A11 A9 A2 A3 A6', 'B10 B3 B8 B5 B2']
CALABASH = ['A3 A9 B3 C3 D9', 'A10 A2 B10 C2 D2']
QUADRUPLE = ['A4 A9 B4 C4 D4', 'A10 A3 B3 C3 D3']
FLUSH_STRAIGHT = ['A8 A9 A6 A5 A7', 'B2 B3 B4 B5 B6']


class TestRagged(unittest.TestCase):
    def test_ragged(self):
        self.assertTrue(TexasPoker(RAGGED[0]) == TexasPoker(RAGGED[0]))
        self.assertTrue(TexasPoker(RAGGED[0]) > TexasPoker(RAGGED[1]))


class TestOnePair(unittest.TestCase):
    def test_one_pair(self):
        self.assertTrue(TexasPoker(ONE_PAIR[0]) > TexasPoker(ONE_PAIR[1]))
        self.assertTrue(TexasPoker(ONE_PAIR[0]) > TexasPoker(RAGGED[0]))


class TestTwoPair(unittest.TestCase):
    def test_two_pair(self):
        self.assertTrue(TexasPoker(TWO_PAIR[0]) > TexasPoker(TWO_PAIR[1]))
        self.assertTrue(TexasPoker(TWO_PAIR[0]) > TexasPoker(ONE_PAIR[0]))


class TestTripleCards(unittest.TestCase):
    def test_triple(self):
        self.assertTrue(TexasPoker(TRIPLE[0]) > TexasPoker(TRIPLE[1]))
        self.assertTrue(TexasPoker(TRIPLE[0]) > TexasPoker(TWO_PAIR[0]))


class TestStraightCards(unittest.TestCase):
    def test_straight(self):
        self.assertTrue(TexasPoker(STRAIGHT[0]) > TexasPoker(STRAIGHT[1]))
        self.assertTrue(TexasPoker(STRAIGHT[0]) > TexasPoker(TRIPLE[0]))


class TestFlushCards(unittest.TestCase):
    def test_flush(self):
        self.assertTrue(TexasPoker(FLUSH[0]) > TexasPoker(FLUSH[1]))
        self.assertTrue(TexasPoker(FLUSH[0]) > TexasPoker(STRAIGHT[0]))


class TestCalabashCards(unittest.TestCase):
    def test_calabash(self):
        self.assertTrue(TexasPoker(CALABASH[0]) > TexasPoker(CALABASH[1]))
        self.assertTrue(TexasPoker(CALABASH[0]) > TexasPoker(FLUSH[0]))


class TestQuadrupleCards(unittest.TestCase):
    def test_quadruple(self):
        self.assertTrue(TexasPoker(QUADRUPLE[0]) > TexasPoker(QUADRUPLE[1]))
        self.assertTrue(TexasPoker(QUADRUPLE[0]) > TexasPoker(CALABASH[0]))


class TestFlushStraight(unittest.TestCase):
    def test_flush_straight(self):
        self.assertTrue(TexasPoker(FLUSH_STRAIGHT[0]) > TexasPoker(FLUSH_STRAIGHT[1]))
        self.assertTrue(TexasPoker(FLUSH_STRAIGHT[0]) > TexasPoker(QUADRUPLE[0]))

if __name__ =='__main__':
    unittest.main()