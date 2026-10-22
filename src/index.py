from algorithms.primes import PrimesGenerator
from crypto.rsa import RSACrypto
from ui.ui import UI


def main():
    prime_gen = PrimesGenerator(10000)
    crypto = RSACrypto(2048, prime_gen)
    ui = UI(crypto)

    ui.start()


if __name__ == "__main__":
    main()
