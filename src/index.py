from algorithms import primes


def main():
    bit_size = input("Anna alkulukujen suuruusluokka bitteinä: ")
    print(primes.get_two_random_primes(int(bit_size)))


if __name__ == "__main__":
    main()
