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
    while odd != n - 1:
        y = remainder**2 % n
        odd *= 2
        if y == 1 and remainder != 1 and remainder != n-1:
            return True
        remainder = y
    if remainder != 1:
        return True
    return False


def is_prime(n):
    if n == 1:
        return False
    for i in range(1, n.bit_lenght()):
        witness = secrets.choice(range(2, n-2))
        if is_composite(n, witness):
            return False
    return True
