# imprort all required libraries
import numpy as np
from pandas import DataFrame

# empty set symbol from unicode
empty = '\u2205'

# create the blank filling table
def create_table(string):
    # empty list of table
    table = []
    # create iteration as length of string
    for i in range(len(string)):
        # append empty list to table that act as row
        table.append([])
        # create iteration as length of string (for column of every row)
        for j in range(len(string)):
            # if i < j, add = to column that indicates the cell cannot be filled
            if i < j:
                table[i].append('=')
            # else, add empty set in column to filled with the right value
            else:
                table[i].append(set())

    # return the empty table
    return np.array(table)

# fill the first values into the table
def filling_bottom(cnf, table, string):
    # iterate every char in input string
    for i, char in enumerate(string):
        # create empty set to store the value
        cell = set()
        # iterate every rule in cnf
        for row in cnf:
            # if the char in the cnf's body
            if char in row[1]:
                # add the body into the cell
                cell.add(row[0])

        # fill the cell(i, i) using the value in 'cell' set
        table[i][i] = cell

# fill the table with the right value
def filling_all(cnf, table, row = 1):
    # if the cell (n, 0) in tabel is not an empty set
    if table[len(table) - 1][0] != set():
        # if the cell not contain start symbol, print accepted status
        if 'T*' in table[len(table) - 1][0]: print('\nStatus: STRING ACCEPTED')
        # else, print unaccepted status
        else: print('\nStatus STRING NOT ACCEPTED')

        # return the function (stop recursion)
        return
    
    # call iteration function to fill the cell in table
    # and store the next row to be filled
    next_row = iteration(cnf, table, row)

    # call the filling table (create iteration) to fill the next cell
    filling_all(cnf, table, next_row)


# iteration to fill the cell in table
def iteration(cnf, table, row):
    # the current row to be filled
    i = row
    # iteration from the last column to first column
    for j in range(len(table) - 1, -1, -1):
        # if the tabel in cell (i, j) not empty set
        if table[i][j] == set():
            # print('coordinate:', i, j)
            
            # empty list to story all the values from cell's column and cell's row
            list_of_intersect = []
            # list all values in cell's column, from row 0 to i
            for k in range(0, i):
                # print('kolom', k, j)
                # if the value of column is empty symbol, append empty set to list_of_intersect
                if table[k][j] == empty: list_of_intersect.append(set())
                # else if the value of column not '=' and not empty set, append the value into list_of_intersect
                elif table[k][j] != '=' and table[k][j] != set(): list_of_intersect.append(table[k][j])

            # list all values in cell's row, from current row + 1 till end
            for k in range(j + 1, len(table)):
                # print('baris', i, k)
                # if the value of row is empty symbol, append empty set to list_of_intersect
                if table[i][k] == empty: list_of_intersect.append(set())
                # else if the value of row not '=' and not empty set, append the value into list_of_intersect
                elif table[i][k] != '=' and table[i][k] != set(): list_of_intersect.append(table[i][k])
            
            # print('perpotongan:', list_of_intersect)
            
            # make multiply for all the value in list_of_intersect and store the result
            result_list = make_combination(list_of_intersect)
            # print('hasil perkalian:', result_list)

            # combine (union) all the result and store the result
            combine_result = combine(result_list)
            # print('kombinasi:', combine_result)

            # find the cnf rule from the set in result before and fill the right cell in table
            table[i][j] = find_cnf(combine_result, cnf)
            
            # print the filled table in data frame form
            print(DataFrame(table), '\n')

            # if the row less than length of table, return i += 1, else return 1 (back to row 1)
            i = (i + 1) if i + 1 < len(table) else 1
            return i
    
    # if the row less than length of table, return i += 1, else return 1 (back to row 1)
    i = (i + 1) if i + 1 < len(table) else 1
    return i


# make the multiply of the values in intersect cell
def make_combination(list_input):
    # len of element in list_input divided by 2
    count = (len(list_input) // 2)

    # make empty list to store the combination
    combination = []
    # make an iteration from range of count
    for i in range(count):
        # list1 is the list input index i
        list1 = list_input[i]
        # list2 is the list input index i + count
        list2 = list_input[i + count]

        # append the empty list to the combination list
        combination.append([])

        # iterate all element in list1
        for element1 in list1:
            # iterate all element in list2
            for element2 in list2:
                # make combination from element from list1 and element of list2
                combination[i].append(f'{element1}{element2}')

    # return the combination result
    return combination

# union the combination
def combine(list_of_set):
    # create empty set to store the result
    result_set = set()

    # iterate every list of combination in list_of_set
    for x in list_of_set:
        # iterate every combination in list
        for y in x:
            # add the combination into result_set (union automatically)
            result_set.add(y)

    # return the resust of union
    return result_set

# find the cnf head from the union
def find_cnf(combine, cnf):
    # create empty set to store the result
    cnf_return = set()
    
    # iterate all set input
    for com in combine:
        # iterate every rule in cnf
        for row in cnf:
            # if the set element in body of current rule
            if com in row[1]:
                # add the head of current rule into cnf_return
                cnf_return.add(row[0])
    
    # in no cnf rule match, return empty set
    if cnf_return == set():
        return empty
    # else return the cnf head(s)
    else:
        return cnf_return
