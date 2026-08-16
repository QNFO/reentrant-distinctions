# RESEARCH-CONTINUITY-REGISTRY.md

> **Project:** QNFO.SLB.002 — The Calculus of Re-Entrant Distinctions
> **Created:** 2026-08-12 | **Registry version:** v1.0
> **Canonical DOI:** 10.5281/zenodo.21908818 (v0.8); latest 10.5281/zenodo.21964453 (v0.9, 2026-08-16 so-what remediation)
> **Purpose:** Per research v2.64 — any QNFO publication containing frontier questions, falsifiable predictions, or pre-registration scaffolds MUST be tracked in a living registry.

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | Can the formal system of Part VIII (traced differential cohesive linear HoTT) derive $e^{i\pi} = -1$ without importing $\mathbb{R}$ and $\exp$ as external axioms? | OPEN | Build Appendix D Re-Entrant Machine; attempt G4 | YES — REG-SLB-001 |
| FQ2 | Does the coKleisli fixed-point claim of §9.2 hold as a theorem in DiLL (codereliction/differential-operator fixed point = $e$)? | OPEN | Formalize in DiLL; search literature for fixed-point semantics of the exponential modality | YES — REG-SLB-002 |
| FQ3 | Is the trace of identity on $S^1$ universally $\pi$ in the compact closed structure, or model-dependent? | OPEN | Survey traced models (Rel, Cob, FinVec); pin the universal claim | YES |
| FQ4 | Can the p-adic tree construction (Appendix B) be realized as a higher inductive type with the claimed homotopy type? | OPEN | Implement HIT in a HoTT proof assistant | YES |
| FQ5 | Does the adelic trace reading of the explicit formula (Appendix C) yield the Riemann–von Mangoldt formula exactly? | OPEN | Develop adelic operator formalism; verify against $\psi(x)$ | YES — REG-SLB-003 |
| FQ6 | Is mass-as-re-entry-frequency (§24.1) a re-description or does it carry any observable prediction beyond standard QM phase? | OPEN | KIF-60 null-equivalence analysis; state $O_N$ vs $O_T$ | NO (structural) |

---

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| P1 | The Re-Entrant Machine (Appendix D) computes $\pi$ from $Tr(id_{S^1})$ and $e$ from $Df=f$ without external constants. | 12 months | Re-Entrant Machine implementation | The machine imports $e$ or $\pi$ as axioms → claim refuted |
| P2 | The machine verifies $\xi(s) = \xi(1-s)$ in the adelic model. | 12 months | Appendix D G5 | Functional equation fails in the model → adelic reading refuted |
| P3 | The p-adic tree HIT of Appendix B has contractible homotopy type (as all trees). | 12 months | HoTT proof assistant | HIT is non-contractible → construction incorrect |

---

## 3. PER-RQ FALSIFIABILITY CONDITIONS

| RQ | Condition (disconfirmed if) |
|:---|:----------------------------|
| §12.2 | The formal system imports $\mathbb{R}$/$\exp$ as external axioms to derive $e^{i\pi}=-1$ |
| §24.1 | A particle's rest-frame phase evolution deviates from $e^{-imt}$ (Planck units), or the re-entrant clock fails to produce the exponential phase factor |
| §26.2 | A measurement is exhibited that does not correspond to a trace operation in the modal category |
| §27 | The modal reading fails to organize the known AdS/CFT theorems |
| §39.2 | A structure the algorithm claims to generate cannot be generated; or the modal reading contradicts an established physical law |

---

## 4. PRE-REGISTRATION SCAFFOLDS

### REG-SLB-001 — Euler identity derivation (G4)
- **Hypothesis:** The Calculus of Re-Entrant Distinctions derives $e^{i\pi} = -1$ from the re-entrant mark without importing $e$ or $\pi$.
- **Falsification:** Machine (Appendix D) requires external constants.
- **Data:** Appendix D implementation log; computed trace/fixed-point terms.
- **Deadline:** 2027-08-12.
- **Status:** SCAFFOLDED (pre-registration document pending — publish to Zenodo as overlay when implementation begins)

### REG-SLB-002 — coKleisli fixed point = e
- **Hypothesis:** In DiLL semantics, the codereliction/differential-operator fixed point of the exponential modality evaluates to $e$.
- **Falsification:** A DiLL model where the fixed point is not $e$.
- **Data:** Formal DiLL model construction.
- **Deadline:** 2027-08-12.
- **Status:** SCAFFOLDED

### REG-SLB-003 — explicit formula as adelic trace
- **Hypothesis:** The Riemann–von Mangoldt explicit formula arises as a trace identity in adelic cohomology.
- **Falsification:** Trace computation does not reproduce $\psi(x)$.
- **Data:** Appendix C formalism; computational verification.
- **Deadline:** 2027-08-12.
- **Status:** SCAFFOLDED

---

## 5. CALIBRATION REGISTER

```
[CHECK: 2027-08] Re-Entrant Machine G1-G5 all pass.
Strength: [STRONG — falsifiable, computational]
Status: [PENDING]

[CHECK: 2027-08] P1-P3 above resolved.
Strength: [STRONG]
Status: [PENDING]

[CHECK: 2028-08] ≥1 external citation of the treatise's e/pi-as-logical-scalars claim.
Strength: [WEAK — depends on community]
Status: [PENDING]
```

---

## 6. NEXT ACTIONS (Prioritized)

| Priority | Action | Depends On | Target |
|:---------|:-------|:-----------|:-------|
| P0 | Pre-register REG-SLB-001..003 (publish scaffolds to Zenodo overlay / papers.qnfo.org) | — | 2026-Q4 |
| P0 | Begin Appendix D Re-Entrant Machine implementation (G4 critical) | REG-SLB-001 | 2027-Q1 |
| P1 | Formalize §9.2 coKleisli fixed-point claim in DiLL literature review | — | 2026-Q4 |
| P1 | Survey traced models for §10.3 universal-π claim | — | 2026-Q4 |
| P2 | Adelic trace formalism (Appendix C) | — | 2027-Q1 |
| P2 | Bruhat-Tits HIT in proof assistant (Appendix B) | — | 2027-Q2 |

---

## 7. SESSION LOG + MAINTENANCE PROTOCOL

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-12 | QNFO.SLB.002 P7 | Registry created v1.0 after v0.3 publication (DOI 10.5281/zenodo.21905186) |

**Maintenance:** Update at every session touching the treatise (drafting, implementation, or publication). Bump registry version on structural changes. Pre-registration scaffolds MUST be published before implementation begins (per KIF-60 pre-registration requirement — timestamped, immutable record).
- 2026-08-16 — **v0.9 published (DOI 10.5281/zenodo.21964453)**: so-what remediation per the global mandate — new "So What? Why Should a Reader Care About This Research?" section (stakes, foundations/physicist/CS-AI audiences, premises-depth, practical-utility-even-if-parts-fail, explicit non-claims); registry FQ1-FQ6 / P1-P3 / scaffolds unchanged and referenced from the new section; branch resynced from Zenodo v0.8 (had lagged at v0.5c); frontmatter license aligned cc-by-nc-sa-4.0.
