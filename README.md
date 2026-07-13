# Twisted Eckardt Periods and Prym Fixed-Part Obstruction

This repository contains a display preprint and its exact Jacobian-ring certificates.

The project connects the `littproblem13-f4` situation with `littproblem14`: the first part studies the twisted period variation of the rank-26 $F_4$ summand, while the second constructs uniform Raynaud--Prill representations and separates failure of generic global generation from the stronger finite-orbit condition.

Subject to complete verification of the cited geometric and Fourier--Mukai inputs, the uniform representation in the paper gives a counterexample to Litt's generic-global-generation (GGG) conjecture. It does **not** claim a new counterexample to the Putman--Wieland conjecture.

GPT-5.6 sol was used for exploratory computation, proof checking, and language editing. The exact determinant certificates can be reproduced with:

```text
python verify_exact_minors.py
```

Files:

- `Twisted_Eckardt_Periods_and_Prym_Fixed_Part_Obstruction.pdf`
- `Twisted_Eckardt_Periods_and_Prym_Fixed_Part_Obstruction.tex`
- `verify_exact_minors.py`
