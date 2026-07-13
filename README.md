# Theta--Heisenberg Untwisting and the Genus-Two Prill Minimum

This repository contains the note
*Theta--Heisenberg Untwisting, Uniform Prill Covers, and Abelian Brill--Noether Blocks*.

Its genus-two result constructs a connected degree-five etale cover over
\(y^2=x^5-1\) for which every fibre moves in a pencil. Together with the
general lower bound, this proves that the minimum degree, taken over all
genus-two curves and connected Prill-exceptional covers, is five.

FDmd233 guided GPT-5.6 sol in developing, checking, and preparing this note.

## Files

- `theta_heisenberg_prill_note.pdf` -- compiled note.
- `theta_heisenberg_prill_note.tex` -- LaTeX source.
- `c5_degree5_certificate.g` -- exact GAP certificate for the surface
  monodromy and nonzero spin obstruction.
- `c5_degree5_character_check.py` -- independent matrix and equivariant
  character check.
- `FIRST_PUBLICATION_RECORD.md` -- timestamped publication and integrity
  record for the artifact commit.

## Reproduction

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error theta_heisenberg_prill_note.tex
gap -q c5_degree5_certificate.g
python c5_degree5_character_check.py
```

The degree-five result only asserts that the generalized theta divisor
contains the Abel curve, which is exactly what the Prill condition requires.
It does not assert vanishing over all of `Pic^1(C)` and does not by itself
produce a Putman--Wieland counterexample.
