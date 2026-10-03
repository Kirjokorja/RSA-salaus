import secrets
from algorithms import (eratosthenes_sieve as sieve)
from algorithms import miller_rabin


class PrimesGenerator:
    """Luokka vastaa alkulukujen luonnista.

        Attributes:
            _small_primes (List(int)): lista pieniä alkulukuja
    """

    def __init__(self, max_small_primes):
        """Alusta alkulukugeneraattori.

            Args:
                max_small_primes (int): luku määrittää mihin asti 
                generaattori laskee pieniä alkulukuja Eratostheneen seulalla
        """
        self._small_primes = sieve.get_primes_list(max_small_primes)

    def is_prime(self, n):
        """Funktio selvittää onko annettu luku alkuluku käyttäen
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
            if n % p == 0:
                return False
        if miller_rabin.is_prime(1001, n):
            return True
        return False

    def get_two_random_primes(self, bit_size):
        """Funktio tuottaa kaksi annetun kokoista eri alkulukua käyttäen
        Eratostheneen seulaa ja tarvittaessa Miller-Rabin-algoritmiä.

        Args:
            bit_size (int): alkulukujen suuruusluokka

        Returns:
            Set(unsigned long long): alkulukupari
        """
        p = secrets.randbits(bit_size)
        tried = set()
        while p in tried or not self.is_prime(p):
            tried.add(p)
            p = secrets.randbits(bit_size)
        tried.add(p)
        q = secrets.randbits(bit_size)
        while q in tried or not self.is_prime(q):
            tried.add(q)
            q = secrets.randbits(bit_size)
        return (p, q)
