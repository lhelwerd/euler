"""
Module for modular arithmetic.
"""

def inverse(value: int, modulo: int) -> int:
    """
    Calculate the multiplicative modular inverse `t` of value `a`, modulo `n`.
    So `a * t = 1 mod n`

    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    """

    inverse_t = 0
    new_inverse = 1
    remainder = modulo
    new_remainder = value

    while new_remainder != 0:
        quotient = remainder // new_remainder
        inverse_t, new_inverse = new_inverse, inverse_t - quotient * new_inverse
        remainder, new_remainder = new_remainder, \
            remainder - quotient * new_remainder

    if remainder > 1:
        return 0
    if inverse_t < 0:
        inverse_t += modulo

    return inverse_t
