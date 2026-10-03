import secrets


def is_composite(n, witness):
    """Funktio selvittää onko annettu luku yhdistetty luku.

    Args:
        n (unsigned long long): luku, jonka yhdistyneisyyttä selvitetään
        witness (unsigned long long): luku, jota käytetään todistamaan
        testattavan luvun yhdistyneisyys

    Returns:
        bool: palauttaa True, jos luku on yhdistetty luku ja 
        False, jos se todennäköisesti ei ole
    """
    odd = n - 1
    while odd % 2 == 0:
        odd //= 2
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


def is_prime(lower_bound, n):
    """Funktio selvittää onko annettu luku alkuluku käyttäen Miller-Rabin-algoritmiä.

    Args:
        lower_bound (int): luku, jota pienempiä ei hyväksytä satunnaiseksi koetinluvuksi
        n (unsigned long long): luku, jonka alkulukuisuutta selvitetään 

    Returns:
        bool: palauttaa True, jos luku on todennäköisesti alkuluku ja 
        False, jos se ei ole alkuluku
    """
    if n < 2:
        return False
    if n < 4:
        return True
    if lower_bound > n-2:
        lower_bound = 2
    k = 0
    sys_rand = secrets.SystemRandom()
    while k < n.bit_length():
        witness = sys_rand.randint(lower_bound, n-2)
        if is_composite(n, witness):
            return False
        k += 1
    return True
