#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
U1 FIX — efficient pointwise Picard iteration for the Re-Entrant Machine v0.3.
The v0.3 nested-lambda U1 timed out (closure tower is exponential in depth).
This replaces U1 with standard discretized Picard: f_{k+1}(x) = 1 + int_0^x f_k,
evaluated on a grid, O(iters * n) per seed. Keeps G1-G4 identical.
"""
import sys

MARKED, UNMARKED = 1, 0
def cross(x):
    return MARKED if x == UNMARKED else UNMARKED

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

# ---- U1 (FIXED): efficient pointwise Picard iteration on a grid ----
# Solve f'=f, f(0)=1 by Picard: f_{k+1}(x) = 1 + int_0^x f_k(t) dt.
# Discretize x on [0, X] with n steps; trapezoid integration.
def picard_grid(seed_vals, X=1.0, n=400, iters=40):
    h = X / n
    grid = [i * h for i in range(n + 1)]
    f = list(seed_vals)  # f[i] ~ f(grid[i])
    for _ in range(iters):
        # f_next(x) = 1 + trapezoid int_0^x f
        f_next = [0.0] * (n + 1)
        acc = 0.0
        f_next[0] = 1.0
        for i in range(1, n + 1):
            acc += h * (f[i - 1] + f[i]) / 2.0
            f_next[i] = 1.0 + acc
        f = f_next
    return f, grid

# Seeds: constant 1, linear x+1, quadratic 1+x^2/2 (each sampled on grid)
def seed_vals(seed_fn, X=1.0, n=400):
    h = X / n
    return [seed_fn(i * h) for i in range(n + 1)]

results = {}
for name, fn in [("const", lambda t: 1.0),
                 ("linear", lambda t: t + 1.0),
                 ("quad", lambda t: 1.0 + t * t / 2.0)]:
    f, grid = picard_grid(seed_vals(fn))
    results[name] = f[-1]  # value at x=1
    print(f"[U1] Picard({name}) -> f(1) = {f[-1]:.8f}  (e={e:.8f}, |diff| {abs(f[-1]-e):.2e})")

u1_ok = all(abs(v - e) < 1e-2 for v in results.values())
print(f"[U1] all seeds converge to e: {'PASS' if u1_ok else 'FAIL'}")
assert u1_ok

print("\n" + "=" * 70)
print("RE-ENTRANT MACHINE v0.3 (U1 fixed) - VERIFICATION SUMMARY")
print("=" * 70)
print(f"  e  = {e!r}")
print(f"  pi = {pi_machine!r}")
print(f"  e^(i*pi) = {re_part!r} + i*{im_part!r}")
print(f"  U1  = Picard iteration converges to e from all 3 seeds ({ {k: round(v,6) for k,v in results.items()} })")
print(f"  Constants imported: NONE")
print(f"  G1..G4 + U1: {'ALL PASS' if (g1_ok and g2_ok and g3_ok and g4_ok and u1_ok) else 'FAILURE'}")
print("=" * 70)
sys.exit(0 if (g1_ok and g2_ok and g3_ok and g4_ok and u1_ok) else 1)
