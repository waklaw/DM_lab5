from prettytable import PrettyTable
import itertools
import numpy as np


def graph_order(matrix):
    if len(matrix) != len(matrix[0]):
        return -1
    else:
        return len(matrix)


def matrix_degrees(matrix):
    degrees = []
    for i in range(len(matrix)):
        degrees.append(sum(matrix[i]))
    degrees.sort(reverse=True)
    return degrees


def permutations(matrix):
    if graph_order(matrix) > 8:
        return -1
    all_matrix = []
    idx = list(range(len(matrix)))
    possible_combinations = [list(i) for i in itertools.permutations(idx, len(idx))]
    for i in possible_combinations:
        a = matrix
        a = a[i]
        a = np.transpose(np.transpose(a)[i])
        all_matrix.append({"perm_vertex": i, "adj_matrix": a})

    return all_matrix


def graph_isomporphism(first_matrix, second_matrix):
    first_matrix_degrees = matrix_degrees(first_matrix)
    second_matrix_degrees = matrix_degrees(second_matrix)
    if graph_order(first_matrix) != graph_order(first_matrix):
        return False
    elif not np.array_equal(first_matrix_degrees, second_matrix_degrees):
        return False
    else:
        for i in list(map(lambda matrix: matrix["adj_matrix"], permutations(second_matrix))):
            if np.array_equal(first_matrix, i):
                return True
    return False


if __name__ == '__main__':
    first_matrix = np.array([[0, 0, 0, 1],
                             [0, 0, 0, 1],
                             [0, 0, 0, 1],
                             [1, 1, 1, 0]])
    second_matrix = first_matrix

    print('Matrix G and H:')
    table = PrettyTable([chr(i) for i in range(65, 65 + len(first_matrix))])
    for i in first_matrix:
        table.add_row(i)
    print(table)

    print('Graph Isomorphism -', graph_isomporphism(first_matrix, second_matrix))

    first_matrix = np.array([[0, 1, 1, 1],
                             [1, 0, 1, 1],
                             [1, 1, 0, 1],
                             [1, 1, 1, 0]])
    second_matrix = np.array([[0, 1, 0, 1],
                              [1, 0, 1, 0],
                              [0, 1, 0, 1],
                              [1, 0, 1, 0]])

    print('Matrix G:')
    table = PrettyTable([chr(i) for i in range(65, 65 + len(first_matrix))])
    for i in first_matrix:
        table.add_row(i)
    print(table)

    print('Matrix H:')
    table = PrettyTable([chr(i) for i in range(65, 65 + len(second_matrix))])
    for i in second_matrix:
        table.add_row(i)
    print(table)

    print('Graph Isomorphism -', graph_isomporphism(first_matrix, second_matrix))
