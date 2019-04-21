from decimal import Decimal

def expand_sqrt(n):
    # Generate the unique parameters of the continued fraction expansion of
    # the square root of `n`, stopping when an existing parameter is found.
    s = Decimal(n).sqrt()
    if s % 1 != 0:
        x = s
        f = int(s)
        P = set()
        # Numerator/denominator start values like sqrt(2) expansion #57
        v = Decimal('0')
        w = Decimal('1')
        while (v, w) not in P:
            # Not yet found, so add to the known expansions
            P.add((v, w))
            if v != 0:
                yield (v, w)

            # Calculate next expansion's paramters
            # First iteration: v0 = int(s), w0 = n - int(s)**2 (n = s**2)
            #  --> e.g. for s = sqrt(23) we get v0 = 4, w0 = 23 - 16 = 7
            # v_i = int((v_{i-1} + s) /  w_{i-1}) * w_{i-1} - v{i-1},
            # w_i = int((n - v_i ** 2) / w_{i-1})
            #  --> e.g. for s = sqrt(23) we get
            #  v1 = int((4+4...)/7) * 7 - 4 = 3, w1 = (23 - 3**2) / 7 = 2
            v = f * w - v
            w = (n - v ** 2) // w
            f = (v + s) // w
