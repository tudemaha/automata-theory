from join_rules import join
from start_symbol_check import check_start_in_body
from null_production import remove_null_production
from unit_production import remove_unit_production
from remove_unbalance import remove_not_balance
from remove_more import remove_more_two

def conversion(cfg):
    cfg = join(cfg)
    check_start_in_body('T', cfg)
    cfg = remove_null_production(cfg)
    cfg = remove_unit_production(cfg)
    remove_not_balance(cfg)
    remove_more_two(cfg)  

    return cfg

# print(conversion(cfg = [
#     ['T', {'TT'}],
#     ['T', {'A'}],
#     ['A', {'aAa'}],
#     ['A', {'bB'}],
#     ['B', {'bB'}],
#     ['B', {'ε'}]
# ]))