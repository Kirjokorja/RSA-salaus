import secrets
from algorithms.euclid import extended_euclid
from algorithms.primes import default_primes_gen
from exceptions import (rsa_exceptions as default_exceptions)


class RSACrypto:

    def __init__(self, key_size=2048, primes_gen=default_primes_gen, exceptions=default_exceptions):
        self._key_size = key_size
        self._primes_gen = primes_gen
        self._sys_rand = secrets.SystemRandom()
        self._exceptions = exceptions

    def _encrypt(self, p_key, m):
        if m >= p_key[1]:
            raise self._exceptions.MessageIsTooLong(
                "Salattava viesti on liian pitkä.")
        return pow(m, p_key[0], p_key[1])

    def _decrypt(self, s_key, cipher_m):
        return pow(cipher_m, s_key[0], s_key[1])

    def get_exceptions(self):
        return self._exceptions

    def generate_keys(self):
        p = self._primes_gen.get_random_prime(self._key_size)
        q = self._primes_gen.get_random_prime(self._key_size)
        n = p * q
        phi_n = (p - 1) * (q - 1)

        e = self._sys_rand.randint(2, phi_n - 1)
        euclid = extended_euclid(e, phi_n)
        while euclid[0] != 1:
            e = self._sys_rand.randint(2, phi_n - 1)
            euclid = extended_euclid(e, phi_n)
        d = (euclid[1] % phi_n + phi_n) % phi_n
        keys = {
            "public": (e, n),
            "secret": (d, n)
        }
        return keys

    def encrypt_text(self, p_key, text):
        encoded_m = int.from_bytes(text.encode('utf-8'))
        encrypted = self._encrypt(p_key, encoded_m)
        return encrypted

    def decrypt_text(self, s_key, encrypted):
        decrypted = self._decrypt(s_key, int(encrypted))
        decrypted_bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8)
        return decrypted_bytes.decode('utf-8')
