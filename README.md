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

## Day 2: Diffie-Hellman and the discrete log race

`day02/dlog.py` builds key exchange, then attacks it two ways.

| Function | What it does |
| --- | --- |
| `find_generator(p)` | Smallest generator of `Z_p*`. For a safe prime `p = 2q + 1`, `g` works iff `g^2 != 1` and `g^q != 1`. |
| `dh(p, g, a, b)` | Alice sends `g^a`, Bob sends `g^b`, both reach `g^(ab)` without sending it. |
| `brute_dlog(g, h, p)` | Tries `x = 0, 1, 2, ...` until `g^x == h`. About `p` steps. |
| `bsgs(g, h, p)` | Baby-step giant-step: memorize `m = sqrt(p)` powers, jump back from `h` by `g^-m`. About `2 * sqrt(p)` steps. |
| `race(bits)` | Times both on a worst-case secret. Brute force past 28 bits is extrapolated. |

What it shows:

- `dh(23, 5, 6, 15)` gives public keys 8 and 19 and the shared secret 2.
- At 40 bits, brute force needs 1.1 trillion steps (about 7 hours here). BSGS needs 2.1 million and finishes in 0.23 s.
- Each extra bit doubles brute force but only multiplies BSGS by about 1.4.
- One BSGS step costs about 108 ns on this laptop, so secp256k1 (2^128 steps) would take about 1.1 x 10^24 years.

## Run

Needs Python 3.8 or newer.

```sh
python3 day01/modmath.py
python3 day02/dlog.py
```

## Test

The asserts at the bottom of each file are the tests. A clean run prints `ok`.
