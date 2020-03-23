# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 108trigo_2019
## File description:
## my_cos.py
##

from math import sqrt

from my_matrices.my_same_matrices_mul import my_same_square_matrices_mul
from my_matrices.my_same_matrices_add import my_same_square_matrices_add
from my_matrices.my_same_matrices_sub import my_same_square_matrices_sub

from my_matrices.my_matrice_div_by_float import my_matrice_div_by_float

from my_matrices.my_get_identity_matrix import my_get_identity_matrix

from my_matrices.my_print_matrix import my_print_matrix

def my_cos(A : list) :

    len_A = len(A)
    side_len = sqrt(len_A)

    I = my_get_identity_matrix(A)

    if I is False :
        return 84

    Result = I

    A_pow_2 = my_same_square_matrices_mul(A, A)
    A = A_pow_2
    n = 2
    m = 2

    for i in range(0, 10) :
        n_serie = my_matrice_div_by_float(A, n)
        if i % 2 == 0 :
            Result = my_same_square_matrices_sub(Result, n_serie)
        else :
            Result = my_same_square_matrices_add(Result, n_serie)
        A = my_same_square_matrices_mul(A, A_pow_2)
        m += 1
        n *= m

    my_print_matrix(Result, side_len)
    return 0