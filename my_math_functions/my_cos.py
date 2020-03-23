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

    n = 2
    m = 3

    A_pow2 = my_same_square_matrices_mul(A, A)
    Tmp = A_pow2
    Tmp_1 = my_matrice_div_by_float(Tmp, n)
    Result = my_same_square_matrices_sub(I, Tmp_1)
    leave_calc = False

    for i in range(0, 200) :
        Cmp = Result
        for j in range(0, 2) :
            n *= m
            m += 1
        Tmp = my_same_square_matrices_mul(Tmp, A_pow2)
        Tmp_1 = my_matrice_div_by_float(Tmp, n)
        if i % 2 == 0 :
            Result = my_same_square_matrices_add(Result, Tmp_1)
        else :
            Result = my_same_square_matrices_sub(Result, Tmp_1)
        for j in range(0, len(A)) :
            if round(Cmp[j], 2) == round(Result[j], 2) :
                leave_calc = True
            else :
                leave_calc = False
                break

        if leave_calc == True :
            break

    my_print_matrix(Result, side_len)
    return 0