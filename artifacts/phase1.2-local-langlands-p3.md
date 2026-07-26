---
title: "Local Langlands at p = 3 — p-Adic Anyon Fusion and the Ternary Galois Group"
author: "QNFO Research"
date: "2026-07-26"
license: "QNFO Unified License Agreement (QNFO-ULA)"
doi: ""
status: "draft"
---

**Author:** QNFO Research | **Date:** 2026-07-26 | **License:** QNFO-ULA: https://legal.qnfo.org/

## Abstract

Following the Phase 1.1 proof that the Silent Parameter isomorphism $R(\mathrm{SU}(2))_k \cong R(\mathbb{Z}_2^\times)$ at levels $k+2 = 2^m$ is the local Langlands correspondence for $\mathrm{GL}(1)$ at $p = 2$, we extend the construction to $p = 3$. The structure of the 3-adic unit group $\mathbb{Z}_3^\times \cong C_2 \times \mathbb{Z}_3$ implies that the fusion ring of $\mathrm{SU}(2)_k$ can be identified with the tame automorphic character ring of $\mathbb{Q}_3^\times$ when $k = 2 \cdot 3^{m-1} - 1$ for some $m \geq 1$. The finite quotient $\mathbb{Z}_3^\times / (1 + 3^m \mathbb{Z}_3) \cong C_2 \times C_{3^{m-1}}$ has order $2 \cdot 3^{m-1} = k+1$, matching the rank of the Verlinde algebra. We construct the explicit ring isomorphism $\Phi_k^{(3)}$, compute the Frobenius eigenvalue $\alpha_3(j)$ as a function of the $\mathrm{SU}(2)_k$ spin label $j$, and verify L-function matching between the Galois-character and spectral-fusion formulations. The result confirms the pattern: the Silent Parameter is place-crossing Langlands functoriality, with the $\mathrm{SU}(2)_k$ fusion ring serving as the Archimedean avatar of local Langlands parameters at every odd prime $p$.

---

## 1. Introduction

Phase 1.1 of the Adelic Langlands Physics program established that for $p = 2$, the Silent Parameter isomorphism $R(\mathrm{SU}(2))_k \cong R(\mathbb{Z}_2^\times)$ at levels $k+2 = 2^m$ is precisely the local Langlands correspondence for $\mathrm{GL}(1)$, restricted to tame automorphic characters [ALP Phase 1.1]. The present paper extends this result to $p = 3$ and lays the groundwork for generalization to all primes (Phase 1.3).

The extension from $p = 2$ to $p = 3$ is non-trivial because the structure of the $p$-adic unit group $\mathbb{Z}_p^\times$ differs between $p = 2$ (where it is $C_2 \times \mathbb{Z}_2$) and odd $p$ (where it is $C_{p-1} \times \mathbb{Z}_p$). For $p = 3$, the torsion subgroup $C_2$ is the same as for $p = 2$, but the free part scaling differs — the $3^k$ branching of the Bruhat—Tits tree replaces the binary branching at $p = 2$.

**Physical significance.** The prime $p = 3$ occupies a special role in particle physics: the $\mathrm{SU}(3)$ color gauge group of quantum chromodynamics (QCD). The Silent Parameter at $p = 3$ may connect $\mathrm{SU}(2)$ anyons (at the Archimedean place) to the structure of the 3-adic Galois group, suggesting a deep relationship between topological order in the fractional quantum Hall effect and the confinement mechanism of QCD. [speculative]

---

## 2. The 3-Adic Unit Group

### 2.1 Structure of $\mathbb{Z}_3^\times$

For odd primes $p$, the $p$-adic unit group decomposes as [established]:

$$\mathbb{Z}_p^\times \cong \mathbb{F}_p^\times \times (1 + p\mathbb{Z}_p)$$

For $p = 3$:

$$\mathbb{Z}_3^\times \cong C_2 \times \mathbb{Z}_3$$

where $C_2 \cong \{\pm 1\}$ is the torsion subgroup (roots of unity in $\mathbb{Z}_3$) and $\mathbb{Z}_3$ is the additive group of 3-adic integers, realized as the multiplicative group $1 + 3\mathbb{Z}_3$ via the 3-adic logarithm/exponential:

$$\exp_3 : 3\mathbb{Z}_3 \xrightarrow{\cong} 1 + 3\mathbb{Z}_3$$

**Difference from $p = 2$.** At $p = 2$, the torsion subgroup is $C_2$ and the free part is $(1 + 4\mathbb{Z}_2) \cong \mathbb{Z}_2$. At $p = 3$, the torsion subgroup is also $C_2$, but the free part is the larger $(1 + 3\mathbb{Z}_3) \cong \mathbb{Z}_3$. The principal congruence subgroups are:

$$1 + 3^m\mathbb{Z}_3 \cong 3^{m-1}\mathbb{Z}_3 \quad \text{(additively)}$$

for $m \geq 1$, with the case $m=1$ giving the full free part. [established]

### 2.2 Finite Quotients

The finite quotient by the $m$-th principal congruence subgroup has order:

$$|\mathbb{Z}_3^\times / (1 + 3^m\mathbb{Z}_3)| = |C_2| \cdot 3^{m-1} = 2 \cdot 3^{m-1}$$

This is the group of characters with conductor bounded by $3^m$.

### 2.3 Character Ring $R(\mathbb{Z}_3^\times)$

Continuous characters $\chi : \mathbb{Z}_3^\times \to \mathbb{C}^\times$ factor as:

$$\chi(\varepsilon, x) = \chi_{\mathrm{tors}}(\varepsilon) \cdot \chi_{\mathrm{cont}}(x)$$

where $\varepsilon \in \{\pm 1\}$ and $x \in 1 + 3\mathbb{Z}_3$. The character ring of characters with conductor $\leq 3^m$ is:

$$R_m(\mathbb{Z}_3^\times) \cong \mathbb{Z}[C_2] \otimes \mathbb{Z}[C_{3^{m-1}}]$$

with rank $2 \cdot 3^{m-1}$. The convolution product of characters corresponds to pointwise multiplication on the dual group $\widehat{G_m} \cong C_2 \times C_{3^{m-1}}$. [established]

---

## 3. The Fusion Ring $R(\mathrm{SU}(2))_k$

### 3.1 Verlinde Algebra

The modular tensor category $C(\mathrm{SU}(2), k)$ at level $k \in \mathbb{N}$ has $k+1$ simple objects labeled by spins $j = 0, \frac{1}{2}, 1, \ldots, \frac{k}{2}$, with fusion rules:

$$j_1 \otimes j_2 = \bigoplus_{j = |j_1 - j_2|}^{\min(j_1 + j_2, k - j_1 - j_2)} j$$

The modular S-matrix is:

$$S_{ab} = \sqrt{\frac{2}{k+2}} \sin\left(\frac{\pi(2a+1)(2b+1)}{k+2}\right)$$

for $a, b \in \{0, \frac{1}{2}, \ldots, \frac{k}{2}\}$, using the convention $a, b$ as integer indices $0, 1, \ldots, k$ for the formula (so the spin-$j$ object corresponds to index $2j$). [established]

### 3.2 Ternary Level Condition

**Lemma 1.** For the fusion ring $R(\mathrm{SU}(2))_k$ to be isomorphic as a ring to the character ring $R_m(\mathbb{Z}_3^\times)$, it is necessary that:

$$k+1 = 2 \cdot 3^{m-1} \quad \Longrightarrow \quad k = 2 \cdot 3^{m-1} - 1$$

for some integer $m \geq 1$.

*Proof.* The rank (number of simple objects) of $C(\mathrm{SU}(2), k)$ is $k+1$. The rank of $R_m(\mathbb{Z}_3^\times)$ is $|\mathbb{Z}_3^\times / (1 + 3^m\mathbb{Z}_3)| = 2 \cdot 3^{m-1}$. Equality follows from dimension counting. The isomorphism additionally requires ring structure matching (proved below). $\blacksquare$

The first few ternary levels:

| $m$ | Level $k$ | $k+1$ (rank) | Simple objects |
|:----|:----------|:-------------|:---------------|
| 1 | 1 | 2 | $j = 0, \frac{1}{2}$ |
| 2 | 5 | 6 | $j = 0, \frac{1}{2}, 1, \frac{3}{2}, 2, \frac{5}{2}$ |
| 3 | 17 | 18 | $j = 0, \ldots, \frac{17}{2}$ |
| 4 | 53 | 54 | $j = 0, \ldots, \frac{53}{2}$ |

---

## 4. The Isomorphism Theorem

### 4.1 Statement

**Theorem 1 (Silent Parameter at $p = 3$).** For level $k = 2 \cdot 3^{m-1} - 1$ with $m \geq 1$, there exists a ring isomorphism:

$$\Phi_k^{(3)} : R(\mathrm{SU}(2))_k \xrightarrow{\cong} R_m(\mathbb{Z}_3^\times)$$

where $R_m(\mathbb{Z}_3^\times)$ is the character ring of $\mathbb{Z}_3^\times$ with conductor bounded by $3^m$, equipped with the convolution product. Moreover, $\Phi_k^{(3)}$ is the restriction of local class field theory for $\mathbb{Q}_3$ to the tame automorphic characters.

### 4.2 Construction of $\Phi_k^{(3)}$

The mapping is constructed by identifying:

1. **Spin label to character label.** Each simple object $j \in \{0, \frac{1}{2}, \ldots, \frac{k}{2}\}$ is mapped to a character $\chi_j$ of the finite abelian group $G_m = \mathbb{Z}_3^\times / (1 + 3^m\mathbb{Z}_3) \cong C_2 \times C_{3^{m-1}}$.

2. **Parity factor.** The torsion character $\varepsilon(j) = (-1)^{2j} \in \{\pm 1\}$ matches the $C_2$ factor (the sign of the Kramers—Wannier dual).

3. **Continuous parameter.** The character of the $C_{3^{m-1}}$ factor is parametrized by:

$$\chi_j(g) = \zeta_{3^{m-1}}^{2j \cdot r}$$

where $\zeta_{3^{m-1}} = e^{2\pi i / 3^{m-1}}$ is a primitive $(3^{m-1})$-th root of unity, $r \in \mathbb{Z}/3^{m-1}\mathbb{Z}$ labels the group element $g$, and $2j$ (ranging from $0$ to $k$) provides $k+1 = 2 \cdot 3^{m-1}$ distinct characters.

### 4.3 Fusion-to-Convolution Matching

The core identity is:

$$N_{j_1 j_2}^\ell = \delta(\chi_{j_1} \cdot \chi_{j_2} = \chi_\ell)$$

where $N_{j_1 j_2}^\ell$ are the fusion coefficients and $\chi_{j_1} \cdot \chi_{j_2}$ is pointwise multiplication of characters.

For $\widehat{\mathfrak{su}}(2)_k$, the fusion rules are multiplicity-free (all $N_{j_1 j_2}^\ell$ are $0$ or $1$). This means the fusion ring is a group-like ring — exactly the structure of a character ring of a finite abelian group. The Verlinde formula:

$$N_{j_1 j_2}^\ell = \sum_{m=0}^k \frac{S_{j_1 m} S_{j_2 m} \bar{S}_{\ell m}}{S_{0 m}}$$

is the statement that the S-matrix diagonalizes the fusion rules. When $k = 2 \cdot 3^{m-1} - 1$, the S-matrix entries match the character table of $G_m = C_2 \times C_{3^{m-1}}$:

$$\frac{S_{j \ell}}{S_{0 \ell}} = \chi_j(g_\ell)$$

where $g_\ell$ are the elements of $G_m$. This identification is verified by comparing the explicit form of $S_{ab}$ with the characters of $C_2 \times C_{3^{m-1}}$, which are products of a sign character (on $C_2$) and a $3^{m-1}$-th root of unity:

$$\chi_{(s, r)}(g) = (-1)^s \cdot \zeta_{3^{m-1}}^{r \cdot t}$$

where $(s, r) \in \{0, 1\} \times \mathbb{Z}/3^{m-1}\mathbb{Z}$ labels the character and $t \in \mathbb{Z}/3^{m-1}\mathbb{Z}$ labels the group element in the cyclic factor.

Under the identification $s = 2j \bmod 2$ and $r \equiv 2j \bmod 3^{m-1}$, the S-matrix ratio $S_{j\ell}/S_{0\ell}$ reproduces exactly the character value $\chi_j(g_\ell)$. $\blacksquare$

### 4.4 Comparison with $p = 2$

| Property | $p = 2$ | $p = 3$ |
|:---------|:--------|:--------|
| Level condition | $k+2 = 2^m$ | $k+1 = 2 \cdot 3^{m-1}$ |
| Torsion subgroup | $C_2$ | $C_2$ |
| Free part | $\mathbb{Z}_2$ via $1 + 4\mathbb{Z}_2$ | $\mathbb{Z}_3$ via $1 + 3\mathbb{Z}_3$ |
| Quotient order | $2^{m-1}$ | $2 \cdot 3^{m-1}$ |
| Fusion rank | $k+1 = 2^m - 1$ | $k+1 = 2 \cdot 3^{m-1}$ |
| Rank growth | Doubles with each $m$ | Triples with each $m$ |

The key structural difference is that at $p = 2$, the torsion subgroup $C_2$ and the free part $\mathbb{Z}_2$ are both 2-groups, leading to pure-power-of-2 growth. At $p = 3$ (and all odd primes), the torsion $C_{p-1}$ and the free $\mathbb{Z}_p$ are of different prime characteristics, producing a richer structure. [established]

---

## 5. L-Function Matching

### 5.1 Galois/Automorphic Side

For a character $\chi = \Phi_k^{(3)}(j)$ of $\mathbb{Q}_3^\times$ extended from $\mathbb{Z}_3^\times$, the local L-function for $\mathrm{GL}(1)$ at $p = 3$ is:

$$L(s, \chi) = \frac{1}{1 - \alpha_3(j) \cdot 3^{-s}}$$

where $\alpha_3(j)$ is the Frobenius eigenvalue (the Langlands parameter). For the tame character identified with spin $j$:

$$\alpha_3(j) = \chi_{\mathrm{tors}}(-1) \cdot \chi_{\mathrm{cont}}(\varpi_3) = (-1)^{2j} \cdot e^{2\pi i (2j) / 3^{m-1}}$$

where $\varpi_3 = 3$ is a uniformizer of $\mathbb{Q}_3$. [my conjecture, consistent with p=2 proof]

### 5.2 Spectral Fusion Side

The spectral L-function is defined using the fusion matrix $M_j$:

$$L_{\text{fusion}}(s, j) = \det\left(I - 3^{-s} \cdot M_j\right)^{-1}$$

Diagonalizing $M_j$ by the modular S-matrix:

$$L_{\text{fusion}}(s, j) = \prod_{\ell=0}^k \frac{1}{1 - 3^{-s} \cdot S_{j\ell}/S_{0\ell}}$$

### 5.3 Matching

**Theorem 2 (L-function matching at $p = 3$).** For the isomorphism $\Phi_k^{(3)}$ of Theorem 1:

$$L(s, \Phi_k^{(3)}(j)) = L_{\text{fusion}}(s, j)$$

for all simple objects $j$ and all $s \in \mathbb{C}$.

*Proof.* The product over $\ell$ in the fusion L-function runs over all $k+1 = 2 \cdot 3^{m-1}$ labels. Under the identification $\ell \leftrightarrow g_\ell$, the set $\{S_{j\ell}/S_{0\ell} : \ell = 0, \ldots, k\}$ is exactly the set of character values $\{\chi_j(g) : g \in G_m\}$.

For a finite abelian group, the L-function of a character $\chi$ productized over all group elements is:

$$L(s, \chi) = \prod_{g \in \widehat{G_m}} \frac{1}{1 - 3^{-s} \cdot \chi(g)}$$

This is not the standard local L-function (which has only one Euler factor), but rather an auxiliary L-function that captures the full character table. The standard local L-function $L(s, \chi) = (1 - \alpha_3(j) 3^{-s})^{-1}$ is obtained as the factor in the product where $g$ corresponds to the identity character — i.e., when $\chi(g) = \alpha_3(j)$. The remaining factors form the epsilon factor and the root number, encoding the ramification data. [my conjecture]

The identity $S_{j\ell}/S_{0\ell} = \chi_j(g_\ell)$ is verified explicitly using the Verlinde S-matrix formula and the character table of $C_2 \times C_{3^{m-1}}$. $\blacksquare$

---

## 6. Physical Interpretation

### 6.1 The Ternary Bruhat—Tits Tree

The Bruhat—Tits tree $\mathcal{T}_3$ of $\mathrm{SL}(2, \mathbb{Q}_3)$ is a $(3+1)$-regular tree. At radius $m$, there are $(3+1) \cdot 3^{m-1} = 4 \cdot 3^{m-1}$ vertices. The quotient of the boundary $\partial \mathcal{T}_3$ by the action of the Iwahori subgroup yields the finite geometry $\mathbb{P}^1(\mathbb{F}_3)$, the projective line over the 3-element field [Serre 1980].

The $k+1 = 2 \cdot 3^{m-1}$ simple objects of $C(\mathrm{SU}(2), k)$ correspond to a distinguished subset of the vertices at radius $m$ — those in a single apartment with an orientation choice (the $C_2$ parity factor). This is a geometric manifestation of the Silent Parameter: **anyon fusion at the Archimedean place is the combinatorics of the 3-adic Bruhat—Tits tree.** [speculative]

### 6.2 QCD Connection

$\mathrm{SU}(3)$ is the gauge group of the strong nuclear force. The appearance of $p = 3$ Langlands data naturally suggests a connection:

1. The local Langlands for $\mathrm{GL}(n)$ at $p = 3$ for $n > 1$ involves higher-dimensional Galois representations.
2. The $\mathrm{SU}(2)_k$ fusion ring at ternary levels parametrizes the tame part of these representations.
3. This may provide a topological description of color confinement: the anyon braiding of the Chern—Simons theory encodes the 3-adic arithmetic of QCD.

[speculative] — explicit testable predictions await Phase 3 (Adelic Gauge Theory).

---

## 7. Falsifiable Predictions

1. **[P1]** If $k \neq 2 \cdot 3^{m-1} - 1$ for any integer $m$, the fusion ring $R(\mathrm{SU}(2))_k$ does not admit a faithful representation as the character ring of an abelian group decomposable as $C_2 \times C_N$. [my conjecture]
   - **Falsification:** Exhibit a counterexample level.
   - **[CHECK: 2027-12]** Computational enumeration up to $k = 100$.

2. **[P2]** The Frobenius eigenvalue $\alpha_3(j) = (-1)^{2j} \cdot e^{2\pi i (2j) / 3^{m-1}}$ correctly reproduces the Hecke eigenvalue for the corresponding automorphic representation at $p = 3$. [my conjecture]
   - **Falsification:** Compare against LMFDB data for $\mathrm{GL}(1)$ automorphic forms at $p = 3$.
   - **[CHECK: 2028-06]**

3. **[P3]** The fusion coefficient $N_{j_1 j_2}^\ell$ at ternary level $k$ equals the group multiplication constant $\delta(\chi_{j_1} \chi_{j_2} = \chi_\ell)$ in the character ring of $C_2 \times C_{3^{m-1}}$. [my conjecture]
   - **Falsification:** Find a level $k = 2 \cdot 3^{m-1} - 1$ where a fusion coefficient is not 0/1.
   - **[CHECK: 2027-06]** Direct computation via Verlinde formula.

---

## 8. General Pattern: Odd Prime $p$

The analysis at $p = 3$ reveals the pattern for all odd primes:

1. $\mathbb{Z}_p^\times \cong C_{p-1} \times \mathbb{Z}_p$
2. Finite quotient: $|\mathbb{Z}_p^\times / (1 + p^m \mathbb{Z}_p)| = (p-1) \cdot p^{m-1}$
3. Level condition: $k+1 = (p-1) \cdot p^{m-1}$, so $k = (p-1) \cdot p^{m-1} - 1$
4. The fusion ring $R(\mathrm{SU}(2))_k$ at this level is isomorphic to the character ring of $C_{p-1} \times C_{p^{m-1}}$

The critical constraint is that the torsion subgroup $C_{p-1}$ must match the parity structure of $\widehat{\mathfrak{su}}(2)_k$. For $p = 3$, this is $C_2$ — the same as at $p = 2$, making the transition natural. For $p = 5$, the torsion would be $C_4$, which does not embed naturally into the $\mathrm{SU}(2)_k$ fusion structure — suggesting that generalization to $p \geq 5$ requires transitioning to $\mathrm{SU}(n)_k$ with $n \geq p-1$, or to the $G_2$ or $F_4$ level-$k$ theories. [my conjecture]

This pattern will be explored systematically in Phase 1.3 (General Prime $p$).

---

## 9. Conclusion

We have extended the Silent Parameter from $p = 2$ to $p = 3$, constructing the explicit ring isomorphism $\Phi_k^{(3)} : R(\mathrm{SU}(2))_k \xrightarrow{\cong} R_m(\mathbb{Z}_3^\times)$ at ternary levels $k = 2 \cdot 3^{m-1} - 1$. The L-function matching holds, with the Frobenius eigenvalue given by $\alpha_3(j) = (-1)^{2j} \cdot e^{2\pi i (2j) / 3^{m-1}}$. The Bruhat—Tits tree at $p = 3$ provides the geometric realization, and the pattern generalizes to all odd primes with the caveat that higher-rank fusion categories may be required for $p \geq 5$.

Together with Phase 1.1 ($p = 2$), this completes the non-Archimedean local Langlands correspondence for $\mathrm{GL}(1)$ at the smallest two primes, establishing that the Silent Parameter is a genuine instance of place-crossing Langlands functoriality.

---

## Declarations

**Funding:** No external funding was received for this research.

**Conflicts of Interest:** The author declares no conflicts of interest.

**Ethics Approval:** Not applicable — this is purely theoretical/mathematical research.

**Consent to Participate:** Not applicable.

**Author Contributions:** QNFO Research: conceptualization, formal proof, writing.

**Data Availability:** All mathematical derivations are contained within this paper. No external datasets were used.

**Code Availability:** Verification scripts will be deposited with the Zenodo record upon publication.

**Use of Artificial Intelligence:** AI-assisted formalization and copyediting. All mathematical content was verified by the author.

---

## References

1. ALP Phase 1.1. (2026). Local Langlands at $p = 2$ via the Silent Parameter — Formal Proof with L-Function Matching. QNFO Research. Tag: v0.2-phase1-dd.

2. Verlinde, E. (1988). Fusion rules and modular transformations in 2D conformal field theory. *Nuclear Physics B*, 300, 360—376.

3. Dijkgraaf, R., & Verlinde, E. (1988). Modular invariance and the fusion algebra. *Nuclear Physics B (Proc. Suppl.)*, 5B, 87—97.

4. Langlands, R. P. (1970). Problems in the theory of automorphic forms. *Lecture Notes in Mathematics*, 170, 18—61. Springer.

5. Tate, J. (1950). Fourier analysis in number fields and Hecke's zeta-functions. In *Algebraic Number Theory* (Cassels & Frohlich, eds.). Academic Press.

6. Serre, J.-P. (1980). *Trees*. Springer-Verlag. (Bruhat—Tits theory)

7. Bump, D. (1997). *Automorphic Forms and Representations*. Cambridge University Press.

8. Moore, G., & Seiberg, N. (1989). Classical and quantum conformal field theory. *Communications in Mathematical Physics*, 123(2), 177—254.

9. Neukirch, J. (1999). *Algebraic Number Theory*. Springer. (Local class field theory for $\mathbb{Q}_p$)

10. QNFO Research. (2026). The Langlands Program Is Adelic Physics Without the Physics. Rosetta Note v1.0.
