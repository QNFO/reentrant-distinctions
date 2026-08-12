# Re-Entrant Machine

**Appendix D computational implementation — *The Calculus of Re-Entrant Distinctions*** (DOI 10.5281/zenodo.21906728, v0.5)

## Status: v0.2 — G1–G4 ALL PASS (numerical PoC)

The machine computes **e** and **π** and verifies **e^{iπ} = −1** using only the mark's differential structure (Taylor series machinery) — **without importing** `math.e`, `math.pi`, `math.exp`, `math.cos`, `math.sin`, `math.sqrt`, or any transcendental constants.

### Verification goals (Appendix D)

| Goal | Claim | v0.2 result |
|:-----|:------|:------------|
| G1 | The mark's re-entry produces the oscillation (period-2 clock) | PASS — `[1,0,1,0,1,0,1,0]` |
| G2 | The differential combinator produces the exponential series; e = fixed point Df=f | PASS — e = 2.7182818284590455 (|err| 4.4e-16) |
| G3 | The trace of identity on S¹ computes π via the Gaussian integral (∫e^{-x²}dx)² = π | PASS — π = 3.141592652354373 (|err| 1.2e-9) |
| G4 | e^{iπ} = −1 derived without importing e or π | PASS — cos(π)+i sin(π) = −0.9999999999999998 + i·1.2e-9 |

### Honest development record

- **v0.1 FAILED G3** (2026-08-12): the naive alternating Taylor series for e^{−x²} at large |x| catastrophically cancels in float64 → I = −1.68e23. Recorded, not hidden.
- **v0.2 FIX** (2026-08-12): compute e^{−t} = 1/exp_series(+t) — the positive series is numerically stable. The exponential remains internally generated (fixed point of Df=f), not imported.

### What this is / is not

- **IS:** a numerical proof-of-concept that the re-entrant-mark program is not vacuous — the constants emerge from the differential combinator and the trace construction.
- **IS NOT:** a formal proof. REG-SLB-001 (Euler derivation in a formal system) and REG-SLB-002 (DiLL coKleisli fixed point = e as a theorem) remain pending formalization.

### Files

- `reentrant_machine_v02.py` — canonical implementation (G1–G4, all pass)
- `reentrant_machine_v01.py` — failed v0.1 (kept for the honest failure record)

### Related

- Pre-registration overlay: DOI 10.5281/zenodo.21907580
- Research continuity registry: `RESEARCH-CONTINUITY-REGISTRY.md` (REG-SLB-001/002/003)
