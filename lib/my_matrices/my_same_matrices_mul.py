# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 108trigo_2019
## File description:
## Multiplies two squared same size matrices.
##

from math import sqrt

def my_same_square_matrices_mul(matrix_1: list, matrix_2: list) :

    nb_components = len(matrix_1)

    if nb_components != len(matrix_2) :
        return False

    side_matrix = sqrt(nb_components)

    if not side_matrix.is_integer() :
        return False

    side_matrix = int(side_matrix)
    result = [0] * nb_components

    row_i = 0
    column_i = 0
    save_row = 0
    save_column = 0
    x = 0

    for i in range(0, nb_components) :
        for j in range(0, side_matrix) :
            result[i] += matrix_1[row_i] * matrix_2[column_i]
            row_i += 1
            column_i += side_matrix
        save_column += 1
        if save_column == side_matrix :
            save_column = 0
        x += 1
        if x == side_matrix :
            x = 0
            save_row += side_matrix
        column_i = save_column
        row_i = save_row

    return result