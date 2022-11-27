from cfg_to_cnf import conversion
from triangular_table import *
cfg = [
    ['T', {'TT'}],
    ['T', {'A'}],
    ['A', {'aAa'}],
    ['A', {'bB'}],
    ['B', {'bB'}],
    ['B', {'ε'}]
]

cnf = conversion(cfg)

string = 'bbaba'

table = create_table(string)
filling_bottom(cnf, table, string)
filling_all(cnf, table)

print('\n', cnf)