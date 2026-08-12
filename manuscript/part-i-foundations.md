# Part I — Foundations: The Act of Distinction

> **WBS:** QNFO.SLB.002.P4.T1 | **Draft:** v0.1 | **Date:** 2026-08-12
> **Status:** FIRST DRAFT — subject to red-team review before publication
> **Genre:** A (Epistemic) — certainty calibration applied inline

---

## Preamble: The Primacy of the Mark

The unmarked state. The first boundary. Why there is something rather than nothing, encoded as the act of drawing a distinction.

This treatise develops a single thesis: that the primitive act of distinction — the drawing of a boundary between marked and unmarked — generates, under the discipline of re-entry and linear resource management, the constants $e$ and $\pi$, the landscape of completions of the rational numbers, the loop–tree duality of the Langlands program, the mathematical structure of quantum theory, and the grammar of a universal logical language. Each part of the treatise is a witness to this thesis in a different domain. This first part establishes the calculus from which everything else is derived.

The foundational claim is mathematical, not metaphysical: the calculus of indications [established — Spencer-Brown 1969] provides a minimal formal system in which the act of distinction is the only primitive. What we add in this treatise is a systematic study of what happens when that mark is allowed to *re-enter* its own form — a move that Spencer-Brown identified as producing the imaginary Boolean value and, with it, the possibility of time [established — Spencer-Brown 1969, Chapter 11]. The further claim of this treatise — that re-entry under linear discipline generates the exponential and circular constants *as logical scalars* — is [my conjecture], developed in Part III. The treatise builds on published predecessors in the calculus of distinction: *Quantum Laws of Form* (DOI 10.5281/zenodo.21205582) and *The Calculus of Distinction: A Formal Isomorphism Between Laws of Form and Ultrametric Trees* (DOI 10.5281/zenodo.21205097). The physical identities developed in Part VI are interpretative re-descriptions of established quantum mechanics, not new predictions; the formal claims of Part III are pre-registered for computational verification.

---

## §1. The Unmarked State and the First Boundary

### 1.1 The void that is not a void

The calculus of indications begins with a state of affairs that Spencer-Brown names the *unmarked state*: no boundary has been drawn, no distinction made [established — Spencer-Brown 1969, p. 1]. The unmarked state is not "nothing" in the physical sense; it is the formal precondition of any act of indication. Every mark presupposes a space in which it can be drawn, and that space — prior to the drawing — is unmarked.

The first act of the calculus is the *drawing of a distinction*. Spencer-Brown's first injunction: *Draw a distinction* [established]. The distinction creates three things simultaneously:

1. A *marked state* (the inside),
2. An *unmarked state* (the outside), and
3. The *boundary* between them.

The mark of distinction is written $\overline{\phantom{x}}$ (or in the older notation, a cross or bracket). The calculus has two primitive acts of condensation and cancellation that generate its arithmetic:

$$\overline{\overline{x}} = x \quad \text{(involution — calling)}$$
$$x \, x = x \quad \text{(idempotence — crossing)}$$

where juxtaposition denotes the operation of *calling* (the copy) and the overbar denotes *crossing* (the mark). These two laws constitute the arithmetic of the calculus [established].

### 1.2 Why the boundary is primal

The central philosophical claim of this section is that the boundary is not an object within the calculus but the act that constitutes the calculus. This claim is [my conjecture] in the strong form stated here; it is [established] that the calculus functions without any other primitive. The *form* of a distinction — the pair of inside and outside separated by a boundary — is the archetype of every subsequent structure in this treatise:

- A **loop** is a boundary that returns to itself.
- A **tree** is a hierarchy of nested boundaries.
- A **constant** is a boundary that persists under every transformation of the calculus.

The loop–tree duality that organizes Parts IV–VIII is present, in embryonic form, in the very act of drawing: a single mark is a trivial loop (its boundary closes); a system of nested marks is a tree.

### 1.3 Falsifiability note

The claim "the boundary is primal" is a choice of axiomatic starting point, not an empirical hypothesis; it is falsifiable only in the sense that the entire derivation program of this treatise could fail — if the constants $e$ and $\pi$ could not be derived from the re-entrant mark under the discipline of Part II, the program would be refuted. This conditional falsifiability is stated here and will be sharpened in §12.

---

## §2. The Calculus of Indications

### 2.1 Arithmetic and algebra

The calculus of indications has two levels:

**Arithmetic.** The arithmetic consists of the two laws of calling and crossing, governing the behavior of marks in the absence of variables:

$$\overline{\overline{x}} = x \quad \text{and} \quad x\,x = x \quad [\text{established}]$$

With two marks $\overline{\phantom{x}}$ and the empty state, the arithmetic produces exactly two distinct values: the marked and the unmarked state. Every well-formed expression evaluates to one of these two values.

**Algebra.** The algebra introduces variables $a, b, c, \ldots$ ranging over the states, and the two laws become:

$$\overline{\overline{a}} = a \quad \text{(involution)}$$
$$a\,a = a \quad \text{(idempotence)}$$

From these, the entire Boolean algebra is recovered: the mark implements negation, juxtaposition implements a form of conjunction (in the marked-inclusive reading), and the calculus is complete for classical propositional logic [established — Spencer-Brown 1969, Chapter 4; see also the extensive literature on the algebraic completeness of the calculus].

### 2.2 The mark as operator and operand

A distinctive feature of the calculus is that the mark serves simultaneously as operator (crossing — the act of negation) and operand (the marked state). This dual role is the first appearance of a theme that recurs throughout the treatise: in linear logic, a formula is both a proposition and a resource; in the re-entrant form, the mark is both the operation and the state it produces. This self-applicative structure is what makes re-entry possible: the mark can be applied to its own form because it is already both operator and operand.

### 2.3 Depth and the algebra of nesting

Spencer-Brown defines the *depth* of an expression as the number of alternations of marked/unmarked regions crossed from the outside [established]. Depth is the discrete scaffolding on which the continuous structures of later parts will be erected. An expression at even depth behaves differently from one at odd depth under crossing, and this parity structure anticipates:

- The sign of the phase in §4 (the half-turn of the mark),
- The parity structure of the Fourier transform in §11,
- The $\mathbb{Z}_2$-grading that underlies the fermionic/bosonic distinction in Part VI.

The appearance of parity in the primitive calculus is [established] (it is a direct consequence of the two laws); the claim that this parity is the ancestor of physical spin-statistics is [my conjecture], developed in Part VI.

---

## §3. Re-Entry and the Imaginary Truth Value

### 3.1 The equation $f = \overline{f}$

The pivotal move of the calculus — and the pivot of this entire treatise — is *re-entry*. A form is allowed to re-enter its own space: the mark is applied to its own result. The simplest re-entrant form satisfies

$$f = \overline{f}.$$

In the arithmetic of the calculus, this equation has no solution: the marked state is not the unmarked state. Spencer-Brown's response was to introduce a *third value*, the imaginary state [established — Spencer-Brown 1969, Chapter 11]. The equation $f = \overline{f}$ oscillates between marked and unmarked; the imaginary value is the name of that oscillation.

### 3.2 The oscillation theorem

The re-entrant form $f = \overline{f}$ generates the sequence

$$\overline{\phantom{x}}, \overline{\overline{\phantom{x}}}, \overline{\overline{\overline{\phantom{x}}}}, \ldots$$

which alternates between the marked and unmarked states. Two readings are possible:

1. **The paradoxical reading:** the form has no stable value in the two-valued arithmetic; it is inconsistent.
2. **The temporal reading:** the form is a clock. Each crossing is a tick; the value is not fixed but *changes*; the form is the simplest possible model of a time-dependent system [established as a reading — Spencer-Brown 1969; Kauffman's extension of the waveform interpretation].

This treatise adopts the temporal reading as its primary interpretation, and this choice is the bridge from logic to process that Parts III–VIII exploit.

### 3.3 The imaginary state as proto-time

[my conjecture] The imaginary state is proto-time: the minimal structure that distinguishes a *before* from an *after* without importing any external notion of duration. The sequence of crossings is discrete; duration arises only when the re-entrant form is coupled to a continuum (Part IV: the Archimedean place) or when many re-entrant forms are synchronized (Part VI: the clock as a system of coupled distinctions).

**Falsifiability condition:** the claim "re-entry generates proto-time" is a claim about the interpretation of a formal system, not about physical time; it is [not yet falsifiable] as a physical claim. Its physical content appears only in Part VI (§24), where it receives a concrete, falsifiable formulation in terms of the Compton frequency. The present section is properly read as establishing the *logical possibility* of time within the calculus.

---

## §4. Time, Oscillation, and the Birth of Frequency

### 4.1 Re-entry as a clock

The re-entrant form $f = \overline{f}$ ticks. If the ticks are indexed by a discrete counter $n \in \mathbb{N}$, the state after $n$ crossings is:

$$f(n) = (-1)^n \, f(0) \quad [\text{established — elementary consequence}]$$

in the Boolean encoding where marked $= 1$, unmarked $= 0$ (equivalently $\pm 1$ under the multiplicative encoding). The discrete clock has period 2.

### 4.2 From discrete ticks to continuous phase

To pass from the discrete clock to a continuous time, we need a parameterization of the *phase* of the oscillation. The minimal continuous model is the unit circle: the marked state corresponds to one half-turn and the unmarked to the other. This is the first appearance of $\pi$ in the treatise: the unit circle's circumference, the half-turn $\pi$ radians that carries the mark to its complement [established — elementary geometry; the *logical* derivation of $\pi$ from the trace of the circle type is the subject of §10 and §36].

The claim that the phase of the re-entrant mark *is* the phase of the unit circle is [MAP — model of the re-entrant oscillation]; the mathematical correspondence is exact, and its physical reading is deferred to Part VI.

### 4.3 Frequency as the rate of re-entry

[my conjecture] Define the *frequency of re-entry* as the number of crossings per unit time. The claim that physical frequency — in particular the Compton frequency of a massive particle — is a rate of re-entry is [TERRITORY — claimed identity] in Part VI (§24), where it is given a precise, falsifiable formulation. In this foundational part, frequency is introduced purely as a rate within the discrete clock, and its connection to the exponential $e^{i\theta}$ phase factor is prepared:

$$e^{i\theta} = \cos\theta + i\sin\theta \quad [\text{established — Euler's formula, see §12}]$$

The half-turn of the mark corresponds to $\theta = \pi$: $e^{i\pi} = -1$, the marked state under the multiplicative encoding. The full derivation of the Euler identity from the calculus is the subject of §12; the present section establishes the geometric picture.

### 4.4 The transition from static logic to dynamic process

The passage from Part I to Part II is the passage from a *static* calculus (the arithmetic and algebra of indications) to a *dynamic* one (re-entry, oscillation, phase). The discipline imposed in Part II — linear logic's resource management — governs *how* the mark may be copied, reused, and discarded. It is the linear discipline that turns the raw oscillation of §3 into the structured exponential and circular constants of Part III.

The unit circle as the space of phases is [established] as a mathematical object; its role as the canonical phase space of the re-entrant mark is [MAP — model of the phase space].

---

## End of Part I (Draft v0.1)

### Drafting Notes (internal — remove before publication)

- **Citations verified:** Spencer-Brown 1969 (book, no DOI — canonical record); Euler identity deferred to §12 with full derivation.
- **Certainty labels:** applied inline per QNFO Core §0.0. Novel claims marked [my conjecture]; interpretive claims marked [MAP]; identity claims in Part VI marked [TERRITORY] with falsifiability conditions.
- **Banned words check:** none of the §0.0 banned words (reality, fundamental, essence, truly, deeply, profoundly, actually, basically, merely, essentially, obviously, clearly) used. Verify at compile.
- **Mojibake check:** pending — run scan-mojibake.py before commit.
- **Ostrowski dimensionlessness:** no dimensional physics formulas in this part; first physics formulas appear in Part VI and will be written in dimensionless Planck units per §0.7.
- **Missing:** the detailed algebraic completeness proof of §2 (standard — cite textbook), the full formal treatment of the imaginary value (follow Kauffman's waveform algebra), and the discrete-to-continuous limit argument (§4.2) which currently relies on geometric intuition. These are flagged for the P4.T1 second pass.

### Known Risks (from P1 audit)

- §4.2's "first appearance of π" claim must not pre-empt §10's logical derivation; the geometric picture here is motivation, not derivation.
- The proto-time claim (§3.3) must remain [not yet falsifiable] until §24 gives it physical content.
