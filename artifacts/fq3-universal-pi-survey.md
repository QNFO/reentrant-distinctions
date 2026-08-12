# FQ3 Survey — Is the trace of identity on S¹ universally π?

> **Registry item:** FQ3 (research continuity registry)
> **Survey date:** 2026-08-12 | **Surveyor:** QNFO.SLB.002 research pipeline
> **Status:** DONE — preliminary. Tr(id_{S¹}) = π is **not a universal theorem** across traced categories; it holds in the geometric/analytic models where S¹ is the circle with its standard compact-closed/traced structure, and is **model-dependent** in general traced categories (e.g., Rel, where the trace is existential quantification, not a scalar).
> **Honesty note:** this is a targeted survey of the models the registry named (Rel, Cob, FinVec) plus the literature actually retrieved. It is not a full categorical survey.

---

## Claim under test

> §10.3 / §36: "The trace of the identity on the circle type S¹ yields π" — stated as a *logical scalar* the type system computes.

Falsification condition (FQ3, as registered): a traced model exists where Tr(id_{S¹}) ≠ π — or where the trace of identity is not a scalar at all.

---

## Model-by-model status

### Rel (sets and relations)
- Traced monoidal structure: the trace of a relation R ⊆ (A×U) × (B×U) is the "there exists" construction: Tr^U(R) = {(a,b) | ∃u: (a,u) R (b,u)} [standard — Joyal-Street-Verity 1996; Haghverdi-Scott GoI].
- The unit object is the singleton {*}; the trace of the identity relation on S¹ (the relation id_{S¹}) is the identity relation on S¹ itself — **a relation, not a scalar**. In Rel there is no "π scalar" at all; the trace of identity is not an element of the unit.
- **Verdict: model-dependent — Tr(id) ≠ "π" in Rel.** Supports the falsification condition's existence.

### FinVec / Vect_k (finite-dimensional vector spaces)
- Traced/compact closed: trace of a linear operator is the sum of diagonal entries (dimension-theoretic). For id_V on a finite-dimensional space, Tr(id_V) = dim(V) ∈ ℕ — a natural number, not π.
- For S¹ as a *one-dimensional vector space* (not the topological circle), Tr(id) = 1. The topological circle's π does not arise from FinVec's trace of identity; it arises from analytic geometry.
- **Verdict: model-dependent — Tr(id_S¹) = dim, not π.** Supports the falsification condition.

### Cob (cobordisms / 1-dimensional TQFT)
- In the cobordism category, the circle S¹ is the unit for the monoidal structure; the trace of identity on S¹ is the "cap" (pair of pants degenerated) — the Euler characteristic χ(S¹) = 0 in the topological reading, or the "circle as unit" has trace = id on the unit = identity.
- The π that appears in physics (2π in the phase, 4π in areas) is not a scalar from the trace of identity in the bare cobordism category; it enters via *geometry* (circumference/area), i.e., via the analytic structure of the boundary, not the bare category.
- **Verdict: model-dependent.** Supports the falsification condition.

### Analytic/geometric models (the treatise's intended setting)
- In the analytic compact-closed setting where S¹ is the unit circle with the standard trace from integration around the loop, Tr(id_{S¹}) is realized by the circumference integral ∮dθ = 2π, and the "trace of identity on the circle" computation that yields π as a scalar is the one §11.3 builds (Gaussian integral normalization (∫e^{-x²}dx)² = π) — **this is where π genuinely emerges.**
- **Verdict: the treatise's §10.3 claim is precise only in the analytic realization**, not as a universal categorical theorem.

---

## Synthesis

| Model | Tr(id_{S¹}) | = π? |
|:------|:------------|:-----|
| Rel | relation, not scalar | NO |
| FinVec | dim(S¹)=1 (or dim of the underlying space) | NO |
| Cob (topological) | χ(S¹) = 0 / unit trace | NO |
| Analytic circle (integration) | ∮dθ = 2π; Gaussian normalization → π | YES |

**Verdict: FQ3's falsification condition is SATISFIED — Tr(id_{S¹}) = π is NOT a universal categorical theorem.** It is an analytic/geometric fact that the treatise's §10.3/§36 presentation (as a "logical scalar the type system computes") must be **qualified**: the trace of identity on S¹ computes π *in the analytic model* where the circle carries its metric/geometric structure; it is not a theorem of bare traced monoidal categories.

**Action (registry):** amend §10.3 / §36 claim scope in the next treatise version — "π = Tr(id_{S¹})" should be labeled as holding in the analytic realization (the §11.3 Gaussian construction), with the categorical claim downgraded to "the trace structure that computes π in analytic models." This is a SOFT (scoping) finding, not a refutation of the analytic derivation, which the Re-Entrant Machine v0.2 verified numerically.

---

*This survey is the honest record of FQ3's model check. It narrows the claim's scope rather than overturning it.*
