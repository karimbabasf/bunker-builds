"""Day 2: Diffie-Hellman, then brute force vs baby-step giant-step."""

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
    # TODO


def dh(p, g, a, b):
    """Alice has a, Bob has b. Return (A, B, shared) where both sides agree."""
    # TODO: A = g^a, B = g^b, shared from both sides, assert they match


def brute_dlog(g, h, p):
    """Return (x, steps) with g^x == h mod p, trying x = 0, 1, 2, ..."""
    # TODO


def bsgs(g, h, p):
    """Return (x, steps) with g^x == h mod p, in about 2*sqrt(p) steps."""
    # TODO: m = ceil(sqrt(p - 1))
    #   baby steps: table {g^j: j} for j in 0..m-1
    #   giant steps: gamma = h, multiply by g^-m each round, look it up


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
