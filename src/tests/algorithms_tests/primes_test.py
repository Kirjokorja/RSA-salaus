import unittest
from algorithms.primes import PrimesGenerator


class TestPrimesGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = PrimesGenerator(10000)

    def test_is_prime_for_2(self):
        self.assertTrue(self.gen.is_prime(2))

    def test_is_prime_for_negative_numbers(self):
        self.assertFalse(self.gen.is_prime(-2))
        self.assertFalse(self.gen.is_prime(-10))
        self.assertFalse(self.gen.is_prime(-578220543932))

    def test_is_prime_for_1(self):
        self.assertFalse(self.gen.is_prime(1))

    def test_is_prime_for_0(self):
        self.assertFalse(self.gen.is_prime(0))

    def test_is_prime_for_known_prime_3_digits(self):
        self.assertTrue(self.gen.is_prime(757))

    def test_is_prime_for_known_prime_4_digits(self):
        self.assertTrue(self.gen.is_prime(2689))

    def test_is_prime_for_known_prime_8_digits(self):
        self.assertTrue(self.gen.is_prime(82589933))

    def test_is_prime_for_known_prime_10_digits(self):
        self.assertTrue(self.gen.is_prime(5463458053))

    def test_is_prime_for_known_prime_35_digits(self):
        self.assertTrue(
            self.gen.is_prime(23768741896345550770650537601358309),
        )

    def test_is_prime_for_known_prime_100_digits(self):
        self.assertTrue(
            self.gen.is_prime(
                2908511952812557872434704820397229928450530253990158990550731991011846571635621025786879881561814989),
        )

    def test_is_prime_for_known_prime_290_digits(self):
        self.assertTrue(
            self.gen.is_prime(47636001527157843615510166362212813825553995166349359052560828063795751982743949356281378571281356684995526346349689115319412565735006540850254022130876377867983398374239198108049044484863543699346022227692817853215225730056764957039852693911896900286014520659611654434776741074401112976951),
        )

    def test_is_prime_for_known_prime_300_digits(self):
        self.assertTrue(
            self.gen.is_prime(531872289054204184185084734375133399408303613982130856645299464930952178606045848877129147820387996428175564228204785846141207532462936339834139412401975338705794646595487324365194792822189473092273993580587964571659678084484152603881094176995594813302284232006001752128168901293560051833646881436219),
            True
        )

    def test_is_prime_for_composite_of_3_and_four_digit_numbers(self):
        self.assertFalse(self.gen.is_prime(757*2689))

    def test_is_prime_for_composite_of_8_and_10_digit_numbers(self):
        self.assertFalse(self.gen.is_prime(43112609*2147483647))

    def test_is_prime_for_composite_of_100_and_35_digit_numbers(self):
        self.assertFalse(
            self.gen.is_prime(
                2908511952812557872434704820397229928450530253990158990550731991011846571635621025786879881561814989*23768741896345550770650537601358309),
        )

    def test_is_prime_for_composite_of_300_and_290_digit_numbers(self):
        self.assertFalse(
            self.gen.is_prime(531872289054204184185084734375133399408303613982130856645299464930952178606045848877129147820387996428175564228204785846141207532462936339834139412401975338705794646595487324365194792822189473092273993580587964571659678084484152603881094176995594813302284232006001752128168901293560051833646881436219 *
                              47636001527157843615510166362212813825553995166349359052560828063795751982743949356281378571281356684995526346349689115319412565735006540850254022130876377867983398374239198108049044484863543699346022227692817853215225730056764957039852693911896900286014520659611654434776741074401112976951),
        )
