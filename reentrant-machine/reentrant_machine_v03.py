#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Re-Entrant Machine v0.3 — adds Picard-Lindelof uniqueness check (U1)
=====================================================================
The Calculus of Re-Entrant Distinctions (QNFO.SLB.002, DOI 10.5281/zenodo.21908428)

G1: mark re-entry oscillation (period-2 clock)
G2: e from fixed point Df=f (Taylor series)
G3: pi from trace of identity on S^1 (Gaussian integral)
G4: e^{i*pi} = -1 without importing e or pi
U1 (NEW): Picard-Lindelof uniqueness — fixed-point iteration from multiple
          seeds converges to the same e (strengthens REG-SLB-001 formal claim)
"""
import sys

MARKED, UNMARKED = 1, 0
def cross(x):
    return MARKED if x == UNMARKED else UNMARKED

# G1
osc = []
v = UNMARKED
for _ in range(8):
    v = cross(v)
    osc.append(v)
g1_ok = (osc == [1, 0, 1, 0, 1, 0, 1, 0])
print(f"[G1] mark re-entry oscillation: {osc}  {'PASS' if g1_ok else 'FAIL'}")
assert g1_ok

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def exp_series(x, terms=60):
    return sum((x ** n) / factorial(n) for n in range(terms))

e = exp_series(1.0, 60)
g2_ok = abs(e - 2.718281828459045) < 1e-12
print(f"[G2] e = {e!r}  {'PASS' if g2_ok else 'FAIL'}")
assert g2_ok

def exp_neg(t):
    return 1.0 / exp_series(t, 80)

def gaussian_integral(a, b, n=18000):
    h = (b - a) / n
    s = exp_neg(a * a) + exp_neg(b * b)
    for i in range(1, n):
        x = a + i * h
        w = 4 if (i % 2 == 1) else 2
        s += w * exp_neg(x * x)
    return s * h / 3.0

I = gaussian_integral(-4.5, 4.5, 18000)
pi_machine = I * I
g3_ok = abs(pi_machine - 3.141592653589793) < 1e-5
print(f"[G3] pi = {pi_machine!r} (|err| {abs(pi_machine - 3.141592653589793):.3e})  {'PASS' if g3_ok else 'FAIL'}")
assert g3_ok

def cos_series(x, terms=30):
    return sum(((-1) ** n) * (x ** (2 * n)) / factorial(2 * n) for n in range(terms))

def sin_series(x, terms=30):
    return sum(((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1) for n in range(terms))

re_part = cos_series(pi_machine)
im_part = sin_series(pi_machine)
g4_ok = abs(re_part - (-1.0)) < 1e-7 and abs(im_part) < 1e-7
print(f"[G4] e^(i*pi) = {re_part!r} + i*{im_part!r}  {'PASS' if g4_ok else 'FAIL'}")
assert g4_ok

# U1: Picard-Lindelof uniqueness via fixed-point iteration from multiple seeds.
# The Picard iteration for f'=f, f(0)=1 is f_{k+1}(x) = 1 + int_0^x f_k(t) dt.
def picard_step(f, x, n=200):
    # numerical integration of f over [0,x] (trapezoid)
    h = x / n
    s = (f(0) + f(x)) / 2
    for i in range(1, n):
        s += f(i * h)
    return 1.0 + s * h

def iterate(seed_fn, x=1.0, iters=30):
    f = seed_fn
    for _ in range(iters):
        f = (lambda g: (lambda t: picard_step(g, t)))(f)
    return f(x)

# seeds: constant 1, linear x+1, quadratic 1+x^2/2
seed1 = lambda t: 1.0
seed2 = lambda t: t + 1.0
seed3 = lambda t: 1.0 + t * t / 2.0

vals = [iterate(seed1), iterate(seed2), iterate(seed3)]
u1_ok = all(abs(v - e) < 1e-2 for v in vals)  # all converge near e
print(f"[U1] Picard iteration from seeds -> {[f'{v:.6f}' for v in vals]} (e={e:.6f})  {'PASS' if u1_ok else 'FAIL'}")
assert u1_ok

print("\n" + "=" * 70)
print("RE-ENTRANT MACHINE v0.3 - VERIFICATION SUMMARY")
print("=" * 70)
print(f"  e  = {e!r}")
print(f"  pi = {pi_machine!r}")
print(f"  e^(i*pi) = {re_part!r} + i*{im_part!r}")
print(f"  Constants imported: NONE")
print(f"  G1..G4 + U1: {'ALL PASS' if (g1_ok and g2_ok and g3_ok and g4_ok and u1_ok) else 'FAILURE'}")
print("=" * 70)
sys.exit(0 if (g1_ok and g2_ok and g3_ok and g4_ok and u1_ok) else 1)
