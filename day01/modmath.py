"""Day 1: modular arithmetic and the group Z_p*."""


def gcd(a, b):
    """Euclid: gcd(a, b) == gcd(b, a mod b)."""
    while b != 0:
        a, b = b, a % b
    return a


def egcd(a, b):
    """Return (g, x, y) with a*x + b*y == g == gcd(a, b)."""
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0


def inverse(a, n):
    """Return a^-1 mod n. Raise ValueError if gcd(a, n) != 1."""
    g, x, _ = egcd(a % n, n)
    if g != 1:
        raise ValueError(f"{a} has no inverse mod {n}")
    return x % n


def power(base, exp, n):
    """Square and multiply: O(log exp) multiplications. No pow()."""
    result = 1
    base %= n
    while exp > 0:
        if exp & 1:
            result = (result * base) % n
        base = (base * base) % n
        exp >>= 1
    return result


def generators(p):
    """Every g in Z_p* whose powers hit all p - 1 elements."""
    gens = []
    for g in range(1, p):
        seen = {power(g, k, p) for k in range(1, p)}
        if len(seen) == p - 1:
            gens.append(g)
    return gens


if __name__ == "__main__":
    assert gcd(240, 46) == 2
    g, x, y = egcd(240, 46)
    assert g == 2 and 240 * x + 46 * y == 2
    assert inverse(3, 7) == 5
    assert inverse(7, 26) == 15
    assert power(3, 200, 101) == pow(3, 200, 101)
    assert power(2, 10**18, 101) == pow(2, 10**18, 101)
    gens = generators(101)
    assert len(gens) == 40, len(gens)
    print("ok, 40 generators of Z_101*, first five:", gens[:5])
