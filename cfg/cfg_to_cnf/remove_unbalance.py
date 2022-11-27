import re
from copy import deepcopy

small = re.compile(r'[a-z]')
capital = re.compile(r'[A-Z]')

# remove pattern aA
def remove_not_balance(cfg):
    terminal = find_terminal(cfg)
    terminal_rule = create_terminal_rule(terminal)
    remove_unstable(terminal_rule, cfg)
    

# find all terminal symbol in cfg
def find_terminal(cfg):
    terminal_symbol = set()

    for row in cfg:
        for element in row[1]:
            terminal = small.findall(element)
            for ter in terminal:
                terminal_symbol.add(ter)

    return terminal_symbol

# create fix rule with 1 terminal
def create_terminal_rule(terminal):
    new = []
    greeks = ['Z', 'Y', 'X', 'W', 'V', 'U', 'R', 'Q', 'P', 'O']
    
    for i, ter in enumerate(terminal):
        new.append([greeks[i], {ter}])
    
    return new

# remove the aA pattern
def remove_unstable(terminal_rule, cfg):
    temp_cfg = deepcopy(cfg)
    used = []

    for i, row in enumerate(temp_cfg):
        for element in row[1]:
            terminal = small.findall(element)
            non_terminal = capital.findall(element)
            
            if len(element) >= 2 and len(terminal) >= 1 and len(non_terminal) >= 1:
                
                for j, rule in enumerate(terminal_rule):
                    if terminal[0] in rule[1]:
                        if j not in used:
                            used.append(j)
                            cfg.append(rule)
                        
                        new = []
                        for char in element:
                            if char == terminal[0]:
                                new.append(rule[0])
                            else:
                                new.append(char)

                        cfg[i][1].remove(element)
                        cfg[i][1].add(''.join(new))