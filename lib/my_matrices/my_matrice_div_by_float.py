# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 108trigo_2019
## File description:
## my_matrice_div_by_float.py
##

def my_matrice_div_by_float(matrix : list, diviser : float) :

    if diviser == 0 :
        return False

    Result = [0] * len(matrix)

    for i in range(0, len(matrix)) :
        Result[i] = matrix[i] / diviser

    return Result