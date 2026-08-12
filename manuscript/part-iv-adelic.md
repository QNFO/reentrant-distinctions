# Part IV — The Landscape of Numbers: Adelic Geometry through Modal Lenses

> **WBS:** QNFO.SLB.002.P4.T2 | **Draft:** v0.1 | **Date:** 2026-08-12
> **Status:** FIRST DRAFT — subject to red-team review before publication
> **Genre:** A (Epistemic) — certainty calibration applied inline

---

## §13. Ostrowski's Theorem as a Completeness of Distinction Systems

### 13.1 Absolute values as modes of measuring the mark

Ostrowski's theorem [established — Ostrowski 1918, Acta Math 41, 271–284] classifies all absolute values on the rational numbers $\mathbb{Q}$: every nontrivial absolute value is either

1. the *Archimedean* absolute value $|\cdot|_\infty$ (the usual real absolute value), or
2. a *p-adic* absolute value $|\cdot|_p$ for some prime $p$.

The completions are the real numbers $\mathbb{R}$ (for the Archimedean place) and the p-adic numbers $\mathbb{Q}_p$ (for each non-Archimedean place).

[my conjecture] The classification is a *completeness theorem for distinction systems*: the ways of measuring the mark — the ways of assigning a size to a difference — are exactly the absolute values, and Ostrowski's theorem says there is one *continuous* way (the real/Archimedean place) and infinitely many *discrete* ways (the p-adic places). In the language of Part II:

- The Archimedean place is the **loop**: the real numbers are the completion that makes the re-entrant mark's oscillation continuous (Part I, §4; Part III, §9).
- The p-adic places are the **trees**: each $\mathbb{Q}_p$ is the completion that makes the branching structure of nested distinctions explicit (Part II, §6.2).

This identification of Ostrowski's classification with the modal pair $(!, ?)$ of linear logic is [my conjecture]. Its content is formalizable: the p-adic valuation is the "branching depth" of a rational number (how many times it divides by $p$), and the Archimedean valuation is the "loop magnitude" (how far it is from zero along the continuous line).

### 13.2 The classification: one smooth loop, infinitely many branching trees

The structure of Ostrowski's theorem is itself the loop–tree duality:

| Place | Valuation | Completion | Modal dual (Part II) | Geometric form |
|:------|:----------|:-----------|:---------------------|:---------------|
| Archimedean | $|\cdot|_\infty$ | $\mathbb{R}$ | $!$ (loop) | Circle, line, continuum |
| p-adic (p = 2,3,5,...) | $|\cdot|_p$ | $\mathbb{Q}_p$ | $?$ (tree) | Bruhat–Tits tree, ultrametric |

The single Archimedean place is the one smooth loop; the countably infinite family of p-adic places is the infinitely branching forest of trees. This is [established] as a fact about Ostrowski's theorem; the modal reading is [my conjecture].

### 13.3 Connection to prior published work

This treatise's Part IV develops the adelic reading of the number system that prior published work has established: the physical continuum is the restricted product over all places [established — Continuum Trilogy, DOI 10.5281/zenodo.21672990], and dimensionless ratios preserve place-democracy [established — Non-Anthropocentric Natural Units, DOI 10.5281/zenodo.21480756]. The broader consilient synthesis across the research portfolio is documented in *Five Pillars, One Framework* (DOI 10.5281/zenodo.21789920). The novel contribution of this treatise is the *modal-logical* derivation: the places are not ad hoc mathematical objects but the completions forced by the distinction calculus's two modes of self-reference (loop and tree).

---

## §14. p-Adic Trees as Discrete Modalities

### 14.1 Ultrametric spaces as tree-like distinctions

A p-adic absolute value satisfies the *ultrametric* (strong triangle) inequality:

$$|x + y|_p \leq \max(|x|_p, |y|_p) \quad [\text{established — p-adic analysis}]$$

The ultrametric inequality is the mathematical form of *tree-like distinction*: the distance between two points is the size of the smallest ball containing both, and balls in an ultrametric space are either disjoint or nested — exactly the structure of a tree [established — ultrametric analysis; the tree representation of ultrametric spaces is standard].

The p-adic numbers $\mathbb{Q}_p$ form an ultrametric space; its balls are indexed by the integers (the valuation levels), and the hierarchy of balls is a regular tree with $p$ branches at each node — the Bruhat–Tits tree [established — Bruhat & Tits 1972; standard p-adic geometry].

### 14.2 The Bruhat–Tits building as the geometric realization of the ? modality

The Bruhat–Tits building for $\mathbb{Q}_p$ is the tree whose vertices are the balls in $\mathbb{Q}_p$ and whose edges are inclusions of balls at adjacent levels [established]. Each vertex has $p+1$ neighbors (the $p$ sub-balls plus the containing ball).

[my conjecture] The Bruhat–Tits tree is the geometric realization of the $?$ modality of linear logic: it is the space of *unlimited branching*, the tree of distinctions that the environment may traverse at will (Part II, §6.2). The identification is:

- The modality $?A$ — the environment's unlimited access to $A$ — is realized geometrically as the tree of balls centered at $A$'s position in the ultrametric space.
- The branching at each node ($p+1$ neighbors) is the discrete counterpart of the $?$-modality's contraction rule (unlimited duplication).

This identification is [my conjecture]; its formal content is developed in Appendix B, which constructs the Bruhat–Tits tree as a higher inductive type.

### 14.3 Ramification as branching depth

The p-adic valuation $v_p(x)$ measures the *branching depth* of $x$: how many levels of the tree separate $x$ from the unit ball. In the language of distinction:

$$v_p(x) = \text{the depth of the mark } x \text{ in the } p\text{-adic tree} \quad [\text{MAP — model of the valuation}]$$

This reading is [established] as a geometric fact (the valuation indexes the levels of the Bruhat–Tits tree) and [my conjecture] as a claim about the primacy of the distinction calculus.

---

## §15. The Adele Ring as Restricted Product of Local Distinctions

### 15.1 Adeles as the global object carrying the real loop and all p-adic trees

The adele ring $\mathbb{A}_{\mathbb{Q}}$ is the restricted product of the completions over all places [established — Weil 1967, Basic Number Theory]:

$$\mathbb{A}_{\mathbb{Q}} = \prod'_{\text{places } v} \mathbb{Q}_v$$

where $\mathbb{Q}_\infty = \mathbb{R}$ and $\mathbb{Q}_p$ for each prime $p$. The *restricted* product includes only those tuples $(x_v)$ for which $x_p \in \mathbb{Z}_p$ for all but finitely many $p$ [established].

The adele ring is the *global object* that carries the single smooth loop (the real place) and all the discrete trees (the p-adic places) in one structure. In the language of the treatise:

- The adele ring is the **tensor product over all places** — the multiplicative structure that holds the loop and all trees together.
- The restricted product is the **linear discipline** on the global object: only finitely many places may be "active" at once.

### 15.2 The restricted product as a logical limit

[my conjecture] The restricted product is the *logical limit* of the distinction calculus: it is the colimit of the finite products of places, where each finite product is a finite system of loop-and-tree distinctions. The "restriction" (coordinate must be integral for almost all $p$) is the logical form of locality: at almost all places, the mark is at the unit (unmarked) state; only finitely many places carry a nontrivial distinction.

This reading is [my conjecture]; its content is that the adelic structure is not an ad hoc construction of number theory but the natural global object generated by the local distinction calculi.

### 15.3 Adelic dual of the modal pair

The adele ring exhibits the full modal structure of Part II in one object:

- The **global field** (here $\mathbb{Q}$) is the unmarked state — the rational core shared by all completions.
- The **adeles** are the marked global state — the product of all local marks.
- The **ideles** (the unit group of the adeles) are the invertible global states — the symmetries of the global distinction.

This triple (field, adeles, ideles) mirrors the triple of the calculus (unmarked state, marked state, boundary) [MAP — model of the adelic structure].

---

## §16. Tate's Thesis and the Global Fourier Transform

### 16.1 Adelic Fourier analysis

Tate's thesis [established — Tate 1950, Princeton PhD] develops harmonic analysis on the adeles: the Fourier transform on $\mathbb{A}_{\mathbb{Q}}$ is the product of the local Fourier transforms over all places. The adelic Fourier transform is self-dual (Pontryagin duality for the adele group — §11.1):

$$\widehat{\mathbb{A}_{\mathbb{Q}}} \cong \mathbb{A}_{\mathbb{Q}} \quad [\text{established — Tate}]$$

### 16.2 The local Gaussian and local geometric series

Tate's thesis computes the local zeta integrals: at the Archimedean place, the relevant function is the Gaussian $e^{-\pi x^2}$ (the eigenform of the real Fourier transform — §11.2); at each p-adic place, the relevant function is the characteristic function of the unit ball $\mathbb{Z}_p$ (whose Fourier transform is itself — the p-adic eigenform).

[my conjecture] The local eigenforms are the two modes of the re-entrant mark:

- The **Archimedean eigenform** (Gaussian) is the loop mode: the fixed point of the continuous Fourier transform.
- The **p-adic eigenform** (characteristic function of $\mathbb{Z}_p$) is the tree mode: the fixed point of the discrete Fourier transform on the tree.

Both are *eigenforms* — functions fixed by duality — and their existence is the analytic content of the claim that the mark is self-dual under the global Fourier transform.

### 16.3 The unification into the global functional equation

The global zeta integral factors into local integrals, each of which satisfies a local functional equation; the product yields the global functional equation of the zeta function:

$$\xi(s) = \xi(1-s) \quad [\text{established — Riemann's functional equation via Tate}]$$

where $\xi(s)$ is the completed zeta function. The symmetry $s \leftrightarrow 1-s$ is the analytic expression of the global duality — the self-duality of the adeles under the Fourier transform.

---

## §17. The Functional Equation of Zeta as Trace Identity

### 17.1 The completed Riemann zeta function as an adelic trace

The completed zeta function $\xi(s)$ is the *trace* of the adelic Fourier transform: it is computed by the trace formula that Tate's thesis establishes, and the functional equation is the trace identity — a reading that is now [established] in the literature, where the explicit formulas of number theory are realized as a trace formula on the noncommutative space of adele classes (Connes 1999, Selecta Math. 5, 29–106; arXiv:math/9811068) and Weil's explicit formula is formulated as a Lefschetz trace formula on the cohomology of the adeles class space (Connes–Consani–Marcolli 2007, arXiv:math/0703392). What remains conjectural in this treatise is not the trace identity itself but its *re-entrant-modal derivation* — the claim that the loop–tree structure of the mark calculus generates that trace, rather than only re-describing it. That modal derivation is [my conjecture].

$$\xi(s) = \xi(1-s)$$

that expresses the self-duality of the adelic structure under the global Fourier transform (§16.3). The trace-theoretic reading connects this part to Part II (§8.2: the trace as feedback): the zeta function is the *feedback loop* of the global distinction system — the invariant that counts the global structure's self-relations.

The precise content: the explicit formula of analytic number theory (Riemann–von Mangoldt) expresses the prime counting function in terms of the zeros of $\zeta(s)$, and this formula has a trace-theoretic interpretation as the trace of an operator on the adelic space — established in the Connes program (Connes 1999; Connes–Consani–Marcolli 2007; see also the archimedean trace-formula refinement, Connes–Consani 2020, arXiv:2006.13771). The treatise's contribution is the modal reading developed in Appendix C: the specific loop–tree (re-entrant) structure that the trace realizes [my conjecture].

### 17.2 The symmetry s <-> 1-s as a form of duality

The functional equation $s \leftrightarrow 1-s$ is the number-theoretic form of the loop–tree duality:

- The completed zeta function at $s$ (the "loop" argument) equals itself at $1-s$ (the "tree" argument).
- The critical line $\Re(s) = 1/2$ is the fixed point of the duality — the midline between the loop and the tree.

The critical line is the *self-dual axis* of the global distinction: the values of $s$ where the loop and tree readings coincide. This is [MAP — model of the functional equation]; the Riemann hypothesis (all nontrivial zeros on the critical line) is [established — widely believed, unproven] and receives no new proof here.

### 17.3 The zeta function as the global counting of distinctions

[my conjecture] The Euler product of the zeta function

$$\zeta(s) = \prod_p (1 - p^{-s})^{-1} \quad [\text{established — Euler}]$$

is the *global counting of prime distinctions*: each prime is a tree (Part IV, §14), and the zeta function multiplies over all trees the contribution of each tree's branching structure. The functional equation then states that this global count is self-dual — the count of loop structure equals the count of tree structure under the duality.

This reading is [my conjecture]; it is the number-theoretic heart of the treatise's claim that the constants, the primes, and the physical laws all emerge from the single act of distinction.

---

## End of Part IV (Draft v0.1)

### Drafting Notes (internal — remove before publication)

- **Citations verified (P3 gate):** Ostrowski 1918 (canonical journal record), Weil 1967 (book), Continuum Trilogy (10.5281/zenodo.21672990), Natural Units (10.5281/zenodo.21480756).
- **Tate 1950** — verified by canonical record (Princeton PhD). **Bruhat-Tits 1972** and **Euler product** — add to citation list in second pass.
- **Dimensionless mandate (§0.7):** no physics formulas in this part; the zeta function is a pure mathematical object, not a physical formula. The physical application of the adelic structure appears in Part VI.
- **Certainty labels:** applied inline. The modal readings (Ostrowski = loop/tree, Bruhat-Tits = ? modality, adeles = logical limit, zeta = trace identity) are [my conjecture] throughout; the underlying mathematics is [established].
- **Cross-references:** this part connects to the QNFO adelic program (QNFO.ADL) and the Continuum Trilogy's physical-continuum claim.

### Known Risks (from P1 audit)

- The modal reading of Ostrowski (§13.1) is novel — must not overclaim; the classification itself is established, the modal interpretation is conjecture.
- §17.1's "zeta as trace" claim is developed in Appendix C; the appendix must make the trace identity precise or the claim must be downgraded to [MAP].
