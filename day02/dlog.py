"""Day 2: Diffie-Hellman, then brute force vs baby-step giant-step."""

import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "day01"))
from modmath import inverse, power  # noqa: E402

# Safe primes p = 2q + 1 (q also prime), largest below 2^bits.
# Safe means p - 1 = 2q, so g is a generator iff g^2 != 1 and g^q != 1.
SAFE_PRIMES = {
    20: 1048343,
    24: 16776899,
    28: 268435019,
    30: 1073740439,
    32: 4294967087,
    36: 68719476599,
    40: 1099511627339,
}

# Brute force past this many bits takes hours in Python. Extrapolate instead.
BRUTE_MAX_BITS = 28


def find_generator(p):
    """Smallest generator of Z_p* for a safe prime p."""
    q = (p - 1) // 2
    for g in range(2, p):
        if power(g, 2, p) != 1 and power(g, q, p) != 1:
            return g


def dh(p, g, a, b):
    """Alice has a, Bob has b. Return (A, B, shared) where both sides agree."""
    A = power(g, a, p)
    B = power(g, b, p)
    alice = power(B, a, p)
    bob = power(A, b, p)
    assert alice == bob
    return A, B, alice


def brute_dlog(g, h, p):
    """Return (x, steps) with g^x == h mod p, trying x = 0, 1, 2, ..."""
    cur = 1
    for x in range(p - 1):
        if cur == h:
            return x, x + 1
        cur = cur * g % p


def bsgs(g, h, p):
    """Return (x, steps) with g^x == h mod p, in about 2*sqrt(p) steps."""
    m = math.isqrt(p - 1) + 1

    # Baby steps: memorize g^0 .. g^(m-1).
    table = {}
    cur = 1
    for j in range(m):
        table[cur] = j
        cur = cur * g % p

    # Giant steps: start at h, jump back m steps each round.
    back = inverse(power(g, m, p), p)
    cur = h
    for i in range(m):
        if cur in table:
            return i * m + table[cur], m + i + 1
        cur = cur * back % p


def race(bits):
    """Time both attacks on one prime. Return a row for the table."""
    # TODO: pick a secret x near the top of the range (worst case),
    #   h = g^x, time bsgs, time brute only if bits <= BRUTE_MAX_BITS


def plot(rows):
    """ASCII plot: log2(steps) against bits, one line per attack."""
    # TODO


if __name__ == "__main__":
    p = SAFE_PRIMES[20]
    g = find_generator(p)
    assert power(g, 2, p) != 1 and power(g, (p - 1) // 2, p) != 1

    A, B, shared = dh(p, g, 123456, 654321)
    assert shared == power(A, 654321, p) == power(B, 123456, p)

    x, _ = brute_dlog(g, power(g, 777, p), p)
    assert x == 777
    x, steps = bsgs(g, power(g, 999_999, p), p)
    assert x == 999_999 and steps < 3 * 1024, steps

    rows = [race(bits) for bits in sorted(SAFE_PRIMES)]
    plot(rows)
    # TODO: years for secp256k1 = 2^128 steps * (seconds per bsgs step) / seconds per year
    print("ok")
