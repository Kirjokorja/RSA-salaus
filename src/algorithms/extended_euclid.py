
def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)
    (d, x, y) = extended_euclid(a, a % b)
    return (d, y, x - a // b * y)
