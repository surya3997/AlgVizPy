from sympy import *
import math

deg = 5

coeff = [1, -3.5, 2.75, 2.125, -3.875, 1.25]

r = -1
s = -1

A = coeff[:]

precision = 4

stopper = 20


def calculate_c(r, s, B):
    n = len(A)

    if n > 3:
        C = []

        C.append(B[0])
        C.append(B[1] + r * C[0])

        for i in range(2, len(A) - 1):
            C.append(B[i] + r * C[i - 1] + s * C[i - 2])

        # print(C)
        return(C)


def calculate_b(r, s):
    n = len(A)

    if n > 3:
        B = []

        B.append(A[0])
        B.append(A[1] + r * B[0])

        for i in range(2, len(A)):
            B.append(A[i] + r * B[i - 1] + s * B[i - 2])

        print(B)
        return(B)


def calculate_dels(c_m, b_v):
    delta = c_m[0][0] * c_m[1][1] - c_m[1][0] * c_m[0][1]
    d1 = c_m[1][1] * b_v[0] - c_m[0][1] * b_v[1]
    d2 = c_m[0][0] * b_v[1] - c_m[1][0] * b_v[0]

# print(c_m)
    return(round(d1 / delta, precision), round(d2 / delta, precision))


B = calculate_b(r, s)
C = calculate_c(r, s, B)

c_matrix = [[C[len(C) - 2], C[len(C) - 3]], [C[len(C) - 1], C[len(C) - 2]]]
b_vector = [-B[len(B) - 2], -B[len(B) - 1]]

del_r, del_s = calculate_dels(c_matrix, b_vector)
r += del_r
s += del_s
cnt = 0

while del_r != 0 and del_s != 0 and cnt < stopper:
    if math.inf in B:
        break

    B = calculate_b(r, s)
    C = calculate_c(r, s, B)

    c_matrix = [[C[len(C) - 2], C[len(C) - 3]], [C[len(C) - 1], C[len(C) - 2]]]
    b_vector = [-B[len(B) - 2], -B[len(B) - 1]]

    del_r, del_s = calculate_dels(c_matrix, b_vector)
    r += del_r
    s += del_s

##    print(del_r, del_s)

    cnt += 1


print("\nr and s converges to ", r, s)
