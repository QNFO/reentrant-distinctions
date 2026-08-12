# REG-SLB-002 — Formal DiLL Model Construction: the codereliction fixed point

> **Registry item:** REG-SLB-002 (research continuity registry)
> **Status:** MODEL CONSTRUCTION DONE — 2026-08-12 (survey done earlier; claim OPEN, consistent with the model)
> **Parent:** *The Calculus of Re-Entrant Distinctions* (DOI 10.5281/zenodo.21908428, v0.7)
> **Pre-registration:** REG-SLB-002 scaffold (overlay DOI 10.5281/zenodo.21907630)

---

## 0. Claim (as pre-registered)

> In DiLL semantics, the codereliction/differential-operator fixed point of the exponential modality (the coKleisli morphism of `!`) evaluates to e.

Falsification condition: a DiLL model where the fixed point is not e.

## 1. The standard smooth model (convenient vector spaces)

The canonical model of DiLL (Ehrhard; Blute–Cockett–Seely differential categories) is the category of convenient vector spaces with smooth maps:

- Objects: convenient vector spaces $E, F$ (locally convex, $c^\infty$-complete).
- Linear maps: bounded linear maps.
- Smooth maps: $c^\infty$-maps.
- Exponential modality: $!E = C^\infty(E^*, \mathbb{C})$ (smooth functions on the dual) — for finite-dimensional $E$, $!E \cong C^\infty(E)$.
- CoKleisli category: morphisms $!E \to F$ are smooth maps $E^* \to F$.

**Codereliction** (the map $\eta: A \to !A$, or rather its dual): the codereliction of $v \in E$ is the linear functional $w \mapsto \langle v, w\rangle$ on $E^*$ — i.e., the "linear part" of a smooth function. More precisely, in the differential category axioms, the codereliction $\eta_A: A \to !A$ embeds $A$ as the linear (degree-1) part of $!A$, and the differential operator $D: !A \to A \multimap A$ differentiates.

## 2. The fixed-point equation in the model

In the coKleisli category, a morphism $f: !\mathbb{R} \to \mathbb{R}$ is a smooth function $f: \mathbb{R} \to \mathbb{R}$. Its derivative under the differential combinator is $Df: \mathbb{R} \to \mathbb{R}$, $Df(x) = f'(x)$ (the usual derivative).

The claim's fixed-point equation in the model:

$$ Df = f, \qquad f(0) = 1, $$

i.e. $f' = f$, $f(0) = 1$ — the exact ODE of REG-SLB-001 Theorem 1.

## 3. Result

By Picard–Lindelöf + power-series (REG-SLB-001 Theorems 1–3, both [established]):

- The equation $Df = f$, $f(0)=1$ has a **unique** smooth solution in the model: $f(x) = \sum x^n/n! = e^x$.
- Evaluating at $x=1$: $f(1) = e$.
- **Therefore, in the smooth model, the codereliction/differential fixed point evaluates to e — the claim HOLDS in this model.**

## 4. What this does and does not establish

| Question | Answer |
|:---------|:-------|
| Does the claim hold in the standard smooth model? | **YES** — unique solution $e^x$, fixed point = e (established). |
| Does this prove the claim as a *bare categorical theorem* (all DiLL models)? | **NO** — this is one model. Consistent with the FQ3 lesson: categorical claims are model-dependent unless proven categorically. |
| Is the falsification condition met? | **NO** — no model with fixed point ≠ e has been constructed; the smooth model confirms e. |
| Is the claim proven categorically? | **NO** — the categorical proof (for all models satisfying DiLL axioms + analyticity axioms) is the open core. |

## 5. Honest status

- **Claim status: CONSISTENT (confirmed in the standard smooth model); OPEN as a categorical theorem.**
- **Registry update:** REG-SLB-002 → MODEL CONSTRUCTION DONE (standard smooth model confirms the fixed point = e; bare-categorical proof remains open).
- **Next action:** search for a DiLL model (possibly non-analytic, e.g. finiteness spaces / relational models) where the fixed point fails to be e — this would falsify the categorical claim. The Re-Entrant Machine's numerical verification supports the analytic reading.

---

*This artifact records the formal model construction for REG-SLB-002. It narrows the open question to the categorical generality, consistent with the FQ3 model-dependence finding.*
