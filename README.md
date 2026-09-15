# Theta--Heisenberg Untwisting and the Genus-Two Prill Minimum

This repository contains the note
*Theta--Heisenberg Untwisting, Uniform Prill Covers, and Abelian Brill--Noether Blocks*.

Its genus-two result constructs a connected degree-five etale cover over
\(y^2=x^5-1\) for which every fibre moves in a pencil. Together with the
general lower bound, this proves that the minimum degree, taken over all
genus-two curves and connected Prill-exceptional covers, is five. This is
the absolute minimum, not a uniform one. The degree-five locus in
\(\mathcal M_2\) is nonempty and proper, with every irreducible component
of dimension one or two. Consequently a general genus-two curve has no
degree-five example, and the minimum degree valid on every genus-two curve
satisfies

\[
6\le d_{\mathrm{unif}}(2)\le 8.
\]

Degrees six and seven are not excluded in the current note. However, the
present structure suggests that the uniform minimum may be sharpened to
\(d_{\mathrm{unif}}(2)=8\).

AI-assisted tools were used during development, checking, and preparation of the note.

## Files

- `theta_heisenberg_prill_note.pdf` -- compiled note.
- `theta_heisenberg_prill_note.tex` -- LaTeX source.
- `c5_degree5_certificate.g` -- exact GAP certificate for the surface
  monodromy and nonzero spin obstruction.
- `c5_degree5_character_check.py` -- independent matrix and equivariant
  character check.
- `a5_genus2_mcg_boundary_certificate.g` -- exact GAP certificate for the
  nonzero-Schur mapping-class orbit and compact-type boundary normal form.
- `FIRST_PUBLICATION_RECORD.md` -- timestamped publication and integrity
  record for the artifact commit.

## Reproduction

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error theta_heisenberg_prill_note.tex
gap -q c5_degree5_certificate.g
python c5_degree5_character_check.py
gap -q a5_genus2_mcg_boundary_certificate.g
```

The degree-five result only asserts that the generalized theta divisor
contains the Abel curve, which is exactly what the Prill condition requires.
It does not assert vanishing over all of `Pic^1(C)` and does not by itself
produce a Putman--Wieland counterexample.
