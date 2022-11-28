# import all function from the module
from cyk_algorithm.triangular_table import *

# function to perform cyk algorithm
def cyk_algorithm(cnf, string):
    # create the filling table
    table = create_table(string)
    # fill the first value into the table
    filling_bottom(cnf, table, string)
    # fill all the table with the right value
    filling_all(cnf, table)