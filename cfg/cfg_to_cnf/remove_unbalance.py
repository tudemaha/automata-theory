# import all required library
import re
from copy import deepcopy

# define small and capital letters in regex
small = re.compile(r'[a-z]')
capital = re.compile(r'[A-Z]')

# remove pattern aA
def remove_not_balance(cfg):
    # find all terminal symbol used in rule
    terminal = find_terminal(cfg)
    # create rule than only contain terminal symbol in its body
    terminal_rule = create_terminal_rule(terminal)
    # removet the aA form
    remove_unstable(terminal_rule, cfg)
    

# find all terminal symbol in cfg
def find_terminal(cfg):
    # empty set to store all terminal symbol used in rules
    terminal_symbol = set()

    # iterate every rules in cfg
    for row in cfg:
        # iterate every element in body
        for element in row[1]:
            # find all terminal symbol used in element
            terminal = small.findall(element)
            # add all terminal symbol to terminal_symbol set
            for ter in terminal:
                terminal_symbol.add(ter)

    # return the terminal_symbol
    return terminal_symbol

# create fix rule with 1 terminal
def create_terminal_rule(terminal):
    # empty list to store the rule that only contains terminal symbols in its body
    new = []
    # list of capital letter to be used for head
    greeks = ['Z', 'Y', 'X', 'W', 'V', 'U', 'R', 'Q', 'P', 'O']
    
    # iterate every terminal symbol stored
    for i, ter in enumerate(terminal):
        # append new rule in form A -> a to 'new' list
        new.append([greeks[i], {ter}])
    
    # return the new rules
    return new

# remove the aA pattern
def remove_unstable(terminal_rule, cfg):
    # create a deep copy of cfg input
    temp_cfg = deepcopy(cfg)
    # empty list to store all the used all the rule in form A -> a
    used = []

    # iterate every rule in temp_cfg
    for i, row in enumerate(temp_cfg):
        # iterate every element in current rule's body
        for element in row[1]:
            # find all terminal symbols and non terminal symbols from current element
            terminal = small.findall(element)
            non_terminal = capital.findall(element)
            
            # if number of element >= 2 and number of terminal >= 1 and number of non terminal >=
            if len(element) >= 2 and len(terminal) >= 1 and len(non_terminal) >= 1:
                
                # iterarte all the rule that just contain terminal symbol in its body
                for j, rule in enumerate(terminal_rule):
                    # if the terminal appear in body of terminal_rule
                    if terminal[0] in rule[1]:
                        # if index j not in list used (the terminal_rule not used yet)
                        if j not in used:
                            # append the index j into used
                            used.append(j)
                            # append the terminal_rule to cfg
                            cfg.append(rule)
                        
                        # empty list to store the new body to replace aA form
                        new = []
                        # iterate every char in element of current cfg rule
                        for char in element:
                            # if char of current element is equal to first char in terminal list
                            if char == terminal[0]:
                                # append the head of rule contain the char in its body
                                new.append(rule[0])
                            else:
                                # else, just append the char to 'new' list
                                new.append(char)

                        # remove the current element in current body of rule in cfg
                        cfg[i][1].remove(element)
                        # append the new form to the body of current rule
                        cfg[i][1].add(''.join(new))