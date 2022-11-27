import numpy as np
from itertools import permutations

# create the filling table
def create_table(string):
    table = []
    for i in range(len(string)):
        table.append([])
        for j in range(len(string)):
            if i < j:
                table[i].append('=')
            else:
                table[i].append(set())

    return np.array(table)

# filling the last row in table
def filling_bottom(cnf, table, string):
    for i, char in enumerate(string):
        cell = set()
        for row in cnf:
            if char in row[1]:
                cell.add(row[0])
        table[i][i] = cell

def filling_all(cnf, table):
    if table[len(table) - 1][0] != set():
        # print(table[len(table) - 1][0])
        return

    for i in range(1, len(table)):
        for j in range(len(table) - 2, -1, -1):
            if table[i][j] == set():
                
                list_of_intersect = []
                for k in range(i + 1):
                    if table[k][i] != '=': list_of_intersect.append(table[k][i])
                for k in range(j + 1):
                    if table[j][k] != '=': list_of_intersect.append(table[j][k])
                
                # print(list_of_intersect)
                result_list = make_permutation(list_of_intersect)
                # print(result_list)
                combine_result = combine(result_list)
                # print(combine_result)

                table[i][j] = find_cnf(combine_result, cnf)
                print('\n', table)

                break
        else:
            continue
        break

    filling_all(cnf, table)

def make_permutation(list_input):
    count = (len(list_input) // 2)

    combination = []
    for i in range(count):
        list1 = list_input[i]
        list2 = list_input[i + count]

        combination.append([])

        permut = permutations(list1, len(list2))

        for comb in permut:
            zipped = zip(comb, list2)
            combination[i].append(list(zipped))
    
    return combination

def combine(list_of_set):
    result_set = set()

    for x in list_of_set:
        for y in x:
            result_set.add(''.join(*y))

    return result_set

def find_cnf(combine, cnf):
    cnf_return = set()
    
    for com in combine:
        for row in cnf:
            if com in row[1]:
                cnf_return.add(row[0])
                break
    
    if cnf_return == set():
        return 'Ø'
    else:
        return cnf_return
