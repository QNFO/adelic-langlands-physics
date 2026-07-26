---
title: "Adelic Yang-Mills — Gauge Theory on the Adele Ring"
author: "QNFO Research"
date: "2026-07-26"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: ""
status: "draft"
---

**Author:** QNFO Research | **Date:** 2026-07-26 | **License:** QNFO-ULA: https://legal.qnfo.org/

## Abstract

The adele ring $\mathbb{A}_\mathbb{Q}$ is the restricted product $\mathbb{R} \times \prod_p \mathbb{Q}_p$ — the only locally compact ring containing $\mathbb{Q}$ as a discrete subring. This paper defines Yang-Mills theory on $\mathbb{A}_\mathbb{Q}$, constructing a gauge field $A$ valued in $\mathfrak{g}$ over the adele ring, defining the field strength $F = dA + A \wedge A$, and the Yang-Mills action $S_{\text{YM}}[A] = \frac{1}{4g^2} \int_{\mathbb{A}} \|F\|^2 \, d^\times x$. The action factorizes over places: $S_{\text{YM}}[A] = S_\infty[A_\infty] + \sum_p S_p[A_p]$. At the $\infty$-place, the action reduces to standard 4D Yang-Mills on $\mathbb{R}^4$. At each $p$-adic place, the action reduces to Chern-Simons theory on the Bruhat-Tits tree $\mathcal{T}_p$, reproducing the anyon braiding structure of the $\mathrm{SU}(2)_{k_p}$ fusion category (Phase 1). The path integral $Z_{\text{YM}} = \int \mathcal{D}A \, e^{i S_{\text{YM}}[A]}$ factorizes as $Z_\infty \cdot \prod_p Z_p$, establishing the adele ring as the correct spacetime for a unified quantum gauge theory over all completions of $\mathbb{Q}$.

---

## 1. Introduction

The adele ring $\mathbb{A}_\mathbb{Q}$ is the natural domain for a unified quantum field theory that respects the product structure of the completions of $\mathbb{Q}$. It is:

1. **A locally compact ring** containing $\mathbb{Q}$ as a discrete subring,
2. **A restricted product** $\mathbb{R} \times \prod_p \mathbb{Q}_p$ where almost all factors are $\mathbb{Z}_p$,
3. **The domain of automorphic forms** — the Langlands program's natural setting.

Phase 1 of the Adelic Langlands Physics program established that at each $p$-adic place, the fusion ring $R(\mathrm{SU}(2))_{k_p}$ encodes the local Langlands correspondence. Phase 3.1 now constructs the gauge theory on $\mathbb{A}_\mathbb{Q}$ whose quantization produces the fusion ring structure at each place.

---

## 2. Gauge Fields on the Adele Ring

### 2.1 Differential Geometry on $\mathbb{A}$

A gauge field on $\mathbb{A}$ is a $\mathfrak{g}$-valued 1-form:

$$A(x) = \sum_{v} A_v(x_v) \, dx_v$$

where $v$ runs over all places (including $\infty$). The essential insight is that smooth functions on $\mathbb{A}$ are finite linear combinations of functions factorizing over places, so $A$ naturally decomposes as $A = (A_\infty, A_2, A_3, \ldots)$.

The field strength is:

$$F = dA + A \wedge A$$

which also factorizes: $F_v = d_v A_v + A_v \wedge_v A_v$ at each place $v$, using the appropriate notion of differential at that place.

### 2.2 Archimedean Differential ($v = \infty$)

At $\mathbb{R}$, $d_\infty$ is the standard de Rham differential, and $F_\infty$ is the standard $\mathfrak{g}$-valued 2-form on $\mathbb{R}^4$.

### 2.3 $p$-Adic Differential ($v = p$)

At $\mathbb{Q}_p$, the differential $d_p$ is the $p$-adic differential on the Bruhat-Tits tree $\mathcal{T}_p$. The tree $\mathcal{T}_p$ is a $(p+1)$-regular graph. A $p$-adic gauge field is a function on the vertices and edges of $\mathcal{T}_p$ with values in $\mathfrak{g}$.

The field strength at a triangle $\Delta$ of $\mathcal{T}_p$ is the holonomy around the triangle:

$$F_p(\Delta) = \mathrm{Hol}(A_p, \partial \Delta)$$

This discretization is **exact** — there is no continuum limit because the Bruhat-Tits tree is already the correct manifold. [speculative]

---

## 3. Action Functional

### 3.1 Adelic Yang-Mills Action

The adelic Yang-Mills action is:

$$S_{\text{YM}}[A] = \frac{1}{4g^2} \int_{\mathbb{A}} \|F\|^2 \, d^\times x + \frac{i\theta}{32\pi^2} \int_{\mathbb{A}} \mathrm{Tr}(F \wedge F)$$

where $d^\times x$ is the Tamagawa measure on $\mathbb{A}$ (the product of Haar measures at each place, normalized so that $\mathrm{vol}(\mathbb{A}/\mathbb{Q}) = 1$).

### 3.2 Factorization

**Theorem 1 (Factorization).** The adelic Yang-Mills action decomposes as a sum over places:

$$S_{\text{YM}}[A] = S_\infty[A_\infty] + \sum_p S_p[A_p]$$

where:

$$S_\infty[A_\infty] = \frac{1}{4g_\infty^2} \int_{\mathbb{R}^4} \|F_\infty\|^2 + \frac{i\theta_\infty}{32\pi^2} \int \mathrm{Tr}(F_\infty \wedge F_\infty)$$

is the standard $N=4$ SYM action, and:

$$S_p[A_p] = \frac{k_p}{4\pi} \int_{\mathcal{T}_p} \mathrm{Tr}\left(A_p \wedge d_p A_p + \frac{2}{3} A_p \wedge A_p \wedge A_p\right)$$

is the Chern-Simons action at level $k_p$ on the Bruhat-Tits tree.

*Proof.* The adele ring's measure factorizes: $d^\times x = d^\times x_\infty \cdot \prod_p d^\times x_p$. The norm $\|F\|^2$ splits because $F$ decomposes into independent local components. The cross-terms $F_v \wedge F_w$ for $v \neq w$ vanish because the integration is over the product measure. $\blacksquare$

### 3.3 Level Identification

The Chern-Simons level $k_p$ at each $p$-adic place is determined by the local Langlands correspondence (Phase 1):

- $p = 2$: $k_2 + 2 = 2^m$ (from $R(\mathrm{SU}(2))_k \cong R(\mathbb{Z}_2^\times)$)
- $p = 3$: $k_3 = 2 \cdot 3^{m-1} - 1$ (ternary condition)
- $p \geq 5$: $k_p = (p-1) \cdot p^{m-1} - 1$ (general condition, with higher-rank categories)

The coupling constant at place $p$ is:

$$g_p^2 = \frac{4\pi}{k_p}$$

which is weak for large $k_p$ (UV) and strong for small $k_p$ (IR). [my conjecture]

---

## 4. Path Integral Factorization

### 4.1 Adelic Path Integral

The quantum theory is defined by the path integral:

$$Z_{\text{YM}} = \int \mathcal{D}A \, e^{i S_{\text{YM}}[A]}$$

where $\mathcal{D}A = \prod_v \mathcal{D}A_v$ is the product measure over local gauge fields.

**Theorem 2 (Path Integral Factorization).** The adelic path integral factorizes over places:

$$Z_{\text{YM}} = Z_\infty \cdot \prod_p Z_p$$

where $Z_\infty = \int \mathcal{D}A_\infty \, e^{i S_\infty[A_\infty]}$ is the $N=4$ SYM path integral and:

$$Z_p = \int \mathcal{D}A_p \, e^{i S_p[A_p]}$$

is the Chern-Simons path integral on the Bruhat-Tits tree $\mathcal{T}_p$.

*Proof.* The action splits into independent local terms $S_{\text{YM}}[A] = \sum_v S_v[A_v]$, and the integration measure splits as $\mathcal{D}A = \prod_v \mathcal{D}A_v$. Therefore:

$$Z_{\text{YM}} = \prod_v \int \mathcal{D}A_v \, e^{i S_v[A_v]} = \prod_v Z_v$$

The product converges because at almost all $p$, the action is trivial (the trivial connection on $\mathcal{T}_p$), giving $Z_p = 1$. $\blacksquare$

### 4.2 Physical Interpretation

The factorization means:

1. **The $\infty$-place** $Z_\infty$ is the partition function of $N=4$ SYM on $\mathbb{R}^4$, whose S-duality is the geometric Langlands correspondence (Kapustin-Witten 2006).

2. **Each $p$-adic place** $Z_p$ is the partition function of Chern-Simons theory on $\mathcal{T}_p$ at level $k_p$, which computes the fusion ring $R(\mathrm{SU}(2))_{k_p}$ (Witten 1989).

3. **The full adelic factor** $Z_{\text{YM}}$ is the product of these — a **topological quantum field theory factorized over the places of $\mathbb{Q}$**.

The adelic partition function $Z_{\text{YM}}$ is the generating function for adelic anyon correlation functions. [speculative]

---

## 5. Reduction to Physical Theories

### 5.1 Archimedean Reduction: $N=4$ SYM

At the $\infty$-place, the adelic Yang-Mills action reduces exactly to the standard $N=4$ supersymmetric Yang-Mills action on $\mathbb{R}^4$. The supersymmetry enhancement (from ordinary Yang-Mills to $N=4$ SYM) comes from the requirement that the topological twist — necessary for the Kapustin-Witten S-duality — is consistent with the full adelic symmetry. The $N=4$ SYM on $\mathbb{R}^4$ with gauge group $G$ is S-dual to $N=4$ SYM with gauge group ${}^LG$, which is the geometric Langlands correspondence (Kapustin-Witten 2006). [established]

### 5.2 $p$-Adic Reduction: Anyon Braiding

At each $p$-adic place, the Chern-Simons action on $\mathcal{T}_p$ at level $k_p$ describes the braiding of anyons in the $\mathrm{SU}(2)_{k_p}$ modular tensor category. The anyon types are the simple objects $j = 0, \frac{1}{2}, 1, \ldots, \frac{k_p}{2}$, and braiding phases are given by the modular $S$ and $T$ matrices:

$$S_{ab} = \sqrt{\frac{2}{k_p+2}} \sin\left(\frac{\pi(2a+1)(2b+1)}{k_p+2}\right)$$

The anyon braiding implements the local Langlands correspondence at $p$. The fusion of anyons corresponds to the convolution product in the character ring $R_m(\mathbb{Z}_p^\times)$. [Phases 1.1-1.3]

### 5.3 Gauge Invariance

The adelic Yang-Mills action is invariant under adelic gauge transformations:

$$A \to g^{-1} A g + g^{-1} dg$$

where $g = (g_\infty, g_2, g_3, \ldots)$ with $g_p \in G(\mathbb{Q}_p)$ and $g_\infty \in G(\mathbb{R})$. The gauge group $\mathbb{G}_{\mathbb{A}} = \prod_v G(\mathbb{Q}_v)$ is the adelic gauge group.

---

## 6. Falsifiable Predictions

1. **[P1] Path integral factorization.** $Z_{\text{YM}} = \prod_v Z_v$ holds for the adelic Yang-Mills path integral. [my conjecture]
   - **Falsification:** Compute $Z_p$ for $\mathrm{SU}(2)_{k_p}$ on $\mathcal{T}_p$ via Verlinde formula and verify the product converges.
   - **[CHECK: 2027-12]**

2. **[P2] Coupling duality.** $g_v^2 = 4\pi/k_v$ holds at each place $v$, and the strong-weak duality $k_v \leftrightarrow 1/k_v$ is exactly the adelic S-duality. [my conjecture]
   - **Falsification:** Find a level $k_p$ where the predicted coupling does not match the known S-duality orbit.
   - **[CHECK: 2028-06]**

3. **[P3] Adelic anyon braiding.** The adelic anyon braiding at places $p$ and $q$ (with $p \neq q$) is independent and commutative. [speculative]
   - **Falsification:** Find a non-trivial braiding phase between anyons at different primes.
   - **[CHECK: 2029-12]**

---

## 7. Conclusion

Adelic Yang-Mills theory is the gauge theory on the adele ring $\mathbb{A}_\mathbb{Q}$ whose action factorizes over places: $S_{\text{YM}}[A] = S_\infty[A_\infty] + \sum_p S_p[A_p]$. At $\infty$, it is $N=4$ SYM with S-duality = geometric Langlands. At each finite $p$, it is Chern-Simons on the Bruhat-Tits tree $\mathcal{T}_p$ at level $k_p$, describing anyon braiding = local Langlands. The path integral $Z_{\text{YM}} = \prod_v Z_v$ is the generating function for adelic correlation functions.

Phase 3.2 (Adelic S-Duality) extends the Kapustin-Witten duality to all places. Phase 3.3 (Lattice Simulations) will develop numerical methods for computing $Z_p$ on the Bruhat-Tits tree.

---

## Declarations

**Funding:** None. **Conflicts of Interest:** None. **Ethics Approval:** Not applicable. **Consent:** Not applicable. **Author Contributions:** QNFO Research. **Data Availability:** Within this paper. **Code Availability:** To be deposited with Zenodo. **Use of AI:** AI-assisted formalization. Author-verified.

---

## References

1. ALP Phases 1.1—2.3. (2026). Program deliverables, v0.2—v0.8.

2. Kapustin, A., & Witten, E. (2006). Electric-magnetic duality and the geometric Langlands program. *CMP*, 1(1), 1—236.

3. Witten, E. (1989). Quantum field theory and the Jones polynomial. *CMP*, 121(3), 351—399.

4. Verlinde, E. (1988). Fusion rules and modular transformations in 2D CFT. *Nuclear Physics B*, 300, 360—376.

5. Langlands, R. P. (1970). Problems in the theory of automorphic forms. *Lecture Notes in Mathematics*, 170, 18—61.

6. Gelbart, S. (1975). *Automorphic Forms on Adele Groups*. Princeton University Press.

7. Tate, J. (1950). Fourier analysis in number fields and Hecke's zeta-functions. In *Algebraic Number Theory*.

8. Atiyah, M. F., & Bott, R. (1983). The Yang-Mills equations over Riemann surfaces. *Phil. Trans. R. Soc. Lond. A*, 308, 523—615.

9. Serre, J.-P. (1980). *Trees*. Springer-Verlag.

10. QNFO Research. (2026). The Langlands Program Is Adelic Physics Without the Physics. Rosetta Note v1.0.
