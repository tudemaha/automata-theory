from numpy import array
from cfg_to_cnf import conversion
from cyk_conversion import cyk_algorithm

cfg = [
    ['T', {'TT'}],
    ['T', {'A'}],
    ['A', {'aAa'}],
    ['A', {'bB'}],
    ['B', {'bB'}],
    ['B', {'ε'}]
]

string = 'abab'

cnf = conversion(cfg)
print(array(cnf), '\n')

cyk_algorithm(cnf, string)