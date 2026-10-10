import secrets
from algorithms.euclid import extended_euclid

class RSACrypto:

    def __init__(self, prime_gen):
        self._prime_gen = prime_gen
        self._sys_rand = secrets.SystemRandom()

    def generate_keys(self):
        p = self._prime_gen.get_random_prime(2048)
        q = self._prime_gen.get_random_prime(2048)
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
