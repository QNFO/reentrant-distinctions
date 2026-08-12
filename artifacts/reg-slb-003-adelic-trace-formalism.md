# REG-SLB-003 — Appendix C Formalism: Explicit Formula as a Trace in Adelic Cohomology

> **Registry item:** REG-SLB-003 (research continuity registry)
> **Status:** FIRST DRAFT (2026-08-12) — formalism sketch, honest about established vs conjectural
> **Parent:** *The Calculus of Re-Entrant Distinctions* (DOI 10.5281/zenodo.21906728), Appendix C
> **Falsification condition (as registered):** the trace computation does not reproduce the Chebyshev function ψ(x)

---

## 1. The target: Riemann–von Mangoldt explicit formula

The explicit formula (established analytic number theory) relates primes to zeros of ζ:

$$ \psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \log 2\pi - \frac{1}{2}\log(1 - x^{-2}) $$

where ψ is the Chebyshev function and ρ runs over nontrivial zeros. The treatise's §17.1 conjecture: this is a **trace identity in adelic cohomology** — the trace of an operator on the adelic space counts the primes.

## 2. What is established

| Element | Status |
|:--------|:-------|
| ψ(x) = Σ_{p^k ≤ x} log p (Chebyshev function) | [established] |
| von Mangoldt explicit formula (above) | [established] |
| Tate's adelic Fourier analysis: ζ-factors as local integrals | [established — Tate 1950] |
| Adeles A_Q = restricted product over all places; self-dual under Fourier | [established] |
| Weil's explicit formula (generalized, function-field/adelic reading) | [established — Weil 1952; standard] |

**Key established anchor:** the Weil explicit formula is already a *distributional trace* statement: the sum over primes and the sum over zeros appear as the two sides of a distribution pairing on the ideles. This is the strongest support for the conjecture's plausibility — the adelic/idelic structure already hosts the explicit formula in the literature.

## 3. The conjectural step (this treatise's claim)

The novel claim: the explicit formula is the **trace of the identity-like operator on the adelic cohomology**, parallel to the treatise's §17 reading of the completed zeta as an adelic trace and §36's claim that the trace of identity computes scalars in the analytic realization.

Sketch (what would have to be true):

1. Construct a space of adelic test functions / a cohomology theory H^*(A_Q) with a trace pairing.
2. Define the operator T whose spectral trace is the sum over zeros: Tr(T | H^*(A_Q)) = Σ_ρ x^ρ/ρ.
3. Show the trace formula (Weil / Riemann–von Mangoldt) equates this spectral trace with the arithmetic side: the prime count ψ(x) = Tr(T) - (trivial factors).
4. The functional equation ξ(s) = ξ(1-s) is then the self-duality of the trace (the treatise's §17.2 loop/tree reading).

**Honest status:** steps 1–3 are NOT established in this draft. The Weil explicit formula provides the *distributional* trace framework, but the *cohomological* trace reading (an operator on adelic cohomology whose trace yields ψ) is a research program, not a theorem. The Re-Entrant Machine does not yet test REG-SLB-003 (unlike G4 for REG-SLB-001).

## 4. Verification path (next actions)

1. **P1:** Study the Weil explicit formula in its idelic/distributional form (Connes' trace formula program is the closest existing framework — Connes 1999, "Trace formula in noncommutative geometry and the zeros of the Riemann zeta function").
2. **P1:** Determine whether Connes' adelic/noncommutative trace formula already implies the treatise's "explicit formula as adelic trace" reading — if so, the claim is [established-adjacent] rather than novel, and the treatise must cite Connes.
3. **P2:** Build a computational check: for a truncated zero set, verify Σ x^ρ/ρ reproduces ψ(x) (numerically — this is a known check of the explicit formula, not of the cohomological reading).
4. **Falsification monitor:** if no trace operator on adelic cohomology can be constructed with the required spectral properties within the formal framework, the claim is refuted per REG-SLB-003.

## 5. Key references to consult

- Weil, A. (1952). *Sur les formules explicites de la théorie des nombres*. (the explicit-formula-as-distribution anchor)
- Tate, J. (1950). Fourier analysis in number fields.
- Connes, A. (1999). Trace formula in noncommutative geometry and the zeros of the Riemann zeta function. *Selecta Math.* (closest existing trace-formula framework)
- Riemann (1859) / von Mangoldt (1895) (classical anchors)

## 6. Conclusion (honest)

This draft establishes the *plausibility* of REG-SLB-003: the explicit formula is already a distributional trace in the idelic setting (Weil), so the "trace identity" reading is not far-fetched. The *cohomological* refinement (a trace on adelic cohomology) is the open, falsifiable core. Next concrete step: study the Connes trace-formula program and determine the overlap — this may convert REG-SLB-003 from [my conjecture] to [established-adjacent] or expose a precise falsification.

---

*This is a first-draft formalism artifact, not a published claim. It carries the treatise's certainty labels (established vs conjectural) and is tracked in the research continuity registry.*
