from builtins import range

def proper_divisors(n, add=1):
    # Find proper divisors of `n`
    divisors = set()
    divisors.add(add)
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return divisors
