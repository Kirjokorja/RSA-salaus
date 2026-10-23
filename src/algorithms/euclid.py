
def extended_euclid(a, b):
    """Funktio selvittää parametrien a ja b suurimman yhteisen tekijän.

        Args:
            a (unsigned long long): ensimmäinen kokonaisluvuista,
                                    joiden suurinta yhteistä tekijää etsitään 
            b (unsigned long long): toinen kokonaisluvuista,
                                    joiden suurinta yhteistä tekijää etsitään

        Returns:
            monikko (unsigned long long, long long, long long): 
                Monikon ensimmäinen jäsen on a:n ja b:n suurin yhteinen tekijä ja
                loput kaksi ovat Bézout’n yhtälön (syt(a,b) = ax + by) kertoimia.
    """
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return (a, x0, y0)
