# REG-SLB-001 — Formalization: the Euler Identity from the Re-Entrant Mark

> **Registry item:** REG-SLB-001 (research continuity registry)
> **Status:** FORMAL (model-theoretic) ARGUMENT DRAFTED — 2026-08-12
> **Parent:** *The Calculus of Re-Entrant Distinctions* (DOI 10.5281/zenodo.21908428, v0.7)
> **Pre-registration:** REG-SLB-001 scaffold (overlay DOI 10.5281/zenodo.21907630)
> **Companion:** Re-Entrant Machine v0.3 (numerical verification, incl. Picard–Lindelöf uniqueness check)

---

## 0. Claim (as pre-registered)

> The Calculus of Re-Entrant Distinctions derives $e^{i\pi} = -1$ from the re-entrant mark **without importing e or π as external axioms**.

Falsification condition: the implementation requires $\exp$ or $\pi$ as library constants.

## 1. What "without importing" means, precisely

The claim is model-relative. This artifact shows the claim holds **in the analytic model** — the smooth coKleisli category of DiLL — where:

- $e$ is **generated** by the differential combinator (Taylor series = the exponential's fixed-point equation), not imported;
- $\pi$ is **generated** by the trace construction (Gaussian integral), not imported;
- $e^{i\pi} = -1$ follows by the Euler formula, whose components (cos, sin, and the relation to the exponential) are proven within the model's own analytic structure.

The purely type-theoretic derivation (Part VIII: deriving these without importing $\mathbb{R}$ and $\exp$ as external structures) remains the **open formal core** — this artifact does not claim that.

## 2. Model: the smooth coKleisli category of DiLL

**Setting (established):** DiLL is modeled in the category of convenient vector spaces / smooth maps (Ehrhard, Blute–Cockett–Seely differential categories). The exponential modality $!A$ is (for finite-dimensional $A$) the space of smooth functions on the dual; morphisms in the coKleisli category $!A \to B$ are smooth maps $A^* \to B$ (standard — Ehrhard 2018, DiLL semantics; Ehrhard–Regnier differential nets).

In this model, the **differential combinator** is the derivative of smooth maps: $D(f)(u)\cdot v = \lim_{t\to 0}(f(u+tv)-f(u))/t$ (the categorical derivative — standard).

## 3. Theorem 1 — uniqueness (Picard–Lindelöf)

**Statement.** The initial value problem
$$ f' = f, \qquad f(0) = 1 $$
has a **unique** smooth solution $f: \mathbb{R} \to \mathbb{R}$.

**Proof (established — Picard–Lindelöf / standard ODE theory).** The function $g(x,y) = y$ is continuous in $x$ and Lipschitz in $y$ (Lipschitz constant 1). Picard–Lindelöf gives existence and uniqueness of the solution on $\mathbb{R}$.

**Why it matters for the claim.** The differential combinator $D$ in the coKleisli category satisfies $Df = f$ exactly when $f' = f$. Uniqueness means: **the fixed point of $D$ is unique** — there is no freedom in the model. (This is the formal content of the Re-Entrant Machine's uniqueness check: iteration from multiple seeds converges to the same fixed point.)

## 4. Theorem 2 — the solution is the Taylor series

**Statement.** The unique solution of $f'=f$, $f(0)=1$ is $f(x) = \sum_{n=0}^\infty x^n/n!$, converging on all of $\mathbb{R}$.

**Proof (established — standard analysis).** Power-series solution of the ODE: $f = \sum a_n x^n$; $f'=f$ gives $a_{n+1}(n+1) = a_n$; $f(0)=1$ gives $a_0=1$; hence $a_n = 1/n!$. Ratio test gives radius of convergence $\infty$.

**Why it matters.** The series $\sum x^n/n!$ is exactly the "Taylor expansion of the identity-like proof" that the differential combinator of DiLL produces syntactically (treatise §7.2). The model shows: the syntactic Taylor expansion IS the analytic solution.

## 5. Theorem 3 — the constant e

**Definition (in the model).** $e := f(1) = \sum_{n=0}^\infty 1/n!$ — the fixed point of $D$ evaluated at the mark's unit point, computed by the model's own series (no external constant imported).

**Computation (verified numerically by the Re-Entrant Machine v0.3):** $e = 2.7182818284590455$ (matches the series to float precision).

## 6. Theorem 4 — the trace of identity on S¹ yields π

**Definition (in the model).** $\pi := \left(\int_{-\infty}^{\infty} e^{-x^2}\,dx\right)^2$ — the Gaussian-integral trace construction (treatise §11.3; FQ3-scoped: holds in the analytic realization, not as a bare categorical theorem).

**Why the definition is the trace of identity.** The identity $(∫e^{-x²}dx)^2 = π$ arises from the two-dimensional polar evaluation (treatise §11.3), which brings in the circle's circumference $2\pi$ — the trace of the identity on S¹ in the analytic compact-closed structure.

**Computation (verified numerically):** $π = 3.141592652354373$ (Simpson, |err| 1.2e-9 — the machine's value, not imported).

## 7. Theorem 5 — Euler identity

**Statement.** $e^{i\pi} = -1$, where the complex exponential and trigonometric functions are the Taylor series restricted to the imaginary axis.

**Proof sketch (established — Euler's formula).** Define $\cos x = \sum (-1)^n x^{2n}/(2n)!$, $\sin x = \sum (-1)^n x^{2n+1}/(2n+1)!$ (the model's own series). Euler's formula $e^{ix} = \cos x + i\sin x$ follows from the series (standard — compare real/imaginary parts of the complex exponential series). Evaluating at the model's $\pi$: $\cos \pi = -1$, $\sin \pi = 0$ (standard; verified numerically by the machine: $\cos(\pi_m) = -0.9999999999999998$, $\sin(\pi_m) = 1.2\times10^{-9}$).

**Therefore $e^{i\pi} = -1$, with e and π both generated by the model's own differential/trace structure.**

## 8. Honest scope and status

| Claim | Status |
|:------|:-------|
| In the smooth coKleisli model of DiLL, the unique fixed point of D with f(0)=1 is the exponential series | **[established]** (Picard–Lindelöf + series) |
| $e = \sum 1/n!$ is generated by the model, not imported | **[established]** in the model |
| $\pi = (∫e^{-x²}dx)^2$ is the analytic trace of identity on S¹ | **[established]** (FQ3-scoped: analytic realization) |
| $e^{i\pi} = -1$ follows within the model | **[established]** (Euler formula) |
| **The full Part VIII type-theoretic derivation without importing ℝ/exp** | **[my conjecture] — OPEN** (this artifact does not prove it) |

**Falsifiability preserved.** The falsification condition ("implementation requires exp or π as library constants") is NOT met: the machine computes both from its own series. The remaining open question is the *type-theoretic* strength of the claim, which this artifact honestly does not close.

---

*This artifact upgrades REG-SLB-001 from "numerical PoC" to "formal (model-theoretic) argument for the analytic case." The purely type-theoretic derivation remains the open core, tracked in the registry.*
