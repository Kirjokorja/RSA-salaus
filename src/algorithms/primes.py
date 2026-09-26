import secrets
from algorithms import (eratosthenes_sieve as sieve)
from algorithms import miller_rabin


def is_prime(n):
    if n < 2:
        return False
    small_primes = sieve.get_primes_list(1000)
    for p in small_primes:
        if n % p == 0:
            return False
    if miller_rabin.is_prime(1001, n):
        return True
    return False


def get_two_random_primes(bit_size):
    p = secrets.randbits(bit_size)
    tried = set()
    while p in tried or not is_prime(p):
        tried.add(p)
        p = secrets.randbits(bit_size)
    tried.add(p)
    q = secrets.randbits(bit_size)
    while q in tried or not is_prime(q):
        tried.add(q)
        q = secrets.randbits(bit_size)
    return (p, q)
