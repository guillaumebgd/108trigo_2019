# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 108trigo_2019
## File description:
## Adds two squared same size matrices.
##

from math import sqrt

def my_same_square_matrices_add(matrix_1: list, matrix_2: list) :

    nb_components = len(matrix_1)

    if nb_components != len(matrix_2) :
        return False

    side_matrix = sqrt(nb_components)

    if not side_matrix.is_integer() :
        return False

    result = [0] * nb_components

    for i in range(0, nb_components) :
        result[i] = matrix_1[i] + matrix_2[i]

    return result