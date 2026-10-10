# bunker-builds

Daily builds for a 14-day crash course on post-quantum and AI threats to ECDSA, hash-based signatures and private post-quantum multisig. One folder per day. Plain Python, no dependencies, no `pow()` shortcuts.

## Day 1: modular arithmetic

`day01/modmath.py` builds the number theory every later day sits on.

| Function | What it does |
| --- | --- |
| `gcd(a, b)` | Euclid's algorithm. |
| `egcd(a, b)` | Extended Euclid: returns `(g, x, y)` with `a*x + b*y == g`. |
| `inverse(a, n)` | `a^-1 mod n` from the Bezout coefficient of `egcd`. Raises `ValueError` when `gcd(a, n) != 1`. |
| `power(base, exp, n)` | Square and multiply, so `exp` can be 10^18 and it still takes about 60 steps. |
| `generators(p)` | Every `g` whose powers cover all of `Z_p*`. |

What it shows:

- `7^-1 mod 26 = 15`, because `7 * 15 = 105 = 4 * 26 + 1`.
- `Z_101*` has 40 generators. That is `phi(100) = 40`, so the count checks out.
- Exponents live mod `p - 1`: by Fermat, `g^(p-1) = 1 mod p`, so the powers of `g` repeat every `p - 1` steps.

## Run

Needs Python 3.8 or newer.

```sh
python3 day01/modmath.py
```

## Test

The asserts at the bottom of each file are the tests. A clean run prints `ok`.
