from cfg_to_cnf.join_rules import join
from cfg_to_cnf.start_symbol_check import check_start_in_body
from cfg_to_cnf.null_production import remove_null_production
from cfg_to_cnf.unit_production import remove_unit_production
from cfg_to_cnf.remove_unbalance import remove_not_balance
from cfg_to_cnf.remove_more import remove_more_two

def conversion(cfg):
    cfg = join(cfg)
    check_start_in_body('T', cfg)
    cfg = remove_null_production(cfg)
    cfg = remove_unit_production(cfg)
    remove_not_balance(cfg)
    remove_more_two(cfg)  

    return cfg