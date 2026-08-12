# Part II — The Logical Substrate: Linear and Differential Refinements

> **WBS:** QNFO.SLB.002.P4.T1 | **Draft:** v0.1 | **Date:** 2026-08-12
> **Status:** FIRST DRAFT — subject to red-team review before publication
> **Genre:** A (Epistemic) — certainty calibration applied inline

---

## §5. Linear Logic and Resource-Conscious Distinction

### 5.1 The mark as a linear resource

Part I established the mark of distinction as the primitive of the calculus. Part II asks a new question: *what does it cost to use a mark?* The answer, following Girard's linear logic [established — Girard 1987, DOI 10.1016/0304-3975(87)90045-4], is that every use of a hypothesis consumes it. In classical and intuitionistic logic, a hypothesis may be used any number of times; in linear logic, it must be used exactly once — unless an explicit modality licenses copying or discarding.

The correspondence at the heart of this section:

| Calculus of Indications | Linear Logic |
|:------------------------|:-------------|
| Mark as operand | Linear formula (resource) |
| Mark as operator | Linear implication $\multimap$ |
| Calling (copy) | Controlled by the exponential $!$ |
| Crossing (negation) | Linear negation $(\cdot)^\perp$ |
| Depth | Modality depth / dereliction levels |

This table is the first of several "Rosetta stone" correspondences in the treatise (the full crosswalk appears in §38). It is [MAP — model of the LoF/linear-logic correspondence]: the correspondence is exact at the level of proof structure, and its exploitation throughout this treatise is a design choice, not an empirical claim.

### 5.2 Multiplicative and additive connectives

Linear logic's connectives split into two families [established — Girard 1987]:

**Multiplicatives** (the logic of *parallel* resources):
- Tensor $A \otimes B$: both resources, used together.
- Par $A \parr B$: both alternatives available; the ambient environment chooses which is consumed.
- Linear implication $A \multimap B = A^\perp \parr B$: the resource-transformer.

**Additives** (the logic of *choice*):
- With $A \& B$: the environment chooses which resource is delivered.
- Plus $A \oplus B$: the proof chooses which resource is produced.

The multiplicative/additive distinction is the logical ancestor of the loop/tree distinction that organizes this treatise:

- Multiplicative structure is **looping**: tensor and par both involve the interaction of *two* resources, the minimal graph with a cycle (the exchange/cut structure).
- Additive structure is **branching**: with and plus are binary choices, the minimal tree.

[my conjecture] The claim that multiplicative = loop and additive = tree is a structural correspondence between proof theory and graph theory: multiplicative connectives preserve the cyclic exchange symmetry of their resources, while additive connectives introduce genuine branching. This correspondence is exact for the graphical presentation of proofs (proof nets [established — Girard 1987]), and the treatise develops it in Parts IV and V.

### 5.3 The distinction that cannot be duplicated without control

The key linearity principle: without the exponential $!$, a distinction (hypothesis, resource, mark) cannot be duplicated. This is the *resource-conscious refinement* of the calculus of indications: Spencer-Brown's calling law $x\,x = x$ (idempotence — a mark copied is still one mark) is the *unrestricted* form; linear logic restricts it, requiring an explicit modality to license copying.

[my conjecture] This restriction is the formal seed of the physical principle of non-cloning in quantum theory (Part VI, §26). The no-cloning theorem of quantum mechanics [established — Wootters & Zurek 1982; Dieks 1982] states that an unknown quantum state cannot be duplicated. The treatise's claim is that this is the *physical reading* of linearity: quantum states are linear resources. The claim is [TERRITORY — claimed identity] in Part VI, with its falsifiability condition stated there.

---

## §6. The Exponential Modalities: $!$ and $?$

### 6.1 $!A$ — unlimited copying, the continuous loop

The exponential modality $!A$ (pronounced "of course $A$") licenses unlimited use of $A$: from $!A$ one may derive any number of copies of $A$ [established — Girard 1987]. The rules:

$$\frac{\Gamma \vdash B}{\Gamma, !A \vdash B} \; (weakening) \qquad
  \frac{\Gamma, !A, !A \vdash B}{\Gamma, !A \vdash B} \; (contraction) \qquad
  \frac{! \Gamma \vdash B}{! \Gamma \vdash !B} \; (promotion)$$

The central observation of this section: $!A$ is the *continuous loop* — a resource that can be fed back into itself without loss. The promotion rule internalizes the loop: from a proof that uses the resource, it produces a resource that can be reused indefinitely.

[my conjecture] The modality $!$ is the logical counterpart of the re-entrant mark's *steady oscillation*: where the raw re-entrant form $f = \overline{f}$ oscillates (Part I, §3), the promoted resource $!A$ is the *stabilized* form — a loop that has reached a fixed point, circulating without changing. The connection to the exponential function $e^x$ — whose defining property is that it is its own derivative, i.e. its own rate of circulation — is the subject of Part III, §9.

### 6.2 $?A$ — the dual branching, the discrete tree

The dual exponential $?A$ (pronounced "why not $A$") licenses the *environment's* unlimited use of $A$. It is the De Morgan dual of $!A$:

$$(?A)^\perp = !(A^\perp) \quad [\text{established — Girard 1987}]$$

[my conjecture] $?A$ is the *discrete tree*: the branching structure that results when an unlimited resource is consumed by an environment that can discard or duplicate it at will. The tree metaphor is made precise in Part IV (§14) where the $?$ modality is realized as the geometric structure of a $p$-adic tree (Bruhat–Tits building).

### 6.3 The loop–tree duality as modal duality

The pair $(!, ?)$ is the first precise statement of the loop–tree duality:

- $!$ — the loop: copying without loss, circulation, continuity.
- $?$ — the tree: branching, discrete choice, discontinuity.

This duality is De Morgan dual: each is the negation of the other. The treatise's thesis is that this modal duality is the logical skeleton of the mathematical duality between the real (Archimedean) place and the $p$-adic (non-Archimedean) places of Ostrowski's theorem (Part IV, §13), and between automorphic forms and Galois representations (Part V, §20).

---

## §7. Differential Linear Logic and the Derivative as a Proof Rule

### 7.1 The differential combinator

Differential linear logic (DiLL) extends linear logic with a *differential combinator* that linearizes proofs [established — Ehrhard & Regnier 2006, DOI 10.1016/j.tcs.2006.08.003; Ehrhard 2018, DOI 10.1017/S0960129516000372]. Where linear logic governs *how resources are used*, DiLL governs *how proofs can be varied*. The differential combinator $D$ satisfies:

$$D(f)(u)\cdot v = \text{the derivative of } f \text{ at } u \text{ in direction } v$$

In DiLL, the differential combinator is a proof rule: from a proof of $A \multimap B$ one may derive a proof of $A \otimes A \multimap B$ — the linear approximation of the original proof [established — Ehrhard & Regnier 2006].

### 7.2 Linear approximation and the derivative of a proof

The central insight of DiLL [established — Ehrhard & Regnier 2006]: the Taylor expansion of a proof. Any proof $f$ can be written as a sum (in a suitable sense) of its derivatives:

$$f = \sum_{n=0}^{\infty} \frac{1}{n!} D^n f(0)$$

This is the *Taylor expansion of a proof*, and it is the bridge from the discrete combinatorics of proofs to the continuous analytic structure of the exponential function.

[my conjecture] The derivative of a proof is the *rate of change of a distinction*: the differential combinator measures how a marked/unmarked configuration responds to infinitesimal perturbation. This is the logical seed of the physical derivative — the operator $d/dt$ of dynamics — and the treatise's claim is that the differential combinator of DiLL is the proof-theoretic ancestor of the differential structure of physics (Part VI, and the differential cohesion of Part VIII, §35).

### 7.3 The exponential map emerges syntactically

The decisive observation for Part III: the Taylor expansion of the *identity-like* proof produces the exponential series

$$e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}$$

entirely syntactically, from the differential combinator and the exponential modality [established — the Taylor series; the claim that this *is* the syntactic emergence of $e$ is [my conjecture], developed in §9]. The exponential function is not added to the calculus from outside; it is generated by the calculus's own differential structure.

---

## §8. The Geometry of Interaction and Traced Categories

### 8.1 Cut-elimination as a dynamical system

The Geometry of Interaction (GoI) program [established — Girard 1989, DOI 10.1017/S0305004100074338; Abramsky 2005] interprets proofs as dynamical systems: cut-elimination is not a static rewriting process but the *time-evolution* of an interaction. A proof is a network; its execution is the flow of tokens through the network; the result of cut-elimination is the fixed point of that flow.

The GoI interpretation is the first place in the treatise where *time* appears as an internal feature of proof theory — echoing the temporal reading of the re-entrant mark in Part I, §3. The re-entrant mark and the GoI token are [MAP — model of each other]: both are primitive dynamical processes whose equilibrium is a fixed point.

### 8.2 The trace as feedback

The mathematical structure underlying GoI is the *trace* of a monoidal category [established — Joyal, Street & Verity 1996]. The trace operation $Tr$ takes a morphism $f: A \otimes U \to B \otimes U$ and produces $Tr^U(f): A \to B$, "closing the loop" on the shared resource $U$ — feeding $U$ back into itself.

The trace is the categorical formalization of **feedback**: a system whose output is routed back into its input. The connection to the re-entrant mark is direct: re-entry is feedback, and the trace is its categorical form.

### 8.3 Compact closed categories as the algebra of self-reference

A compact closed category is a symmetric monoidal category in which every object $A$ has a dual $A^*$ with evaluation $A^* \otimes A \to I$ and coevaluation $I \to A \otimes A^*$ [established — Joyal, Street & Verity 1996]. In a compact closed category, the trace always exists.

[my conjecture] Compact closed categories are the algebra of self-reference: the coevaluation $I \to A \otimes A^*$ creates a "self" (the object paired with its dual), and the trace closes the self-referential loop. The re-entrant mark $f = \overline{f}$ is the simplest instance: the object and its negation, traced into a loop. This claim is [MAP — model of self-reference]; its formal content is that the calculus of the re-entrant mark embeds into compact closed structure, which Part III uses to derive the constants.

### 8.4 The bridge to Part III

Part II has established the logical substrate: linear discipline (§5), the modal pair of loop and tree (§6), the differential combinator (§7), and the traced/compact-closed structure of feedback (§8). Part III now asks: what constants does this substrate force into existence? The answer — the exponential constant $e$ from the fixed point of the differential exponential, and the circular constant $\pi$ from the trace of the circle — is the treatise's central technical contribution.

---

## End of Part II (Draft v0.1)

### Drafting Notes (internal — remove before publication)

- **Citations verified (P3 gate):** Girard 1987 (10.1016/0304-3975(87)90045-4), Ehrhard & Regnier 2006 (10.1016/j.tcs.2006.08.003), Ehrhard 2018 (10.1017/S0960129516000372), Joyal-Street-Verity 1996 (10.1017/S0305004100074338), Selinger 2010 (10.1007/978-3-642-12821-9_4). Abramsky 2005 and Blute-Cockett-Seely 2006 in P2 survey; Blute-Cockett-Seely verified via search (10.70930/tac/y9rglypb).
- **Wootters-Zurek 1982 / Dieks 1982 no-cloning** — must be added to the citation list in the P4 second pass (P2 survey omitted them; they are required by §5.3).
- **Certainty labels:** applied inline per §0.0.
- **Banned words check:** none used. Verify at compile.
- **Missing:** the full proof-net presentation of §5.2, the categorical semantics details of §8 (deferred to Appendix A), and the explicit statement of the trace formulas that Part III will use. These are flagged for the second pass.

### Known Risks (from P1 audit)

- §5.3's no-cloning correspondence must carry a [TERRITORY] label with a falsifiability condition in Part VI — it is flagged here and will be fully discharged there.
- §6.1's "steady oscillation" of $!A$ needs a precise formal statement (fixed-point semantics of the modality) in the second pass; the current phrasing is motivational.
