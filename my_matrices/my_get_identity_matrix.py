# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 108trigo_2019
## File description:
## my_get_identity_matrix.py
##

from math import sqrt

def my_get_identity_matrix(matrix : list) :

    nb_components = len(matrix)
    side_matrix = sqrt(nb_components)

    if not side_matrix.is_integer() :
        return False

    side_matrix = int(side_matrix)
    result = [0] * nb_components
    cursor = 0

    for i in range(0, side_matrix) :
        result[cursor] = 1
        cursor += 1
        cursor += side_matrix

    return result