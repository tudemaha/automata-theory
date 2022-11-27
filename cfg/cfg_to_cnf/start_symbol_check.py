# add new rule if in body a start symbol
def check_start_in_body(start_symbol, cfg):
    if check_body(start_symbol, cfg):
        cfg.append([f'{start_symbol}*', {start_symbol}])

# check if there's bodies contain start symbol
def check_body(start_symbol, cfg):
    contain = False

    for row in cfg:
        for element in row[1]:
            if start_symbol in element:
                contain = True
                return contain
            
    return contain