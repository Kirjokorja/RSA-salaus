import unittest
from crypto.rsa import RSACrypto
from exceptions import rsa_exceptions as exceptions
from algorithms.primes import PrimesGenerator

class TestRSACrypto(unittest.TestCase):
    def setUp(self):
        self.primes_gen = PrimesGenerator(10000)
        self.crypto_256 = RSACrypto(256, self.primes_gen, exceptions)
        self.keys_256 = self.crypto_256.generate_keys()

    def test_generate_keys_returns_dictonary(self):
        self.assertEqual(type(self.keys_256), type({}))

    def test_genrate_keys_returns_dictonary_that_contains_keys_public_and_secret(self):
        self.assertIn("public", self.keys_256)
        self.assertIn("secret", self.keys_256)

    def test_generate_keys_returns_two_tuples_in_dictonary(self):
        self.assertEqual(type(self.keys_256["public"]), type(()))
        self.assertEqual(type(self.keys_256["secret"]), type(()))

    def test_generate_keys_returns_integer_pairs_in_tuples_in_dictonary(self):
        self.assertEqual(type(self.keys_256["public"][0]), type(int()))
        self.assertEqual(type(self.keys_256["public"][1]), type(int()))
        self.assertEqual(type(self.keys_256["secret"][0]), type(int()))
        self.assertEqual(type(self.keys_256["secret"][1]), type(int()))

    def test_generate_keys_generates_keys_greater_than_2048_bits_when_class_attribute_key_size_is_2048_bits(self):
        crypto = RSACrypto(2048, self.primes_gen, exceptions)
        keys = crypto.generate_keys()
        self.assertGreater(keys["public"][0].bit_length(), 2048)
        self.assertGreater(keys["public"][1].bit_length(), 2048)
        self.assertGreater(keys["secret"][0].bit_length(), 2048)
        self.assertGreater(keys["secret"][1].bit_length(), 2048)

    def test_generate_keys_generates_keys_size_between_64_and_128_bits_when_class_attribute_key_size_is_64_bits(self):
        crypto = RSACrypto(64, self.primes_gen)
        keys = crypto.generate_keys()
        self.assertGreater(keys["public"][0].bit_length(), 64)
        self.assertGreater(keys["public"][1].bit_length(), 64)
        self.assertGreater(keys["secret"][0].bit_length(), 64)
        self.assertGreater(keys["secret"][1].bit_length(), 64)
        self.assertLessEqual(keys["public"][0].bit_length(), 128)
        self.assertLessEqual(keys["public"][1].bit_length(), 128)
        self.assertLessEqual(keys["secret"][0].bit_length(), 128)
        self.assertLessEqual(keys["secret"][1].bit_length(), 128)

    def test_encrypt_text_returns_message_which_does_not_equal_inputed_message(self):
        message = "{Åland!}'24/"
        self.assertNotEqual(self.crypto_256.encrypt_text(self.keys_256["public"], message),
                            message)

    def test_encrypt_text_returns_same_message_when_same_message_is_encrypted_with_same_key(self):
        self.assertEqual(self.crypto_256.encrypt_text(self.keys_256["public"], "Hyvää päivää!"),
                         self.crypto_256.encrypt_text(self.keys_256["public"], "Hyvää päivää!"))

    def test_encrypt_text_returns_different_message_when_different_message_is_encrypted_with_same_key(self):
        self.assertNotEqual(self.crypto_256.encrypt_text(self.keys_256["public"], "Päivää!"),
                            self.crypto_256.encrypt_text(self.keys_256["public"], "Ö"))

    def test_encrypt_text_returns_different_message_when_same_message_is_encrypted_with_different_keys(self):
        crypto = RSACrypto(64, self.primes_gen)
        keys = crypto.generate_keys()
        self.assertNotEqual(self.crypto_256.encrypt_text(self.keys_256["public"], "?"),
                            self.crypto_256.encrypt_text(keys["public"], "?"))

    def test_encrypt_text_returns_message_of_greater_size_than_public_keys(self):
        pass

    def test_decrypt_text_returns_original_message(self):
        message = "Katin kontit!"
        encrypted = self.crypto_256.encrypt_text(self.keys_256["public"], message)
        self.assertEqual(self.crypto_256.decrypt_text(self.keys_256["secret"], encrypted),
                         message)
