from algorithms import (eratosthenes_sieve as sieve)

def main():
    upper_bound = input("Anna ylin luku alkulukulistalle: ")
    print(sieve.get_primes_list(int(upper_bound)))

if __name__ == "__main__":
    main()