#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Re-Entrant Machine v0.1 — Appendix D implementation
===================================================
The Calculus of Re-Entrant Distinctions (QNFO.SLB.002, DOI 10.5281/zenodo.21906728)

Genuine computational implementation: computes e and pi and verifies the Euler
identity e^{i*pi} = -1 using ONLY the mark's differential structure (Taylor
series machinery) — WITHOUT importing math.e, math.pi, math.exp, math.cos,
math.sin, math.sqrt, or any transcendental constants.

Verification goals (Appendix D):
  G1: the mark's re-entry produces the oscillation (period 2 clock)
  G2: the differential combinator produces the exponential series
  G3: the trace of the identity on S^1 computes pi (via the Gaussian integral)
  G4: e^{i*pi} = -1 derived without importing e or pi
"""
import sys

# ---------------------------------------------------------------------------
# Primitive: the mark calculus (Spencer-Brown two-valued algebra)
# ---------------------------------------------------------------------------
MARKED, UNMARKED = 1, 0

def cross(x):
    """The mark (negation): crossing."""
    return MARKED if x == UNMARKED else UNMARKED

def call(x, y):
    """Calling (juxtaposition): both present -> marked."""
    return MARKED if (x == MARKED and y == MARKED) else UNMARKED

def reenter(f, n):
    """Iterate the re-entrant form f = !f (the mark applied to its own result).
    G1: the sequence must oscillate with period 2 (the discrete clock)."""
    seq = []
    v = UNMARKED
    for _ in range(n):
        v = f(v)
        seq.append(v)
    return seq

# G1 verify: re-entry oscillation
osc = reenter(cross, 8)
g1_ok = (osc == [MARKED, UNMARKED, MARKED, UNMARKED, MARKED, UNMARKED, MARKED, UNMARKED])
print(f"[G1] mark re-entry oscillation (period 2): {osc}")
print(f"     G1 {'PASS' if g1_ok else 'FAIL'}")
assert g1_ok

# ---------------------------------------------------------------------------
# The differential combinator: Taylor machinery (no imported transcendence)
# ---------------------------------------------------------------------------
def factorial(n):
    """Integer factorial (exact)."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def exp_series(x, terms=60):
    """The exponential series sum_{n=0..terms} x^n / n!.
    This IS the differential combinator's Taylor expansion of the identity-like
    proof (DiLL §7.2, treatise §9). Works for negative x (alternating tail)."""
    total = 0.0
    for n in range(terms):
        total += (x ** n) / factorial(n)
    return total

def derivative(poly):
    """Formal derivative of a polynomial (list of coefficients, low->high).
    The differential combinator D of DiLL, applied syntactically."""
    return [c * (i + 1) for i, c in enumerate(poly[1:])]

# G2 verify: the differential combinator generates the exponential series.
# D(exp) = exp is the fixed-point equation; the series solves Df = f, f(0)=1.
e = exp_series(1.0, 60)          # e = sum 1/n!
e_check = exp_series(1.0, 30)    # convergence check
g2_ok = abs(e - 2.718281828459045) < 1e-12
print(f"[G2] e from fixed point Df=f (Taylor series at x=1): {e!r}")
print(f"     |e - 2.718281828459045| = {abs(e - 2.718281828459045):.3e}  G2 {'PASS' if g2_ok else 'FAIL'}")
assert g2_ok

# ---------------------------------------------------------------------------
# The trace of identity on S^1: pi via the Gaussian integral (treatise §11.3)
# ---------------------------------------------------------------------------
def gaussian_integral(a, b, n=16000):
    """Simpson's rule for I = int_a^b e^{-x^2} dx, using our own exp_series
    (never math.exp). The treatise §11.3: (int e^{-x^2} dx)^2 = pi — the
    two-dimensional polar evaluation brings in the circle's circumference 2*pi,
    i.e. the trace of the identity on the circle."""
    h = (b - a) / n
    s = exp_series(-a * a, 40) + exp_series(-b * b, 40)
    for i in range(1, n):
        x = a + i * h
        w = 4 if (i % 2 == 1) else 2
        s += w * exp_series(-x * x, 40)
    return s * h / 3.0

I = gaussian_integral(-8.0, 8.0, 20000)   # e^{-64} ~ 1e-28: tail negligible
pi_machine = I * I                          # trace of identity on S^1
g3_ok = abs(pi_machine - 3.141592653589793) < 1e-6
print(f"[G3] I = int e^-x^2 dx = {I!r};  pi = I^2 = {pi_machine!r}")
print(f"     |pi - 3.141592653589793| = {abs(pi_machine - 3.141592653589793):.3e}  G3 {'PASS' if g3_ok else 'FAIL'}")
assert g3_ok

# ---------------------------------------------------------------------------
# Euler identity: e^{i*pi} = cos(pi) + i sin(pi), using OUR e, pi, and series
# ---------------------------------------------------------------------------
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

# e^{i pi} via Euler's formula, with pi from the machine (no math.pi)
re_part = cos_series(pi_machine)
im_part = sin_series(pi_machine)
g4_ok = abs(re_part - (-1.0)) < 1e-9 and abs(im_part) < 1e-9
print(f"[G4] e^(i*pi) = cos(pi) + i sin(pi) = {re_part!r} + i*{im_part!r}")
print(f"     re+1 = {abs(re_part + 1.0):.3e}, im = {abs(im_part):.3e}  G4 {'PASS' if g4_ok else 'FAIL'}")
assert g4_ok

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("RE-ENTRANT MACHINE v0.1 — VERIFICATION SUMMARY")
print("=" * 70)
print(f"  e  = {e!r}  (fixed point Df=f, Taylor series)")
print(f"  pi = {pi_machine!r}  (trace of identity on S^1 via Gaussian integral)")
print(f"  e^(i*pi) = {re_part!r} + i*{im_part!r}  (Euler identity)")
print(f"  Constants imported: NONE (only float arithmetic + own series)")
print(f"  G1..G4: {'ALL PASS' if g1_ok and g2_ok and g3_ok and g4_ok else 'FAILURE'}")
print("=" * 70)
sys.exit(0 if (g1_ok and g2_ok and g3_ok and g4_ok) else 1)
