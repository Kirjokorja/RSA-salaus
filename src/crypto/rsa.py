import secrets
from algorithms.euclid import extended_euclid
from algorithms.primes import default_primes_gen
from exceptions import (rsa_exceptions as default_exceptions)


class RSACrypto:
    """Luokka toteuttaa RSA-salauksen.

        Attributes:
            _key_siz (int): haluttu kokoluokka bitteinä avainten alkuluvuille
            _primes_gen (PrimesGenerator): alkulukujen luonnista vastaava olio
            _sys_rand (SystemRandom): käyttöjärjestelmän satunnaislukugeneraattori
            _exceptions: virheluokat
    """

    def __init__(self, key_size=2048, primes_gen=default_primes_gen, exceptions=default_exceptions):
        """Alusta RSA-salausolio.

            Args:
                key_size (int): haluttu kokoluokka bitteinä avainten alkuluvuille
                primes_gen (PrimesGenerator): alkulukujen luonnista vastaava olio
                exceptions: virheluokat
        """
        self._key_size = key_size
        self._primes_gen = primes_gen
        self._sys_rand = secrets.SystemRandom()
        self._exceptions = exceptions

    def _encrypt(self, p_key, m):
        if m >= p_key[1]:
            raise self._exceptions.MessageIsTooLong(
                "Salattava viesti on liian pitkä.")
        return pow(m, p_key[0], p_key[1])

    def _decrypt(self, s_key, m):
        if m >= s_key[1]:
            raise self._exceptions.MessageIsTooLong(
                "Purettava viesti on liian pitkä.")
        return pow(m, s_key[0], s_key[1])

    def get_exceptions(self):
        """Antaa luokan virheilmoitusluokat.

            Returns:
                _exceptions: virheilmoitusluokat
        """
        return self._exceptions

    def generate_keys(self):
        """Luo salausavainparit key_size attribuutin määrittelemän alkulukukoon mukaan. 
            Metodi käyttää laajennettua Eukleideen algoritmiä suurimman yhteisen tekijän 
            löytämiseen sekä kertovan käänteisluvun laskemiseen.

            Returns:
                keys (Dictonary): hajautustaulu, jonka sisäälä julkisen avaimen lukuparit ovat
                                    "public" nimisen avaimen alla monikkona
                                    ja yksityisen avaimen lukuparit ovat
                                    "secret" nimisen avaimen alla omana monikkonaan
        """
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
        """Luo uuden hankkeen.

            Args:
                p_key (Tuple): julkinen salausavain
                text (string): salattava viesti

            Raises:
                MessageIsTooLong: virhe, joka syntyy liian pitkästä salattavasta viestistä

            Returns:
                encrypted (unsigned long long): kokonaisluku, joka esittää salattua viestiä
        """
        encoded_m = int.from_bytes(text.encode('utf-8'))
        encrypted = self._encrypt(p_key, encoded_m)
        return encrypted

    def decrypt_text(self, s_key, encrypted):
        """Luo uuden hankkeen.

            Args:
                s_key (Tuple): yksityinen salausavain
                encrypted (string): salattu viesti kokonaislukua esittävänä merkkijonona

            Raises:
                MessageIsTooLong: virhe, joka syntyy liian pitkästä salatusta viestistä

            Returns:
               merkkijono (string): salauksesta purettu viesti
        """
        decrypted = self._decrypt(s_key, int(encrypted))
        decrypted_bytes = decrypted.to_bytes((decrypted.bit_length() + 7) // 8)
        return decrypted_bytes.decode('utf-8')
