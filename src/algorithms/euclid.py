
def extended_euclid(a, mod):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while mod != 0:
        q = a // mod
        a, mod = mod, a - q * mod
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return (a, x0, y0)
