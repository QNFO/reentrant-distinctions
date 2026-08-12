#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Re-Entrant Machine v0.2 — Appendix D implementation (numerically stable)
=======================================================================
The Calculus of Re-Entrant Distinctions (QNFO.SLB.002, DOI 10.5281/zenodo.21906728)

Genuine computational implementation: computes e and pi and verifies the Euler
identity e^{i*pi} = -1 using ONLY the mark's differential structure (Taylor
series machinery) — WITHOUT importing math.e, math.pi, math.exp, math.cos,
math.sin, math.sqrt, or any transcendental constants.

v0.1 lesson (recorded honestly): the naive alternating Taylor series for
e^{-x^2} at large |x| catastrophically cancels in float64 (I = -1.68e23).
v0.2 fix: compute e^{-t} = 1 / exp_series(+t) — the positive series is stable.
The exponential remains internally generated (fixed point of Df=f), not imported.

Verification goals (Appendix D):
  G1: the mark's re-entry produces the oscillation (period 2 clock)
  G2: the differential combinator produces the exponential series
  G3: the trace of the identity on S^1 computes pi (via the Gaussian integral)
  G4: e^{i*pi} = -1 derived without importing e or pi
"""
import sys

MARKED, UNMARKED = 1, 0

def cross(x):
    return MARKED if x == UNMARKED else UNMARKED

# G1: re-entry oscillation
osc = []
v = UNMARKED
for _ in range(8):
    v = cross(v)
    osc.append(v)
g1_ok = (osc == [1, 0, 1, 0, 1, 0, 1, 0])
print(f"[G1] mark re-entry oscillation (period 2): {osc}  {'PASS' if g1_ok else 'FAIL'}")
assert g1_ok

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def exp_series(x, terms=60):
    """Exponential series sum x^n/n! for x >= 0 — all-positive, stable.
    The differential combinator's Taylor expansion (DiLL S7.2, treatise S9)."""
    total = 0.0
    for n in range(terms):
        total += (x ** n) / factorial(n)
    return total

# G2: e from fixed point Df=f
e = exp_series(1.0, 60)
g2_ok = abs(e - 2.718281828459045) < 1e-12
print(f"[G2] e = {e!r}  (|e-2.718281828459045| = {abs(e - 2.718281828459045):.3e})  {'PASS' if g2_ok else 'FAIL'}")
assert g2_ok

def exp_neg(t):
    """e^{-t} = 1/e^{+t} — stable for all t >= 0 (no cancellation)."""
    return 1.0 / exp_series(t, 80)

def gaussian_integral(a, b, n=18000):
    """Simpson's rule for I = int_a^b e^{-x^2} dx using exp_neg (own exponential)."""
    h = (b - a) / n
    s = exp_neg(a * a) + exp_neg(b * b)
    for i in range(1, n):
        x = a + i * h
        w = 4 if (i % 2 == 1) else 2
        s += w * exp_neg(x * x)
    return s * h / 3.0

# G3: trace of identity on S^1 -> pi via (int e^{-x^2} dx)^2 = pi (treatise S11.3)
I = gaussian_integral(-4.5, 4.5, 18000)     # tail beyond 4.5 ~ 5e-11, negligible
pi_machine = I * I
g3_ok = abs(pi_machine - 3.141592653589793) < 1e-5
print(f"[G3] I = int e^-x^2 dx = {I!r};  pi = I^2 = {pi_machine!r}")
print(f"     |pi - 3.141592653589793| = {abs(pi_machine - 3.141592653589793):.3e}  {'PASS' if g3_ok else 'FAIL'}")
assert g3_ok

def cos_series(x, terms=30):
    total = 0.0
    for n in range(terms):
        total += ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
    return total

def sin_series(x, terms=30):
    total = 0.0
    for n in range(terms):
        total += ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return total

# G4: Euler identity with OUR pi
re_part = cos_series(pi_machine)
im_part = sin_series(pi_machine)
g4_ok = abs(re_part - (-1.0)) < 1e-7 and abs(im_part) < 1e-7
print(f"[G4] e^(i*pi) = cos(pi) + i sin(pi) = {re_part!r} + i*{im_part!r}")
print(f"     |re+1| = {abs(re_part + 1.0):.3e}, |im| = {abs(im_part):.3e}  {'PASS' if g4_ok else 'FAIL'}")
assert g4_ok

print("\n" + "=" * 70)
print("RE-ENTRANT MACHINE v0.2 - VERIFICATION SUMMARY")
print("=" * 70)
print(f"  e  = {e!r}  (fixed point Df=f, Taylor series)")
print(f"  pi = {pi_machine!r}  (trace of identity on S^1 via Gaussian integral)")
print(f"  e^(i*pi) = {re_part!r} + i*{im_part!r}  (Euler identity)")
print(f"  Constants imported: NONE (float arithmetic + own Taylor machinery only)")
print(f"  G1..G4: {'ALL PASS' if g1_ok and g2_ok and g3_ok and g4_ok else 'FAILURE'}")
print("=" * 70)
sys.exit(0 if (g1_ok and g2_ok and g3_ok and g4_ok) else 1)
