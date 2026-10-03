from algorithms.primes import PrimesGenerator


def main():
    prime_gen = PrimesGenerator(1000)
    bit_size = input("Anna alkulukujen suuruusluokka bitteinä: ")
    print(prime_gen.get_two_random_primes(int(bit_size)))


if __name__ == "__main__":
    main()
