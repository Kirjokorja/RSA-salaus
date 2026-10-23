import secrets
from algorithms import (eratosthenes_sieve as sieve)
from algorithms import miller_rabin


class PrimesGenerator:
    """Luokka vastaa alkulukujen luonnista.

        Attributes:
            _small_primes (List): lista pieniä alkulukuja
            _max_small_primes (int): luku määrittää mihin asti 
                generaattori laskee pieniä alkulukuja Eratostheneen seulalla
    """

    def __init__(self, max_small_primes=10000):
        """Alusta alkulukugeneraattori.

            Args:
                max_small_primes (int): luku määrittää mihin asti 
                generaattori laskee pieniä alkulukuja Eratostheneen seulalla
        """
        self._max_small_primes = max_small_primes
        self._small_primes = sieve.get_primes_list(self._max_small_primes)

    def is_prime(self, n):
        """Metodi selvittää onko annettu luku alkuluku käyttäen
        Eratostheneen seulaa ja tarvittaessa Miller-Rabin-algoritmiä.

        Args:
            n (unsigned long long): luku, jonka alkulukuisuutta selvitetään

        Returns:
            bool: palauttaa True, jos luku on todennäköisesti alkuluku ja
            False, jos se ei ole alkuluku
        """
        if n < 2:
            return False

        for p in self._small_primes:
            if n == p:
                return True
            if n % p == 0:
                return False
        return miller_rabin.is_prime(self._max_small_primes + 1, n)

    def get_random_prime(self, bit_size):
        """Metodi tuottaa annetun kokoisen alkuluvun käyttäen
                Eratostheneen seulaa ja tarvittaessa Miller-Rabin-algoritmiä.

            Args:
                bit_size (int): alkuluvun suuruusluokka

            Returns:
                p (unsigned long long): alkuluku
        """
        p = secrets.randbits(bit_size)
        while not self.is_prime(p):
            p = secrets.randbits(bit_size)
        return p


default_primes_gen = PrimesGenerator(10000)
