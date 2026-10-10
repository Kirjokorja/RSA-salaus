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
        # euclid = (gcd(e, phi_n), x, y)
        euclid = extended_euclid(e, phi_n)
        while euclid[0] != 1:
            e = self._sys_rand.randint(2, phi_n - 1)
            euclid = extended_euclid(e, phi_n)
        # e and phi_n are coprime, because 1 = gcd(e phi_n) = e*x +  phi_n*y.
        # euclid[1] = e^-1 mod phi_n (multiplicative inverse of  e, modulo n)
        # (euclid[1] % phi_n + phi_n) % phi_n, makes sure that d is positive,
        # since euclid[1] may be negative.
        # Taking the remainder keeps the d as a valid residue class.
        d = (euclid[1] % phi_n + phi_n) % phi_n
        keys = {
            "public": (e, n),
            "secret": (d, n)
        }
        return keys

    def encrypt(self, p_key, m):
        return pow(m, p_key[0], p_key[1])

    def decrypt(self, s_key, cipher_m):
        return pow(cipher_m, s_key[0], s_key[1])

    def encrypt_text(self, p_key, text):
        encrypted = ""
        for l in text:
            cipher_l = self.encrypt(p_key, ord(l))
            encrypted = encrypted + chr(cipher_l)
        return encrypted

    def decrypt_text(self, s_key, encrypted):
        decrypted = ""
        for cipher_l in encrypted:
            l = self.decrypt(s_key, ord(cipher_l))
            decrypted = decrypted + chr(l)
        return decrypted
