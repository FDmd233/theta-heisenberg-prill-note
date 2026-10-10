# Independent sign audit of the genus-two degree-five construction

**Scope.** This note checks the character and determinant-line
bookkeeping in Section 6 of
\`theta_heisenberg_prill_note.tex\`, especially equations
(6.23)--(6.37). The finite group certificates and character
arithmetic are independent of the following geometric argument.
It does not purport to prove every global family theorem in the paper.

## Geometry of the automorphism

Let \(C:y^2=x^5-1\), let
\(\sigma(x,y)=(\zeta x,y)\), where \(\zeta^5=1\) is
primitive, and write \(\chi(\sigma)=\zeta\).
The fixed points are \((0,\pm i)\) and infinity. Local
parameters give tangent multipliers \(\zeta,\zeta,\zeta^2\).
The canonical differentials \(dx/y,x\,dx/y\) have
characters \(\chi,\chi^2\), respectively, so
\[
V_C=H^0(C,K_C)=\chi\oplus\chi^2,\qquad
\det V_C=\chi^3.
\]

The natural \(A_5\) augmentation representation \(W_\rho\)
has trace \(-1\) on each nontrivial five-cycle. The
projected inertia at all three fixed points is a nontrivial
five-cycle, so the trace on the corresponding \(W_\rho\)
fibre is \(-1\) in each case.

## Holomorphic Lefschetz character

Because \(H^0(C,W_\rho)=0\), Serre duality implies
\(H^1(C,K_C\otimes W_\rho)=0\). With the **pullback**
linearization on sections, the holomorphic Lefschetz formula
uses the denominator \(1-\lambda\) for a tangent
multiplier \(\lambda\); this is consistent, for example,
with the exact index \(-1\) for \(K_{\mathbb P^1}\).

For every \(1\le k\le4\), the trace is
\[
\operatorname{Tr}\bigl(\sigma^k\mid
 H^0(C,K_C\otimes W_\rho)\bigr)
=-\left(\frac{2\zeta^k}{1-\zeta^k}
       +\frac{\zeta^{2k}}{1-\zeta^{2k}}\right)
=1-\zeta^k-\zeta^{2k}.
\]
Its dimension at the identity is \(4\). The unique
\(C_5\)-character with these values is
\[
H^0(C,K_C\otimes W_\rho)
 =2\cdot\mathbf1\oplus\chi^3\oplus\chi^4.
\]
Its determinant character is therefore
\(\chi^{3+4}=\chi^2\).

## Determinant-of-cohomology and Wronskian signs

The complex \(R\Gamma(C,W_\rho)\) has no \(H^0\).
If \(D_\rho=\det R\Gamma(C,W_\rho)\), then
\[
D_\rho=(\det H^1(C,W_\rho))^{-1}.
\]
The augmentation bundle is self-dual and Serre duality gives
\(H^1(C,W_\rho)^\vee\simeq
H^0(C,K_C\otimes W_\rho)\).
Consequently **\(D_\rho=\chi^2\)**, not \(\chi^{-2}\).

For a point \(p\in C\), the exact sequence
\(0\to W_\rho\to W_\rho(p)\to W_{\rho,p}\otimes T_pC\to0\)
shows that the *inverse* determinant-of-cohomology
theta line restricts along \(p\mapsto\mathcal O_C(p)\)
to
\[
a^*\lambda_\rho =
 D_\rho^{-1}\otimes\Delta_\rho^{-1}\otimes K_C^4.
\]
The canonical genus-two Wronskian belongs to
\(H^0(C,K_C^3)\otimes(\det V_C)^{-1}\)
and cuts out the six Weierstrass points. Dividing the
theta section restricted to the Abel curve by this
Wronskian yields an obstruction in
\[
V_C\otimes\Xi_\rho,\qquad
\Xi_\rho=D_\rho^{-1}\otimes
   \Delta_\rho^{-1}\otimes\det V_C.
\]
The oriented real augmentation representation has
\(\Delta_\rho=\mathbf1\). The characters are therefore
\[
\Xi_\rho=\chi^{-2}\chi^3=\chi,\qquad
V_C\otimes\Xi_\rho=\chi^2\oplus\chi^3.
\]
This representation has **no trivial character**.
Provided the theta section and its Wronskian division
carry the stated equivariant linearizations, their
obstruction section is forced to vanish and the
degree-five cover is Prill-exceptional.

## What this audit does and does not certify

It independently confirms all delicate sign and dualization
choices in the *specific* \(C:y^2=x^5-1\) character
calculation, under the standard holomorphic Lefschetz and
determinant-of-cohomology conventions.

It does **not** independently establish the full
globalization of the determinant-of-cohomology section
over the connected 576-sheet Hurwitz component, the
mapping-class orbit classification, or the general
Heisenberg--Raynaud uniformization theorem.
Those are separate external and geometric proof obligations.
