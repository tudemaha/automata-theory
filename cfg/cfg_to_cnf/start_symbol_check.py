# add new rule if in body a start symbol
def check_start_in_body(start_symbol, cfg):
    # if the start symbol appear in body
    if check_body(start_symbol, cfg):
        # append new rule (start* -> start) to cfg
        cfg.append([f'{start_symbol}*', {start_symbol}])

# check if there's bodies contain start symbol
def check_body(start_symbol, cfg):
    # iterate every rule in cfg
    for row in cfg:
        # iterate every body in 
        for element in row[1]:
            # if start symbol appear in current element
            if start_symbol in element:
                # return true 
                return True
    
    # if no start symbol in all body, return false
    return False