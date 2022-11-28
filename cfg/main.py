# import the required libraries
from numpy import array
from cfg_to_cnf.cfg_to_cnf import conversion
from cyk_algorithm.cyk_conversion import cyk_algorithm

# the cfg input
cfg = [
    ['T', {'TT'}],
    ['T', {'A'}],
    ['A', {'aAa'}],
    ['A', {'bB'}],
    ['B', {'bB'}],
    ['B', {'ε'}]
]

# the string to check
string = 'abab'

# convert the cfg to cnf first
cnf = conversion(cfg)
# print the cnf output
print(array(cnf), '\n')

# check the input string using the cnf rules
cyk_algorithm(cnf, string)