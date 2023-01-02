#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    new_list = []
    for i in range(0, len(matrix)):
        new_list = matrix[i]
        for j in range(0, len(new_list)):
            print("{}".format(new_list[j]))
