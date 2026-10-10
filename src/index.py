from algorithms.primes import PrimesGenerator
from crypto.rsa import RSACrypto


def main():
    prime_gen = PrimesGenerator(10000)
    crypto = RSACrypto(prime_gen)
    keys = crypto.generate_keys()
    print(f"Julkinen: {keys["public"]}")
    print(f"Salainen: {keys["secret"]}")


if __name__ == "__main__":
    main()
