from triangular_table import *

def cyk_algorithm(cnf, string):
    table = create_table(string)
    filling_bottom(cnf, table, string)
    filling_all(cnf, table)