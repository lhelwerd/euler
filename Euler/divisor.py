def proper_divisors(n):
    # Find proper divisors of `n`
    divisors = set()
    divisors.add(1)
    for i in range(2, n // 2):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)

    return divisors
