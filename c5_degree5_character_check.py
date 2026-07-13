"""Exact/numerical checks for the C5-equivariant degree-five theorem.

Derived audit artifact; no manuscript files are modified.
"""

import cmath


p = 5
I = ((1, 0), (0, 1))
minus_I = ((4, 0), (0, 4))
A = ((1, 1), (0, 1))
B = ((3, 1), (1, 4))
C = ((1, 0), (1, 1))


def mul(X, Y):
    return tuple(
        tuple(sum(X[i][k] * Y[k][j] for k in range(2)) % p
              for j in range(2))
        for i in range(2)
    )


def power(X, n):
    answer = I
    for _ in range(n):
        answer = mul(answer, X)
    return answer


def generated_group(gens):
    group = {I}
    todo = [I]
    while todo:
        x = todo.pop()
        for g in gens:
            y = mul(g, x)
            if y not in group:
                group.add(y)
                todo.append(y)
    return group


def main():
    print("A^5, B^5, C^5 =", power(A, 5), power(B, 5), power(C, 5))
    print("ABC =", mul(mul(A, B), C))
    print("generated SL2 group order =", len(generated_group([A, B, C])))
    assert power(A, 5) == power(B, 5) == power(C, 5) == I
    assert mul(mul(A, B), C) == minus_I
    assert len(generated_group([A, B, C])) == 120

    zeta = cmath.exp(2j * cmath.pi / 5)
    traces = [4]
    for k in range(1, 5):
        value = -(2 * zeta**k / (1 - zeta**k)
                  + zeta**(2*k) / (1 - zeta**(2*k)))
        traces.append(value)
    multiplicities = []
    for j in range(5):
        multiplicity = sum(traces[k] * zeta**(-j*k) for k in range(5)) / 5
        multiplicities.append(round(multiplicity.real))
    print("Lefschetz traces =", traces)
    print("C5 character multiplicities [1,chi,...,chi^4] =", multiplicities)
    assert multiplicities == [2, 0, 0, 1, 1]

    # det H0(KW)=chi^(3+4)=chi^2; det H0(K)=chi^(1+2)=chi^3.
    d_exponent = (3 + 4) % 5
    det_hodge_exponent = (1 + 2) % 5
    xi_exponent = (-d_exponent + det_hodge_exponent) % 5
    obstruction_characters = sorted(((1 + xi_exponent) % 5,
                                      (2 + xi_exponent) % 5))
    print("D exponent, det Hodge exponent, Xi exponent =",
          d_exponent, det_hodge_exponent, xi_exponent)
    print("obstruction characters =", obstruction_characters)
    assert xi_exponent == 1
    assert 0 not in obstruction_characters


if __name__ == "__main__":
    main()
