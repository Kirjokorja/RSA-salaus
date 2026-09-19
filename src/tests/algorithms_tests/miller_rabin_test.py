import unittest
from algorithms import miller_rabin

class TestMillerRabin(unittest.TestCase):

    def test_find_odd_returns_negative_for_smaller_than_2(self):
        self.assertEqual(miller_rabin.find_odd(1), -1)
        self.assertEqual(miller_rabin.find_odd(0), -1)
        self.assertEqual(miller_rabin.find_odd(-100), -1)

    def test_find_odd_returns_first_odd_number_for_2(self):
        self.assertEqual(miller_rabin.find_odd(2), 1)

    def test_find_odd_returns_first_odd_number_for_11(self):
        self.assertEqual(miller_rabin.find_odd(11), 5)

    def test_find_odd_returns_first_odd_number_for_101(self):
        self.assertEqual(miller_rabin.find_odd(101), 25)

    def test_find_odd_returns_first_odd_number_for_2048(self):
        self.assertEqual(miller_rabin.find_odd(2048), 2047)
