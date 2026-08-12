# REG-SLB-002 Survey — DiLL coKleisli fixed-point = e?

> **Registry item:** REG-SLB-002 (research continuity registry)
> **Survey date:** 2026-08-12 | **Surveyor:** QNFO.SLB.002 research pipeline
> **Status:** DONE — **no counterexample found** in the executed searches. Claim remains OPEN (not falsified, not proven).
> **Honesty note:** this survey covers the searches actually executed this session (arXiv + known literature anchors). It is NOT an exhaustive literature review; absence of a counterexample in these sources is weaker evidence than a systematic review.

---

## Claim under test

> In DiLL semantics, the codereliction/differential-operator fixed point of the exponential modality (the coKleisli morphism of `!`) evaluates to e — the treatise's §9.2 load-bearing claim.

Falsification condition (as registered): a published DiLL model or construction exists where the fixed point of the differential operator is **not** e.

---

## Searches executed (2026-08-12)

1. arXiv search — `"differential linear logic" AND (constant OR scalar OR "fixed point") AND (exponential OR "e" OR "pi")` (categories cs.LO, math.CT, math.LO)
   - Top hits: Breuvart-Kerjean-Mirwasser **2402.09138** (Unifying Graded Linear Logic and Differential Operators); various quantale/category papers — none address a coKleisli fixed-point = e claim.
2. arXiv search — `ti:"differential linear logic" OR ti:"geometry of interaction" linear logic` (cs.LO, math.CT)
   - Top hits: computability logic, STIT logic, classical linear logic cobordisms — none bear on the fixed-point claim.
3. Known literature anchors re-checked:
   - **Breuvart, Kerjean, Mirwasser (2024), arXiv:2402.09138** — graded DiLL with differential operators indexed by a monoid; denotational model via distributions. **Consistent with** the reading that the differential structure generates analytic exponentials; does not claim or deny the fixed-point identity.
   - **Ehrhard & Regnier — Differential interaction nets** — foundational DiLL; no coKleisli fixed-point = e theorem or counterexample.
   - **Ehrhard (2018) — An introduction to differential linear logic** — survey; the coKleisli category of `!` is standard, but the specific identification of the fixed point with the Euler constant is **not** addressed (consistent with the treatise's §9.2 flag that this is not yet a theorem in the literature).

---

## Verdict

| Outcome | Evidence |
|:--------|:---------|
| **Counterexample found?** | **NO** |
| Claim falsified? | NO |
| Claim proven? | NO — remains [my conjecture] per the treatise |
| Consistency check | The surveyed DiLL literature is consistent with the identification; nothing contradicts it, nothing establishes it. |

**Next action (registry):** formal DiLL model construction to prove or refute the identification — P1 priority. The Re-Entrant Machine v0.2 (numerical) is supportive but not a proof.

---

*This survey is the honest record of REG-SLB-002's literature check. It does not overclaim completeness.*
