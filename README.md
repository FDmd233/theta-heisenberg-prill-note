# Theta--Heisenberg Untwisting and the Genus-Two Prill Minimum

This repository contains the note *Theta--Heisenberg Untwisting, Uniform Prill Covers, and Abelian Brill--Noether Blocks*.

Its genus-two construction gives a connected degree-five étale cover of

$$
C:\quad y^2=x^5-1
$$

for which every fibre moves in a pencil. Together with the general lower bound, this shows that the minimum degree, taken over all genus-two curves and connected Prill-exceptional covers, is five.

This is an absolute minimum, not a uniform one. The degree-five locus in $\mathcal M_2$ is nonempty and proper, and every irreducible component has dimension one or two. Hence a general genus-two curve has no degree-five example. The minimum degree valid for every genus-two curve therefore satisfies

$$
6\le d_{\mathrm{unif}}(2)\le 8.
$$

Degrees six and seven remain open in the current note.

## Files

- `theta_heisenberg_prill_note.pdf` -- compiled note.
- `theta_heisenberg_prill_note.tex` -- LaTeX source.
- `c5_degree5_certificate.g` -- exact GAP certificate for the surface monodromy and nonzero spin obstruction.
- `c5_degree5_character_check.py` -- independent matrix and equivariant-character check.
- `a5_genus2_mcg_boundary_certificate.g` -- exact GAP certificate for the nonzero-Schur mapping-class orbit and compact-type boundary normal form.
- `FIRST_PUBLICATION_RECORD.md` -- timestamped publication and integrity record for the artifact commit.

## Reproduction

~~~text
latexmk -pdf -interaction=nonstopmode -halt-on-error theta_heisenberg_prill_note.tex
gap -q c5_degree5_certificate.g
python c5_degree5_character_check.py
gap -q a5_genus2_mcg_boundary_certificate.g
~~~

## Scope

The degree-five result states that the generalized theta divisor contains the Abel curve, exactly as required by the Prill condition. It does **not** assert vanishing over all of $\operatorname{Pic}^1(C)$, and it does not by itself produce a Putman--Wieland counterexample.

## AI assistance

OpenAI GPT-5.6 Sol was used during parts of the development, checking, and preparation of this note. The mathematical statements and finite certificates can be checked independently from the accompanying source files.
