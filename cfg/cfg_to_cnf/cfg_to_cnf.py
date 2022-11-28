# import all required module to perform conversion
from cfg_to_cnf.join_rules import join
from cfg_to_cnf.start_symbol_check import check_start_in_body
from cfg_to_cnf.null_production import remove_null_production
from cfg_to_cnf.unit_production import remove_unit_production
from cfg_to_cnf.remove_unbalance import remove_not_balance
from cfg_to_cnf.remove_more import remove_more_two

# function to perform conversion from cfg to cnf
def conversion(cfg):
    # join the same head into one rule
    cfg = join(cfg)
    # check if the start symbol is in the body
    check_start_in_body('T', cfg)
    # remove the null production
    cfg = remove_null_production(cfg)
    # remove the unit production
    cfg = remove_unit_production(cfg)
    # replace the production in aA form
    remove_not_balance(cfg)
    # replace the production in aAa form
    remove_more_two(cfg)  

    # return the cfg that has been converted to cnf
    return cfg