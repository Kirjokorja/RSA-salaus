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
    previous = pow(witness, odd, mod=n)
    while odd != n - 1:
        current = previous**2 % n
        odd *= 2
        if current == 1 and previous != 1 and previous != n - 1:
            return True
        previous = current
    if previous != 1:
        return True
    return False


def is_prime(n):
    if n == 1:
        return False
    i = 0
    while i < n.bit_lenght():
        witness = secrets.choice(range(2, n-2))
        if is_composite(n, witness):
            return False
        i += 1
    return True
