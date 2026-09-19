import secrets

def find_odd(n):
    if n < 2:
        return -1
    odd = n - 1
    while odd % 2 == 0:
        odd //= 2
    return odd

def is_composite(n, witness):
    odd = find_odd(n)
    remainder = pow(witness, odd, mod=n)
    if remainder == 1 or remainder == n - 1:
        return False
    while odd != n - 1:
        remainder = remainder**2 % n
        odd *= 2
        if remainder == 1:
            return True
    if remainder != 1:
        return True
    return False

def is_prime(n):
    if n == 1:
        return False
    binary = bin(n)[2:]
    num_witnesses = len(binary)-1
    for i in range(1, num_witnesses):
        witness = secrets.choice(range(1, n-1))
        if is_composite(n, witness):
            return False
    return True
