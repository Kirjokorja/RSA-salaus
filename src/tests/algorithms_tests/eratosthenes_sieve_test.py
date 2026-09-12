import unittest
from algorithms import (eratosthenes_sieve as sieve)

class TestErathosthenesSieve(unittest.TestCase):

    def test_get_primes_list_returns_list(self):
        primes = sieve.get_primes_list(5)
        self.assertEqual(type(primes), type(list()))

    def test_get_primes_list_returns_correct_primes_for_2(self):
        primes = [2]
        test_primes= sieve.get_primes_list(2)
        self.assertEqual(test_primes, primes)

    def test_get_primes_list_returns_correct_primes_for_11(self):
        primes = [2, 3, 5, 7, 11]
        test_primes = sieve.get_primes_list(11)
        self.assertEqual(test_primes, primes)

    def test_get_primes_list_returns_correct_primes_for_100(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19,23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        test_primes= sieve.get_primes_list(100)
        self.assertEqual(test_primes, primes)
        
        
