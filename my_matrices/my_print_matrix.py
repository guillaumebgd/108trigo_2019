# -*- coding: Utf-8 -*
##
## EPITECH PROJECT, 2019
## 108trigo_2019
## File description:
## my_print_matrix.py
##

import sys

from math import pow

def my_print_matrix(matrix : list, side_len : int) :

    len_matrix = len(matrix)

    if pow(side_len, 2) != len_matrix :
        return (False)

    for i in range(1, len_matrix + 1) :
        if i % side_len == 0 and i > 1 :
            sys.stdout.write("%.2f\n" % matrix[i - 1])
        else :
            sys.stdout.write("%.2f\t" % matrix[i - 1])