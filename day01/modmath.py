# Bunker Day 1: modular arithmetic by hand. No AI.


def egcd(a, b):
    """Return (g, x, y) with a*x + b*y == g == gcd(a, b)."""
    raise NotImplementedError


def inverse(a, n):
    """Return a^-1 mod n. Raise ValueError if gcd(a, n) != 1."""
    raise NotImplementedError


def power(base, exp, n):
    """Square and multiply. No pow()."""
    raise NotImplementedError


def generators(p):
    """Every g in Z_p* whose powers hit all p - 1 elements."""
    raise NotImplementedError


if __name__ == "__main__":
    assert egcd(240, 46)[0] == 2
    assert inverse(3, 7) == 5
    assert power(3, 200, 101) == pow(3, 200, 101)
    gens = generators(101)
    assert len(gens) == 40, len(gens)
    print("ok", gens[:5])
