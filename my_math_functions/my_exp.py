# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 108trigo_2019
## File description:
## my_exp.py
##

from math import sqrt

from my_matrices.my_same_matrices_mul import my_same_square_matrices_mul
from my_matrices.my_get_identity_matrix import my_get_identity_matrix
from my_matrices.my_same_matrices_add import my_same_square_matrices_add
from my_matrices.my_matrice_div_by_float import my_matrice_div_by_float

from my_matrices.my_print_matrix import my_print_matrix

def my_exp(A : list) :

    I = my_get_identity_matrix(A)

    Result = my_same_square_matrices_add(I, A)
    Tmp = A
    n = 2
    m = 3
    leave_calc = False

    for i in range(0, 200) :
        Tmp = my_same_square_matrices_mul(Tmp, A)
        Tmp_1 = my_matrice_div_by_float(Tmp, n)
        Result = my_same_square_matrices_add(Result, Tmp_1)

        if i > 0 :
            for j in range(0, len(A)) :
                if round(Cmp[j], 2) == round(Result[j], 2) :
                    leave_calc = True
                else :
                    leave_calc = False
                    break

        if leave_calc == True :
            break

        Cmp = Result
        n *= m
        m += 1

    my_print_matrix(Result, sqrt(len(A)))
    return 0