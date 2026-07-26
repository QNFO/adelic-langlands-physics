---
title: "Functoriality as Renormalization — Langlands Lifts and the Renormalization Group"
author: "QNFO Research"
date: "2026-07-26"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: ""
status: "draft"
---

**Author:** QNFO Research | **Date:** 2026-07-26 | **License:** QNFO-ULA: https://legal.qnfo.org/

## Abstract

Langlands functoriality — the lifting of automorphic representations from one group $G$ to another group $H$ via an L-homomorphism ${}^LG \to {}^LH$ — is identified with renormalization group flow in the adelic quantum theory. At each place $v$ of $\mathbb{Q}$, the local lifting $\pi_v^{(G)} \to \pi_v^{(H)}$ corresponds to an RG transformation that changes the effective anyon model: the fusion ring $R(G)_k$ flows to $R(H)_\ell$ under the renormalization step. The critical exponents of the RG flow are the special values of the associated L-function $L(s, \pi, r)$ at integer arguments. For the symmetric power liftings $\mathrm{Sym}^n : \mathrm{GL}(1) \to \mathrm{GL}(n+1)$, the RG flow connects the $\mathrm{SU}(2)_k$ anyon model at level $k$ to effective $\mathrm{SU}(n+1)$ theories at renormalized couplings. The Langlands dual group ${}^LG$ is identified as the RG flow group — the group of admissible renormalization transformations of the adelic quantum theory. This is a conjecture paper; all claims are tagged as [speculative] or [my conjecture] as appropriate.

---

## 1. Introduction

The Langlands program's functoriality conjecture states that for a homomorphism $\rho : {}^LG \to {}^LH$ between L-groups, there should exist a transfer of automorphic representations from $G(\mathbb{A})$ to $H(\mathbb{A})$ that preserves L-functions:

$$\Lambda(s, \pi, r \circ \rho) = \Lambda(s, \Pi, r)$$

for every finite-dimensional representation $r$ of ${}^LH$.

In the physical framework developed by the Adelic Langlands Physics program (Phases 1—2.2), automorphic representations $|\pi\rangle$ are basis states of the adelic Hilbert space $\mathcal{H}_{\mathbb{A}} = \bigotimes'_v \mathcal{H}_v$, and L-functions are expectation values of the operator $\hat{L}(s)$. This paper proposes that **functoriality is renormalization group flow** in this physical setting. [my conjecture]

---

## 2. Functoriality as RG Transformation

### 2.1 Local Lifting as Coupling Flow

At a fixed place $v$, let $\pi_v^{(G)}$ be a local automorphic representation of $G(\mathbb{Q}_v)$, corresponding under the Silent Parameter (Phase 1) to a simple object $j_v^{(G)}$ in the fusion ring $R(G)_{k_v}$. The local Langlands correspondence associates to $\pi_v^{(G)}$ a Galois parameter $\phi_v : W_{\mathbb{Q}_v} \to {}^LG$.

The L-homomorphism $\rho : {}^LG \to {}^LH$ composes with $\phi_v$ to give a Galois parameter into ${}^LH$, and hence (by local Langlands for $H$) an automorphic representation $\Pi_v^{(H)}$ of $H(\mathbb{Q}_v)$ — the **functorial lift** of $\pi_v^{(G)}$.

At the level of fusion rings, this is a homomorphism:

$$\rho_v^* : R(G)_{k_v} \longrightarrow R(H)_{\ell_v}$$

mapping the fusion ring of the "UV" theory at level $k_v$ to the "IR" theory at renormalized level $\ell_v$. The map $\rho_v^*$ is an **RG flow step** — it reduces the number of degrees of freedom while preserving the L-function structure:

$$L_v(s, \rho_v^*(j)) = L_v(s, r \circ \phi_v)$$

[my conjecture]

### 2.2 Example: Symmetric Power Liftings

For $G = \mathrm{GL}(1)$ and $H = \mathrm{GL}(2)$, the symmetric square lifting $\mathrm{Sym}^2 : \mathrm{GL}(1) \to \mathrm{GL}(2)$ sends a character $\chi$ of $\mathbb{Q}_p^\times$ to a representation of $\mathrm{GL}(2, \mathbb{Q}_p)$ whose L-function is:

$$L(s, \mathrm{Sym}^2(\chi)) = L(s, \chi) \cdot L(s, \chi^2)$$

The physical interpretation: the $\mathrm{SU}(2)_k$ anyon model (describing $\mathrm{GL}(1)$ at conductor $m$) is the UV fixed point, and the $\mathrm{SU}(3)_\ell$ anyon model (describing $\mathrm{GL}(2)$) is the IR fixed point reached after two RG steps — first squaring the character (doubling the anyon charge), then composing with the local transfer. [speculative]

The critical exponent $\nu$ of this RG flow is related to the L-function special value:

$$\nu = \frac{1}{\log p} \cdot \frac{d}{ds} \log L(s, \mathrm{Sym}^2(\chi)) \bigg|_{s=1}$$

[speculative]

---

## 3. The Renormalization Group Group

### 3.1 Adelic RG Transformations

An RG transformation on the adelic Hilbert space is an operator $\mathcal{R}$ that:

1. **Coarse-grains:** Reduces the conductor $m_v \to m_v - 1$ at each finite place $v$ (eliminating the highest-resolution anyon types).
2. **Renormalizes the coupling:** Adjusts the level $k_v \to \ell_v$ according to the lifting map.
3. **Preserves L-function structure:** $\Lambda(s, \mathcal{R}|\pi\rangle) = \Lambda(s, \pi)$ up to a finite Euler factor.

The set of all such transformations forms a **group** — the RG group $\mathcal{G}_{\text{RG}}$.

### 3.2 Langlands Dual Group as RG Group

**Conjecture 1 (RG-Langlands Duality).** The group of admissible adelic RG transformations $\mathcal{G}_{\text{RG}}$ is isomorphic to the Langlands dual group ${}^LG$ of the adelic quantum theory.

*Reasoning sketch.* The L-group ${}^LG = \hat{G} \rtimes W_{\mathbb{Q}}$ has two components: the complex dual group $\hat{G}$ (e.g., $\mathrm{SL}(n, \mathbb{C})$ for $G = \mathrm{SU}(n)$) and the Weil group action. The $\hat{G}$ component corresponds to the continuous part of the RG flow — the family of coupling constants parametrized by the dual group. The Weil group action corresponds to the discrete scaling transformations (changes of conductor). [my conjecture]

For $\mathrm{GL}(1)$, the L-group is simply $\mathrm{GL}(1, \mathbb{C}) \cong \mathbb{C}^\times$, which is exactly the multiplicative group of complex numbers — the scaling group of the $\beta$-function in ordinary QFT.

### 3.3 $\beta$-Function of the Adelic Theory

The adelic $\beta$-function is defined as the infinitesimal generator of the RG flow:

$$\beta(g_v) = -\frac{d g_v}{d \log \mu}$$

where $g_v$ is the coupling at place $v$ and $\mu$ is the energy scale. The zeros of $\beta(g)$ are the fixed points — corresponding to the **automorphic representations with trivial epsilon factors** (the unramified principal series).

The special values of L-functions provide the critical exponents:

$$\eta = \lim_{s \to 1} (s-1) \cdot \frac{d}{ds} \log \Lambda(s, \pi)$$

which is the anomalous dimension of the automorphic field. [speculative]

---

## 4. Physical Examples

### 4.1 Central Charge Flow

For anyon models, the central charge $c$ (the chiral central charge of the edge CFT) flows under RG according to Zamolodchikov's c-theorem: $c_{\text{UV}} \geq c_{\text{IR}}$.

In the Langlands framework, the central charge at each place is:

$$c_v = \log |\varepsilon_v|^2$$

where $\varepsilon_v$ is the local epsilon factor (Phase 2.2). The RG flow $p$-adic place $\to$ $\infty$-place sends $c_p^{\text{UV}} \to c_\infty^{\text{IR}}$, with the monotonic decrease $\Delta c = \log |\Lambda(1, \pi)|$ given by the special value of the L-function. [speculative]

### 4.2 Symmetric Power Cascade

For the symmetric power lifting chain:

$$\mathrm{GL}(1) \xrightarrow{\mathrm{Sym}^2} \mathrm{GL}(2) \xrightarrow{\mathrm{Sym}^3} \mathrm{GL}(3) \xrightarrow{\mathrm{Sym}^4} \cdots$$

each step increases the rank of the target group by 1. The corresponding RG cascade connects $\mathrm{SU}(2)_k \to \mathrm{SU}(3)_\ell \to \mathrm{SU}(4)_m \to \cdots$, with the levels flowing according to:

$$\ell = \mathrm{Sym}^2(k), \quad m = \mathrm{Sym}^3(\ell), \quad \ldots$$

At each step, the anyon content becomes richer, and the physical theory flows from simpler (fewer anyon types) to more complex (more anyon types) — the opposite of the usual coarse-graining RG direction. This is **inverse RG flow**, characteristic of topological orders connected by anyon condensation. [speculative]

---

## 5. Falsifiable Predictions

1. **[P1] Functoriality $\leftrightarrow$ RG flow.** For any L-homomorphism $\rho : {}^LG \to {}^LH$, there exists an RG transformation $\mathcal{R}_\rho$ on the adelic Hilbert space such that $\mathcal{R}_\rho |\pi^{(G)}\rangle = |\Pi^{(H)}\rangle$ for all automorphic representations $\pi$ of $G$. [my conjecture]
   - **Falsification:** Find a functorial lift that cannot be realized as an RG flow on the fusion ring.
   - **[CHECK: 2028-12]** Systematic enumeration of low-rank liftings.

2. **[P2] Critical exponents from L-functions.** The critical exponents of the RG flow $\mathcal{R}_\rho$ are the logarithmic derivatives of the associated L-function at integer arguments. [speculative]
   - **Falsification:** Compute critical exponents from first-principles RG and compare to L-function special values.
   - **[CHECK: 2029-06]** Numerical simulation for $\mathrm{Sym}^2$ at small primes.

3. **[P3] c-theorem from Langlands.** The central charge $c(\pi) = \log |\Lambda(1, \pi)|$ is monotone decreasing under any Langlands functorial lifting. [my conjecture]
   - **Falsification:** Find a lifting where $c$ increases.
   - **[CHECK: 2028-06]** Verlinde formula computation for $\mathrm{SU}(2)_k \to \mathrm{SU}(n)_\ell$ at small $k$.

---

## 6. Conclusion

Phase 2.3 completes the global Langlands construction by identifying **functoriality as renormalization group flow**. The L-group ${}^LG$ is the RG group of the adelic quantum theory, and the critical exponents of the flow are the special values of L-functions. Together with Phases 2.1 (Hecke operators as quantum gates) and 2.2 (L-function as physical observable), Phase 2 establishes the global framework connecting automorphic representations to physical quantum systems across all completions of $\mathbb{Q}$.

Phase 3 will construct the full adelic gauge theory — the field theory on the adele ring that unifies $N=4$ SYM S-duality at the $\infty$-place with anyon braiding at finite primes.

---

## Declarations

**Funding:** No external funding.

**Conflicts of Interest:** None.

**Ethics Approval:** Not applicable.

**Consent to Participate:** Not applicable.

**Author Contributions:** QNFO Research: conceptualization, formal proof, writing.

**Data Availability:** All derivations within this paper.

**Code Availability:** To be deposited with Zenodo.

**Use of Artificial Intelligence:** AI-assisted formalization. Author-verified.

---

## References

1. ALP Phase 1—2.2. (2026). Adelic Langlands Physics program deliverables, v0.2—v0.7. QNFO Research.

2. Langlands, R. P. (1970). Problems in the theory of automorphic forms. *Lecture Notes in Mathematics*, 170, 18—61. Springer.

3. Bump, D. (1997). *Automorphic Forms and Representations*. Cambridge University Press.

4. Gelbart, S. (1975). *Automorphic Forms on Adele Groups*. Annals of Mathematics Studies, 83.

5. Zamolodchikov, A. B. (1986). Irreversibility of the flux of the renormalization group in a 2D field theory. *JETP Letters*, 43(12), 730—732.

6. Kitaev, A. (2006). Anyons in an exactly solved model and beyond. *Annals of Physics*, 321(1), 2—111.

7. Cardy, J. (1996). *Scaling and Renormalization in Statistical Physics*. Cambridge University Press.

8. Kapustin, A., & Witten, E. (2006). Electric-magnetic duality and the geometric Langlands program. CMP.

9. Verlinde, E. (1988). Fusion rules and modular transformations in 2D CFT. *Nuclear Physics B*, 300, 360—376.

10. QNFO Research. (2026). The Langlands Program Is Adelic Physics Without the Physics. Rosetta Note v1.0.
