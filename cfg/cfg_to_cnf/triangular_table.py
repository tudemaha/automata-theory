import numpy as np
from itertools import permutations

empty = '\u2205'

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

def filling_all(cnf, table, row = 1):
    if table[len(table) - 1][0] != set():
        # print(table[len(table) - 1][0])
        return
    
    # print(row)
    next_row = iteration(cnf, table, row)

    # print('huhu')
    filling_all(cnf, table, next_row)


def iteration(cnf, table, row):
    i = row
    #  for i in range(1, len(table)):
    for j in range(len(table) - 1, -1, -1):
        if table[i][j] == set():
            # print('koordinat:',i, j)
            
            list_of_intersect = []
            for k in range(0, i):
                # print('k', k, j)
                if table[k][j] == empty: list_of_intersect.append(set())
                elif table[k][j] != '=' and table[k][j] != set(): list_of_intersect.append(table[k][j])

            for k in range(j + 1, len(table)):
                # print('b', i, k)
                # print(table[i][k])
                if table[i][k] == empty: list_of_intersect.append(set())
                elif table[i][k] != '=' and table[i][k] != set(): list_of_intersect.append(table[i][k])
            
            # print('perpotongan:', list_of_intersect)
            result_list = make_permutation(list_of_intersect)
            # print('hasil permutasi:',result_list)
            combine_result = combine(result_list)
            # print('kombinasi: ',combine_result)

            table[i][j] = find_cnf(combine_result, cnf)
            print(table, '\n')

            i = (i + 1) if i + 1 < len(table) else 1
            return i
        
    i = (i + 1) if i + 1 < len(table) else 1
    return i

    
def make_permutation(list_input):
    count = (len(list_input) // 2)

    combination = []
    for i in range(count):
        list1 = list_input[i]
        list2 = list_input[i + count]

        combination.append([])

        for element1 in list1:
            for element2 in list2:
                combination[i].append(f'{element1}{element2}')

    return combination

def combine(list_of_set):
    result_set = set()

    for x in list_of_set:
        for y in x:
            result_set.add(y)

    return result_set

def find_cnf(combine, cnf):
    cnf_return = set()
    
    for com in combine:
        for row in cnf:
            if com in row[1]:
                cnf_return.add(row[0])
    
    if cnf_return == set():
        return empty
    else:
        return cnf_return
