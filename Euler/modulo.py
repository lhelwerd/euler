# Helper functions for modular arithmetic

def inverse(a, n):
    # Calculate the multiplicative modular inverse t of a, modulo n
    # So at = 1 mod n
    # https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    t = 0
    t1 = 1
    r = n
    r1 = a

    while r1 != 0:
        q = r // r1
        t, t1 = t1, t - q * t1
        r, r1 = r1, r - q * r1

    if r > 1:
        return 0
    if t < 0:
        t += n

    return t
