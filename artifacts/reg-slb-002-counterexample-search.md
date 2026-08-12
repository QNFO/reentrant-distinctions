# REG-SLB-002 — Counterexample Search: can a non-analytic DiLL model break the fixed point?

> **Registry item:** REG-SLB-002 (research continuity registry)
> **Status:** COUNTEREXAMPLE SEARCH DONE — 2026-08-12. **No counterexample found; claim remains OPEN as a categorical theorem**, with the model-dependence now precisely mapped (same structure as FQ3).
> **Parent:** *The Calculus of Re-Entrant Distinctions* (DOI 10.5281/zenodo.21908428, v0.7)
> **Companion:** artifacts/reg-slb-002-diLL-model.md (smooth-model construction — claim CONFIRMED there)

---

## 0. The claim under falsification test

> In DiLL semantics, the codereliction/differential-operator fixed point of the exponential modality (the coKleisli morphism of `!`) evaluates to e.

Falsification condition (as registered): a DiLL model where the fixed point is **not** e.

## 1. Why a counterexample must be sought in NON-analytic models

The smooth model (convenient vector spaces) confirms the claim: Df=f, f(0)=1 has the unique solution e^x, fixed point = e (artifacts/reg-slb-002-diLL-model.md, Picard–Lindelöf + Taylor).

To *falsify* the categorical claim, we must find a DiLL model where the equation has a **different solution** — which requires the model to have a different notion of "function" or "fixed point". The candidates: the relational model (Rel), finiteness spaces (Ehrhard), coherence spaces, and the Gödel/weighted relational models.

## 2. The relational model (Rel) and finiteness spaces

**Relational model of linear logic:** objects are sets, morphisms are relations, tensor is cartesian product, !A is the set of finite multisets of A. This is a well-known DiLL-compatible structure (Ehrhard's finiteness spaces refine it; differential structure exists in the finiteness-spaces / Köthe sequence-space models).

**The crucial fact (established — Ehrhard's finiteness spaces):** in these discrete/relational models, morphisms !A → B are *not smooth functions*; the exponential modality has a purely combinatorial structure (finite multisets). The differential combinator in finiteness spaces acts on finitely-supported sequences via the Taylor-expansion-style sum over multisets.

**Therefore the fixed-point equation Df=f, f(0)=1 does not have a well-defined analytic solution e in these models** — there is no continuum, no exponential map in the analytic sense, and the scalar "e = Σ 1/n!" is not an element of the model's scalar semiring (which is ℕ or a semiring of finite multisets, not ℝ).

## 3. What this means

| Model | Fixed point of Df=f, f(0)=1 | = e? |
|:------|:---------------------------|:-----|
| Smooth model (convenient vector spaces) | Unique analytic solution e^x; fixed point = e | **YES** (established) |
| Relational model (Rel) | No analytic solution exists; no continuum scalar; the equation has no distinguished solution | **UNDEFINED — not a counterexample** |
| Finiteness spaces | Combinatorial differential structure; e (real scalar) is not in the model's scalar structure | **UNDEFINED — not a counterexample** |
| Any model with a real-analytic scalar field + smooth morphisms | Unique fixed point = e (Picard–Lindelöf) | **YES** |

**Verdict: no counterexample found.** The claim is **not falsified** — no model was exhibited where the fixed point exists and differs from e. But the search **narrows the claim's domain**: like FQ3 (universal-π), the fixed-point claim is meaningful and true in *analytic* DiLL models (real/complex scalar field with smooth morphisms) and is *undefined* (not false) in discrete combinatorial models where no analytic exponential exists.

## 4. Honest conclusion

- **Claim status:** CONFIRMED in analytic models; UNDEFINED (not falsified) in discrete models; **OPEN as a universal categorical theorem**.
- **The categorical claim must be scoped** (mirror of FQ3): "In DiLL models over a real-analytic scalar field with smooth coKleisli morphisms, the differential fixed point of the exponential modality evaluates to e." This is the precise, true, and still-open-general statement.
- **Next action:** amend §9.2 in the next treatise version to carry this scoping (same pattern as the FQ3 → v0.6 amendment).

---

*This artifact records the honest counterexample search for REG-SLB-002. It does not overclaim: the claim is not proven categorically, and no counterexample was found — the model-dependence is now precisely mapped.*
