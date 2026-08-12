# Appendices

> **WBS:** QNFO.SLB.002.P4.T4 | **Draft:** v0.1 | **Date:** 2026-08-12
> **Status:** FIRST DRAFT — technical appendices, formal content
> **Genre:** A (Epistemic)

---

## Appendix A. Categorical Semantics for Differential Linear Logic

### A.1 Differential categories

The categorical semantics of DiLL is given by *differential categories* [established — Blute, Cockett & Seely 2006; Ehrhard 2018]. A differential category is a symmetric monoidal category with:

1. A **monoidal coalgebra modality** $!$ (the exponential).
2. A **codereliction** map $\eta: A \to !A$ that embeds each object into its "exponential copy."
3. A **differential operator** $D$ that satisfies the axioms of differentiation: linearity, Leibniz rule, and the Schwarz (symmetry) condition.

The standard model: the category of vector spaces with the symmetric algebra $!A = \bigoplus_n S^n(A)$, where the differential operator is the directional derivative [established — Ehrhard 2018].

### A.2 Coherence conditions

The coherence conditions of differential categories [established — Blute-Cockett-Seely 2006]:

- The differential operator $D: \text{Hom}(A \otimes B, C) \to \text{Hom}(A \otimes B \otimes B, C)$ is linear in the first variable, and
- satisfies the product rule: $D(f \circ g) = D(f) \circ (g \otimes D(g))$ with the appropriate tensor structure,
- and the interchange (Schwarz) symmetry: $D^2$ is symmetric in the two directions.

These conditions are the categorical form of the derivative's defining properties; they are the coherence conditions referenced in §7 and §35.

### A.3 Standard models

| Model | Exponential modality | Differential operator |
|:------|:----------------------|:----------------------|
| Vector spaces (k-linear) | Symmetric algebra | Directional derivative |
| Finiteness spaces | Finitely-supported sequences | Taylor expansion |
| Convenient vector spaces | Smooth maps | Fréchet derivative |
| CoKleisli of ! | - | Composition of smooth maps |

[established — Ehrhard 2018; Blute-Cockett-Seely 2006].

### A.4 The fixed point of the differential exponential

In the vector space model, the codereliction of the identity produces the operator whose fixed points are the exponentials [established — the derivative of the exponential is the exponential]. The identification of this fixed point with the constant $e$ (§9) is [my conjecture] and is the subject of the computational verification in Appendix D.

---

## Appendix B. The Bruhat-Tits Building as a Simplicial Type

### B.1 The tree as a higher inductive type

The Bruhat-Tits tree for $\mathbb{Q}_p$ (Part IV, §14) is the regular tree where each vertex has $p+1$ neighbors. It is constructed as a higher inductive type [my conjecture — the construction is natural but the specific HIT presentation is this treatise's proposal]:

- **Vertex type:** the type of balls in $\mathbb{Q}_p$, with the hierarchy of inclusions.
- **Edge type:** the type of adjacent inclusions (ball contains sub-ball at adjacent level).
- **Path type:** the type of paths in the tree — the homotopical structure that makes the tree a *space*.

The HIT presentation realizes the tree's *simplicial structure*: the tree is a 1-dimensional simplicial complex, and the HIT gives it the corresponding homotopy type (contractible, as all trees are).

### B.2 The construction

[my conjecture] The Bruhat-Tits tree HIT:

1. **Point constructors:** for each ball $B \subseteq \mathbb{Q}_p$, a point.
2. **Edge constructors:** for each inclusion $B \supset B'$ at adjacent levels, a path.
3. **Truncation:** the tree type is the 0-truncation of the path structure (a set), with the path structure making it a 1-type.

The construction is the geometric realization of the $?$ modality (Part II, §6.2; Part IV, §14.2): the tree type is the type of unlimited branching.

### B.3 Connection to the modal structure

The Bruhat-Tits building for $GL_n(\mathbb{Q}_p)$ is the higher-dimensional analogue — a *building*, the simplicial complex whose apartments are Coxeter complexes [established — Bruhat & Tits 1972]. [my conjecture] The building is the higher-categorical realization of the $?$ modality: the $n$-dimensional branching structure of the $GL_n$ action. The HIT presentation of the building is the type-theoretic form of the discrete tree structure of the non-Archimedean place.

---

## Appendix C. Explicit Formula as a Trace in Adelic Cohomology

### C.1 The Riemann-von Mangoldt explicit formula

The explicit formula of analytic number theory relates the primes to the zeros of the zeta function [established — Riemann 1859; von Mangoldt 1895; standard analytic number theory]:

$$\psi(x) = x - \sum_\rho \frac{x^\rho}{\rho} - \log 2\pi - \frac{1}{2}\log(1 - x^{-2})$$

where $\psi(x)$ is the Chebyshev function and $\rho$ runs over the nontrivial zeros of $\zeta$.

### C.2 The adelic trace reading

[my conjecture] The explicit formula is a *trace identity in adelic cohomology*: it is the statement that the trace of a certain operator on the adelic space (Part IV, §15-17) counts the primes. The structure:

- The **left side** $\psi(x)$ counts the primes — the tree structure (Part IV, §14).
- The **right side** $x - \sum x^\rho/\rho - \ldots$ is the spectral decomposition — the loop structure (the zeros as eigenvalues on the loop).

The explicit formula equates the tree count (left) with the loop spectrum (right) — the number-theoretic form of the loop-tree duality.

### C.3 Status

The explicit formula is [established]; the trace-theoretic reading is [my conjecture] and requires the precise adelic operator formalism that this appendix sketches. The full development is a research program (the "explicit formula as trace" program suggested by this treatise).

---

## Appendix D. A Computational Implementation: The Re-Entrant Machine

### D.1 The proof assistant

[my conjecture] The Re-Entrant Machine is a proof assistant based on the Calculus of Re-Entrant Distinctions: a computational system that:

1. Implements the calculus of indications (Part I).
2. Implements the linear type theory with exponentials and traces (Part II, §8).
3. Implements the differential combinator (Part II, §7; Part VIII, §35).
4. **Derives $\pi$:** computes the trace of the identity on the circle type (§10.3, §36).
5. **Derives $e$:** computes the fixed point of the differential exponential (§9, §36).
6. **Checks the functional equation of zeta:** verifies $\xi(s) = \xi(1-s)$ in the adelic model (§17).

### D.2 Verification goals

The computational implementation's verification goals (per the falsifiability conditions of §12.2 and §36):

| Goal | Claim verified | Status |
|:-----|:---------------|:-------|
| G1 | The mark's re-entry produces the oscillation | Part I, §3 |
| G2 | The differential combinator produces the exponential series | Part III, §9 |
| G3 | The trace of id on S^1 computes pi | Part III, §10.3 |
| G4 | The system derives e^{i pi} = -1 without importing e and pi as axioms | Part III, §12.2 |
| G5 | The adelic model satisfies the functional equation | Part IV, §17 |

**G4 is the critical verification:** if the machine can derive $e^{i\pi} = -1$ from the mark's structure without importing the constants, the treatise's central thesis is computationally verified; if not, the thesis is refuted.

### D.3 Implementation sketch

The implementation would use a proof assistant with linear type theory and higher inductive types (e.g., a linear extension of a HoTT-based assistant, or the categorical semantics of Appendix A implemented computationally). The sketch:

- **Types:** the mark type, the circle type $S^1$ as a higher inductive type, the linear types with duals.
- **Terms:** the re-entrant form, the trace operator, the differential combinator.
- **Verification:** normalization and computation of the trace and fixed-point terms, comparison with the expected scalars.

### D.4 Status

The Re-Entrant Machine is a *sketch* — a research program, not an implementation. Its construction is the concrete next step of the treatise's program (P9 Extension). The sketch's honesty: the machine does not yet exist; the verification goals (G1-G5) are the acceptance criteria it must meet.

---

## End of Appendices (Draft v0.1)

### Drafting Notes (internal — remove before publication)

- **Citations:** Appendix A: Blute-Cockett-Seely 2006, Ehrhard 2018 (P3-verified). Appendix C: Riemann 1859, von Mangoldt 1895 (classical — add to second-pass citation list). Appendix B: Bruhat-Tits 1972 (add to second-pass list).
- **Certainty labels:** applied inline. The constructions (Bruhat-Tits HIT, explicit formula as trace, Re-Entrant Machine) are [my conjecture] / research programs; the mathematics they use is [established].
- **Banned words check:** none used.
- **Ostrowski Dimensionless (§0.7):** no dimensional physics formulas in the appendices.
- **Critical:** Appendix D's G4 (deriving Euler identity without importing constants) is the treatise's decisive falsifiable claim — its success or failure determines the central thesis.
