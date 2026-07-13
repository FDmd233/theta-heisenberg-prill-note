#!/usr/bin/env python3
"""Exact certificates for the Jacobian-ring computations in the paper.

Only fractions and integer row operations are used.  No floating-point
arithmetic or external computer-algebra system is involved.
"""

from fractions import Fraction
from itertools import combinations, combinations_with_replacement


def reduce_monom(exponents):
    """Reduce a monomial modulo
    (x0*x1, x0^2+3*x1^2, x2^2, x3^2, x4^2).
    """
    e = list(exponents)
    coefficient = Fraction(1)
    if any(e[i] >= 2 for i in (2, 3, 4)):
        return {}
    if e[0] >= 1 and e[1] >= 1:
        return {}
    if e[0] >= 3 or e[1] >= 3:
        return {}
    if e[0] >= 2:
        e[0] -= 2
        e[1] += 2
        coefficient *= -3
        if e[1] >= 3:
            return {}
    return {tuple(e): coefficient}


def monomial(*indices):
    e = [0] * 5
    for i in indices:
        e[i] += 1
    reduced = reduce_monom(e)
    assert len(reduced) == 1
    return next(iter(reduced))


def multiply(a, b):
    out = {}
    for ea, ca in a.items():
        for eb, cb in b.items():
            e = tuple(x + y for x, y in zip(ea, eb))
            for er, cr in reduce_monom(e).items():
                out[er] = out.get(er, Fraction(0)) + ca * cb * cr
    return {e: c for e, c in out.items() if c}


def vector_monomial(e):
    return {e: Fraction(1)}


R1 = [monomial(i) for i in range(5)]
T = [
    monomial(2, 3, 4),
    monomial(1, 3, 4),
    monomial(1, 2, 4),
    monomial(1, 2, 3),
    monomial(1, 1, 4),
    monomial(1, 1, 3),
    monomial(1, 1, 2),
]
R4 = [
    monomial(0, 2, 3, 4),
    monomial(1, 2, 3, 4),
    monomial(1, 1, 3, 4),
    monomial(1, 1, 2, 4),
    monomial(1, 1, 2, 3),
]
SOCLE = monomial(1, 1, 2, 3, 4)


def coordinates_R4(element):
    return [element.get(m, Fraction(0)) for m in R4]


def pair_R4_R1(v4, index):
    element = {R4[i]: v4[i] for i in range(5) if v4[i]}
    product = multiply(element, vector_monomial(R1[index]))
    return product.get(SOCLE, Fraction(0))


def multiply_T_R1(f, index):
    return coordinates_R4(multiply(vector_monomial(f), vector_monomial(R1[index])))


def wedge_pair(u, v, k, ell):
    return (
        pair_R4_R1(u, k) * pair_R4_R1(v, ell)
        - pair_R4_R1(u, ell) * pair_R4_R1(v, k)
    )


def wedge_vector(a, b):
    out = {}
    for i, ai in enumerate(a):
        if not ai:
            continue
        for j, bj in enumerate(b):
            if not bj or i == j:
                continue
            if i < j:
                out[(i, j)] = out.get((i, j), Fraction(0)) + ai * bj
            else:
                out[(j, i)] = out.get((j, i), Fraction(0)) - ai * bj
    return {key: Fraction(value) for key, value in out.items() if value}


def nu_entry(t_pair, source_wedge, target_wedge):
    ia, ib = t_pair
    f, g = T[ia], T[ib]
    value = Fraction(0)
    for (i, j), source_coefficient in source_wedge.items():
        fi = multiply_T_R1(f, i)
        fj = multiply_T_R1(f, j)
        gi = multiply_T_R1(g, i)
        gj = multiply_T_R1(g, j)
        for (k, ell), target_coefficient in target_wedge.items():
            value += source_coefficient * target_coefficient * (
                wedge_pair(fi, gj, k, ell) + wedge_pair(gi, fj, k, ell)
            )
    return value


def wedge_coordinate(u, v, k, ell):
    """Coefficient of e_k wedge e_ell in u wedge v in wedge^2 R4."""
    return u[k] * v[ell] - u[ell] * v[k]


def nu_coordinate(t_pair, source_pair, target_pair):
    """A direct matrix coefficient of nu: wedge^2 R1 -> wedge^2 R4.

    Unlike ``nu_entry``, this does not identify wedge^2 R4 with its dual
    by the socle pairing.  It is the convention used for the 27-by-27
    certificate in the manuscript.
    """
    ia, ib = t_pair
    i, j = source_pair
    k, ell = target_pair
    f, g = T[ia], T[ib]
    fi = multiply_T_R1(f, i)
    fj = multiply_T_R1(f, j)
    gi = multiply_T_R1(g, i)
    gj = multiply_T_R1(g, j)
    return wedge_coordinate(fi, gj, k, ell) + wedge_coordinate(gi, fj, k, ell)


def determinant(matrix):
    a = [list(map(Fraction, row)) for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    det = Fraction(1)
    for column in range(n):
        pivot = next((row for row in range(column, n) if a[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            a[column], a[pivot] = a[pivot], a[column]
            det = -det
        z = a[column][column]
        det *= z
        for j in range(column, n):
            a[column][j] /= z
        for i in range(column + 1, n):
            z = a[i][column]
            for j in range(column, n):
                a[i][j] -= z * a[column][j]
    return det


S2T = list(combinations_with_replacement(range(7), 2))

# The saturated central space U_alpha = wedge^2 ker(alpha).
KER_ALPHA = [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, -1],
    [0, 0, 1, 0, -1],
    [0, 0, 0, 1, -1],
]
U = [wedge_vector(KER_ALPHA[i], KER_ALPHA[j]) for i, j in combinations(range(4), 2)]
S2U = list(combinations_with_replacement(range(6), 2))
CENTRAL = [[nu_entry(t, U[i], U[j]) for i, j in S2U] for t in S2T]


def central_entry(t_pair, u_pair):
    return CENTRAL[S2T.index(tuple(sorted(t_pair)))][S2U.index(tuple(sorted(u_pair)))]


# Certificate 1: the central rank-12 minor.
ROWS_12 = [
    (0, 0), (0, 1), (0, 2), (0, 4), (0, 5), (0, 6),
    (1, 1), (1, 2), (1, 4), (1, 6), (2, 2), (4, 4),
]
COLS_12 = [
    (0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2),
    (3, 3), (3, 4), (3, 5), (4, 4), (4, 5), (5, 5),
]
MINOR_12 = [[central_entry(row, column) for column in COLS_12] for row in ROWS_12]

# Certificate 2: the flattened rank-7 minor.  A row is (eta, U-pair),
# and the column xi is evaluated on the symmetric pair xi*eta.
ROWS_7 = [
    (0, (0, 0)),
    (0, (0, 1)),
    (0, (0, 2)),
    (0, (1, 1)),
    (0, (1, 2)),
    (0, (2, 2)),
    (1, (0, 1)),
]
MINOR_7 = [
    [central_entry((xi, eta), u_pair) for xi in range(7)]
    for eta, u_pair in ROWS_7
]

# Certificate 3: a rank-27 minor for nu|Sym^2(T_E).
STANDARD = [[1 if i == j else 0 for i in range(5)] for j in range(5)]
WEDGE_PAIRS = list(combinations(range(5), 2))
STANDARD_WEDGES = [wedge_vector(STANDARD[i], STANDARD[j]) for i, j in WEDGE_PAIRS]
PAIR_INDEX = {pair: index for index, pair in enumerate(WEDGE_PAIRS)}
ROWS_27 = [
    ((0, 1), (0, 1)), ((0, 1), (0, 2)), ((0, 1), (0, 3)),
    ((0, 1), (0, 4)), ((0, 2), (0, 3)), ((0, 2), (0, 4)),
    ((0, 3), (0, 4)), ((1, 2), (1, 2)), ((1, 2), (1, 3)),
    ((1, 2), (1, 4)), ((1, 2), (2, 3)), ((1, 2), (2, 4)),
    ((1, 2), (3, 4)), ((1, 3), (1, 3)), ((1, 3), (1, 4)),
    ((1, 3), (2, 3)), ((1, 3), (2, 4)), ((1, 3), (3, 4)),
    ((1, 4), (1, 4)), ((1, 4), (2, 4)), ((1, 4), (3, 4)),
    ((2, 3), (2, 3)), ((2, 3), (2, 4)), ((2, 3), (3, 4)),
    ((2, 4), (2, 4)), ((2, 4), (3, 4)), ((3, 4), (3, 4)),
]
COLS_27 = [pair for pair in S2T if pair != (3, 4)]
MINOR_27 = [
    [
        nu_coordinate(column, source, target)
        for column in COLS_27
    ]
    for source, target in ROWS_27
]

# Verify the explicit kernel vector a1*a6+a2*a5+a3*a4.
ALL_GLOBAL_ROWS = [
    (source, target) for source in WEDGE_PAIRS for target in WEDGE_PAIRS
]
kernel_values = []
for source, target in ALL_GLOBAL_ROWS:
    kernel_values.append(
        nu_coordinate((1, 6), source, target)
        + nu_coordinate((2, 5), source, target)
        + nu_coordinate((3, 4), source, target)
    )


if __name__ == "__main__":
    det12 = determinant(MINOR_12)
    det7 = determinant(MINOR_7)
    det27 = determinant(MINOR_27)
    assert det12 == -(2 ** 7) * (3 ** 6), det12
    assert det7 == -(2 ** 3) * (3 ** 7), det7
    assert det27 == -128, det27
    assert all(value == 0 for value in kernel_values)
    print(f"det(M12) = {det12}")
    print(f"det(M7)  = {det7}")
    print(f"det(M27) = {det27}")
    print("kernel relation verified exactly")
